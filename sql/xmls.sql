select

	F.CNPJ,
	O.Entrada_Saida as 'E/S',
	F.CNPJ as 'CNPJ',
	MDF.Data_Emissao as 'DATA EMISS�O',
	MDF.Chave_Acesso as 'CHAVE',
	MDF.Modelo as 'MODELO',
	MDF.Serie as 'SERIE',
	MDF.Numero as 'NUMERO',
	M.Preco_Total_Com_Desconto_Somado as 'VALOR',
	M.ICMS_Normal_Base_Somado as 'BASE ICMS',
	M.ICMS_Normal_Valor_Somado as 'VALOR ICMS',

	replace(replace(replace(replace(
	concat(MDF.Codigo_Status,'-', MDF.Documento_Cancelado)
	,'100-1','CANCELADA')
	,'100-0','AUTORIZADA')
	,'150-0','AUTORIZADA')
	,'302-0','DENEGADA')
	as 'STATUS',

    MDF.XML_Autorizacao,

	MDF.XML_Documento +
	MDF.XML_Autorizacao as 'XML_Documento'

from Movimento_Documentos_Fiscais MDF

left join Movimento M on M.Ordem = MDF.Ordem_Movimento
left join Filiais F on F.Ordem = M.Ordem_Filial
left join Operacoes O on O.Ordem = M.Ordem_Operacao

where

	CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-1,GETDATE()),11) and -- Data da compet�ncia
	MDF.Modelo in('55','65') and -- 55 NFe ou 65 NFCe
	MDF.Codigo_Status in(100, 150) and -- 100 Autorizado ou 302 Denegado
	MDF.Documento_Cancelado in(0) -- 0 Autorizados ou 1 Canceladas
	and O.Entrada_Saida in('E', 'S')

order by MDF.Chave_Acesso