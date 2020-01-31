select

	F.CNPJ,
	MDF.Chave_Acesso as 'CHAVE',
    MDF.XML_Autorizacao,

	MDF.XML_Documento + 
	MDF.XML_Autorizacao as 'XML_Documento',

	NE.Xml_Evento,
	NE.Xml_Evento +
	NE.Xml_Retorno as 'XML_Documento_Cancelamento'

from Movimento_Documentos_Fiscais MDF

left join Movimento M on M.Ordem = MDF.Ordem_Movimento
left join Filiais F on F.Ordem = M.Ordem_Filial
left join Operacoes O on O.Ordem = M.Ordem_Operacao
left join NFe_Eventos NE on NE.Ordem_Movimento_Documentos_Fiscais = MDF.Ordem

where

    F.CNPJ = '' and
	CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and -- Data da competencia
	MDF.Modelo in('55','65') and -- 55 NFe ou 65 NFCe
	MDF.Codigo_Status in(100, 150) and -- 100 Autorizado ou 302 Denegado
	MDF.Documento_Cancelado in(0) -- 0 Autorizados ou 1 Canceladas
	and O.Entrada_Saida in('E', 'S')

order by MDF.Chave_Acesso