# from rest_framework_xml.renderers import XMLRenderer
#
#
# class YMLServiceXMLRenderer(XMLRenderer):
#     root_tag_name = 'yml_catalog'
#     item_tag_name = 'category'
#
#     def _to_xml(self, xml, data):
#         if isinstance(data, (list, tuple)):
#             for item in data:
#                 xml.startElement(self.item_tag_name, {'id': str(item['id'])})
#                 self._to_xml(xml, item)
#                 xml.endElement(self.item_tag_name)
#         super()._to_xml(xml, data)


"""
Provides XML rendering support.
"""
from io import StringIO

from django.db.models.functions.datetime import datetime
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.feedgenerator import rfc3339_date
from django.utils.xmlutils import SimplerXMLGenerator
from rest_framework.renderers import BaseRenderer

from config.settings import TIME_ZONE


class YMLServiceXMLRenderer(BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = "application/xml"
    format = "xml"
    charset = "utf-8"
    item_tag_name = "list-item"
    root_tag_name = "yml_catalog"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ""

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(self.root_tag_name, {"date": str(rfc3339_date(datetime.now(timezone.get_current_timezone())))})

        self._to_xml(xml, data)

        xml.endElement(self.root_tag_name)
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.item_tag_name, {})
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)

        elif isinstance(data, dict):
            for key, value in data.items():
                xml.startElement(key, {})
                self._to_xml(xml, value)
                xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_str(data))
