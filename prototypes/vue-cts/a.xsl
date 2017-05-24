<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:output method="html" />
  <xsl:template match="/">
    <xsl:apply-templates select="//tei:TEI" />
  </xsl:template>
</xsl:stylesheet>
