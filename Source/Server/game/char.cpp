//search for:
pack.bPKMode	= m_bPKMode;

//add under:
ChatPacket(CHAT_TYPE_COMMAND, "SendRealStatus %d %d %d %d", GetRealPoint(POINT_HT), GetRealPoint(POINT_IQ), GetRealPoint(POINT_ST), GetRealPoint(POINT_DX));