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
        tag = {}
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.item_tag_name, tag)
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)

        elif isinstance(data, dict):
            for key, value in data.items():
                self.item_tag_name = key
                xml.startElement(key, tag)
                if self.item_tag_name == 'categories':
                    for id, category in value.items():
                        xml.startElement('category', {'id': id})
                        xml.characters(force_str(category))
                        xml.endElement('category')
                elif self.item_tag_name == 'offers':
                    for service in value:
                        xml.startElement('offer', {'id': service['id']})
                        service.pop('id')
                        for field_name, field_data in service.items():
                            xml.startElement(field_name, {})
                            xml.characters(force_str(field_data))
                            xml.endElement(field_name)
                        xml.endElement('offer')
                else:
                    self._to_xml(xml, value)
                xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_str(data))
