<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text"/>

  <xsl:template match="/users">
    <xsl:for-each select="user">
      INSERT INTO moodle_users (id, username, email, firstname, lastname, idnumber, password, city, country) VALUES (
      '<xsl:value-of select="id"/>',
      '<xsl:value-of select="username"/>',
      '<xsl:value-of select="email"/>',
      '<xsl:value-of select="firstname"/>',
      '<xsl:value-of select="lastname"/>',
      '<xsl:value-of select="idnumber"/>',
      '<xsl:value-of select="password"/>',
      '<xsl:value-of select="city"/>',
      '<xsl:value-of select="country"/>'
      );
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
