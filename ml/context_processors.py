from accounts.templatetags.custom_filters import calculate_age
from patients.models import Feedback
from .models import GeneralSettings


def general_settings(request):
    # Default data
    data = {
        "site_name": "QuickDiag",
        "site_company": "Zila Tech",
        "site_telephone": "(123) 456-7890",
        "site_contact_email": "info.quickdiag@gmail.com",
        "site_address": "123 Main Street, Paraku Estate, XEZ",
        "site_tagline": "Empowering Early Detection, Saving Lives",
        "site_description": "",
        "site_allow_registration": True,
        "site_maintenance_mode": False,
    }

    # Attempt to get settings from the database
    settings = GeneralSettings.objects.first()

    # If settings exist, override defaults where values are not None
    if settings:
        data.update(
            {
                "site_name": settings.site_name or data["site_name"],
                "site_company": settings.company or data["site_company"],
                "site_tagline": settings.tagline or data["site_tagline"],
                "site_description": settings.site_description
                or data["site_description"],
                "site_allow_registration": (
                    settings.allow_registration
                    if settings.allow_registration is not None
                    else data["site_allow_registration"]
                ),
                "site_maintenance_mode": (
                    settings.maintenance_mode
                    if settings.maintenance_mode is not None
                    else data["site_maintenance_mode"]
                ),
                "site_telephone": settings.telephone or data["site_telephone"],
                "site_contact_email": settings.contact_email
                or data["site_contact_email"],
                "site_address": settings.address or data["site_address"],
            }
        )

    # Return the context data
    return data


def feedback_testimonials(request):
    feedbacks = Feedback.objects.filter(show=True).order_by("-submitted_at")[:3]
    if feedbacks.exists():
        testimonials = []
        for feedback in feedbacks:
            obj = feedback.result
            testimonial = {
                "name": obj.user.full_name(),
                "message": feedback.message,
                "age": calculate_age(obj.dob),
                "risk_level": obj.risk_level,
            }
            testimonials.append(testimonial)
    else:
        testimonials = [
            {
                "name": "Mary Johnson",
                "message": "After taking the assessment, I followed the recommended screenings and caught my cancer early. The early detection saved my life.",
                "age": 45,
                "risk_level": "High",
            },
            {
                "name": "Linda Smith",
                "message": "The personalized advice helped me understand my risk factors and take proactive steps to improve my health.",
                "age": 38,
                "risk_level": "Medium",
            },
            {
                "name": "Jane Doe",
                "message": "I found the resources and support links extremely helpful. It gave me the confidence to get the necessary screenings.",
                "age": 50,
                "risk_level": "Low",
            },
        ]
    return {"testimonials": testimonials}
