import io
import base64
from collections import OrderedDict
from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from googleapiclient.errors import HttpError
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

maps = OrderedDict({
    "type": settings.GMAIL_TYPE,
    "project_id": settings.GMAIL_PROJECT_ID,
    "private_key_id": settings.GMAIL_PRIVATE_KEY_ID,
    "private_key": settings.GMAIL_PRIVATE_KEY,
    "client_email": settings.GMAIL_CLIENT_EMAIL,
    "client_id": settings.GMAIL_CLIENT_ID,
    "auth_uri": settings.GMAIL_AUTH_URI,
    "token_uri": settings.GMAIL_TOKEN_URI,
    "auth_provider_x509_cert_url": settings.GMAIL_AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url": settings.GMAIL_CLIENT_X509_CERT_URL
}
)
try:
    SERVICE_ACCOUNT_FILE = 'service_account.json'

    credentials = service_account.Credentials.from_service_account_info(
        info=maps,
        scopes=[settings.GMAIL_SCOPES],
        subject=settings.GMAIL_SUBJECT
    )
    service = build('gmail', 'v1', credentials=credentials)
except Exception:
    pass


def render_to_pdf(template_src, context_dict={}):
    """Render a template to a pdf file"""
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return pdf


def send_mail_invoice(invoice):
    """Create a PDF invoice file and email it"""
    message = MIMEMultipart()
    message['to'] = ''
    message['subject'] = 'Invoice'
    context = {
        'invoice_number': invoice.invoice_number,
        'user': invoice.user.get_full_name(),
        'date': invoice.created_at,
        'amount': invoice.card.total_cost(),
        'carditems': invoice.card.card_items,
    }
    html = render_to_string(
        'invoice.html', context
    )
    # Convert the HTML content to PDF using Pisa
    pdf_file = io.BytesIO()
    pisa.CreatePDF(html, pdf_file)
    pdf_file.seek(0)

    # Attach the PDF file to the email
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
    pdf_attachment.add_header('Content-Disposition', 'attachment',
                              filename=f'Invoive_{invoice.invoice_number}.pdf')
    message.attach(pdf_attachment)

    # Send the email using the Gmail API
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    try:
        message = service.users().messages().send(
            userId='me', body={'raw': raw_message}).execute()
    except HttpError:
        pass
