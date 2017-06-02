<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:output method="html" />

  <xsl:template match="/">
    <xsl:apply-templates select="//tei:TEI" />
  </xsl:template>

  <xsl:template match="tei:div">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:p">
    <p><xsl:apply-templates /></p>
  </xsl:template>

  <xsl:template match="tei:l">
    <div><xsl:apply-templates /> {<xsl:value-of select="@n"/>}</div>
  </xsl:template>

  <xsl:template match="*">
    [<xsl:value-of select="local-name()"/>
      <xsl:for-each select="@*">
        <xsl:text> </xsl:text>
        <xsl:value-of select="name()"/>=<xsl:value-of select="."/>
      </xsl:for-each>]
    <xsl:apply-templates />
    [/<xsl:value-of select ="local-name()"/>]
  </xsl:template>
</xsl:stylesheet>
