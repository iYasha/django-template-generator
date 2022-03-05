from rest_framework import mixins
import rest_framework.viewsets as vs


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                vs.GenericViewSet):
    pass


class CreateMixin(mixins.CreateModelMixin, vs.GenericViewSet):
    pass


class ManyActions(vs.GenericViewSet):
    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class BaseView(vs.GenericViewSet):
    serializer_action_classes = {}

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
