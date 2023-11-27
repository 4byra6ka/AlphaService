from rest_framework_xml.renderers import XMLRenderer


class YMLServiceXMLRenderer(XMLRenderer):
    root_tag_name = 'yml_catalog'
    item_tag_name = 'category'

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.item_tag_name, {'id': str(item['id'])})
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)
        super()._to_xml(xml, data)