<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:output method="html" />

  <xsl:template match="/">
    <xsl:apply-templates select="//tei:TEI" />
  </xsl:template>

  <xsl:template match="tei:TEI">
    <div class="TEI"><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:div[@subtype='verse']">
    <div>{<xsl:value-of select="@n"/>}<xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:div">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:p">
    <p><xsl:apply-templates /></p>
  </xsl:template>

  <xsl:template match="tei:add">
    <ins><xsl:apply-templates /></ins>
  </xsl:template>

  <xsl:template match="tei:del">
    <del><xsl:apply-templates /></del>
  </xsl:template>

  <xsl:template match="tei:pb">
    <hr/>
  </xsl:template>

  <xsl:template match="tei:milestone[@unit='para']">
    <br/>&#xB6;
  </xsl:template>

  <xsl:template match="tei:milestone">
    <span class="milestone">
      <xsl:value-of select="@unit"/>
      <xsl:text>:</xsl:text>
      <xsl:value-of select="@n"/>
      <xsl:text> </xsl:text>
    </span>
  </xsl:template>

  <xsl:template match="tei:l[@n]">
    <div class="l">
      <xsl:apply-templates />
      <span class="n"><xsl:text> </xsl:text><xsl:value-of select="@n"/></span>
    </div>
  </xsl:template>

  <xsl:template match="tei:l">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:lb">
    <br/>
    <xsl:apply-templates />
  </xsl:template>

  <xsl:template match="tei:quote">
    <q><xsl:apply-templates /></q>
  </xsl:template>

  <xsl:template match="tei:q">
    <q><xsl:apply-templates /></q>
  </xsl:template>

  <xsl:template match="tei:sp">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:title">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:said">
    <div class="said"><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:label">
    <div class="label"><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:persName">
    <span><xsl:apply-templates /></span>
  </xsl:template>

  <xsl:template match="tei:seg">
    <span><xsl:apply-templates /></span>
  </xsl:template>

  <xsl:template match="tei:date">
    <span><xsl:apply-templates /></span>
  </xsl:template>

  <xsl:template match="tei:foreign">
    <span><xsl:apply-templates /></span>
  </xsl:template>

  <xsl:template match="tei:note">
    <span><xsl:apply-templates /></span>
  </xsl:template>

  <xsl:template match="tei:head">
    <heading><xsl:apply-templates /></heading>
  </xsl:template>

  <xsl:template match="tei:text">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:body">
    <div><xsl:apply-templates /></div>
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
