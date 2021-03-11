from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from rest_framework.authtoken.models import Token
from django.db.utils import IntegrityError

from .models import Event, EventType


# Test Route
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"msg": "Hello World!!!"}
        return Response(content)


# Main Route
class EventView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_token = get_authorization_header(request).decode().split()[1]
            user = Token.objects.get(key=user_token).user
            try:
                Event.objects.get(user=user)
                return Response({"msg": "You have already created an event"})
            except Event.DoesNotExist:
                pass
            try:
                event_t = EventType.objects.get(name=request.data.get("event_type"))
            except EventType.DoesNotExist:
                event_t = EventType(name=request.data.get("event_type"))
                event_t.save()
            new_event = Event(
                user=user, event_type=event_t, info=request.data.get("info"), timestamp=request.data.get("timestamp")
            )
            new_event.save()
            return Response({"msg": "Event created!"})
        except IntegrityError:
            return Response({"msg": "Bad Body"})
        except Exception:
            return Response({"msg": "Something went wrong!"})
