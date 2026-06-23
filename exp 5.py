from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timezone

def validate_certificate(cert_file):

    try:
        with open(cert_file, "rb") as file:
            cert_data = file.read()

        certificate = x509.load_pem_x509_certificate(
            cert_data,
            default_backend()
        )

        print("\n--- Certificate Details ---")

        print("\nSubject:")
        print(certificate.subject)

        print("\nIssuer:")
        print(certificate.issuer)

        print("\nSerial Number:")
        print(certificate.serial_number)

        print("\nValid From:")
        print(certificate.not_valid_before_utc)

        print("\nValid Until:")
        print(certificate.not_valid_after_utc)

        print("\nPublic Key:")
        print(certificate.public_key())

        current_time = datetime.now(timezone.utc)

        if certificate.not_valid_before_utc <= current_time <= certificate.not_valid_after_utc:
            print("\nValidity Status: Certificate is currently valid.")
        else:
            print("\nValidity Status: Certificate has expired or is not yet valid.")

        if certificate.issuer == certificate.subject:
            print("\nCertificate Type: Self-Signed Certificate")
        else:
            print("\nCertificate Type: Issued by Certificate Authority")

    except FileNotFoundError:
        print("Certificate file not found!")

    except Exception as e:
        print("Error while reading certificate:", e)


filename = input("Enter certificate file name (example: certificate.pem): ")
validate_certificate(filename)