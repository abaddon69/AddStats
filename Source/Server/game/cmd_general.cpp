// search for:
ACMD(do_stat)

//replace whole function:
ACMD(do_stat)
{
	char arg1[256], arg2[256];
	int value = 0;
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	if (!*arg1)
		return;
	
	if (!*arg2)
		value = 1;
	else
		value = atoi(arg2);
	
	if (value < 0)
		return;
	
	if (value == 0)
		value = 1;

	if (ch->IsPolymorphed())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("µĐ°© Áßżˇ´Â ´É·ÂŔ» żĂ¸± Ľö ľř˝Ŕ´Ď´Ů."));
		return;
	}

	if (ch->GetPoint(POINT_STAT) <= 0)
		return;
	
	if (ch->GetPoint(POINT_STAT) < value)
		return;

	BYTE idx = 0;
	
	if (!strcmp(arg1, "st"))
		idx = POINT_ST;
	else if (!strcmp(arg1, "dx"))
		idx = POINT_DX;
	else if (!strcmp(arg1, "ht"))
		idx = POINT_HT;
	else if (!strcmp(arg1, "iq"))
		idx = POINT_IQ;
	else
		return;

	if (ch->GetRealPoint(idx) + value > MAX_STAT)
		return;

	ch->SetRealPoint(idx, ch->GetRealPoint(idx) + value);
	ch->SetPoint(idx, ch->GetPoint(idx) + value);
	ch->ComputePoints();
	ch->PointChange(idx, 0);

	if (idx == POINT_IQ)
	{
		ch->PointChange(POINT_MAX_HP, 0);
	}
	else if (idx == POINT_HT)
	{
		ch->PointChange(POINT_MAX_SP, 0);
	}

	ch->PointChange(POINT_STAT, -value);
	ch->ComputePoints();
}