select

	F.CNPJ

from Movimento_Documentos_Fiscais MDF

left join Movimento M on M.Ordem = MDF.Ordem_Movimento
left join Filiais F on F.Ordem = M.Ordem_Filial
left join Operacoes O on O.Ordem = M.Ordem_Operacao

where

	CONVERT(varchar(8),MDF.Data_Emissao, 11) = convert(varchar(8),DATEADD(DAY,-2,GETDATE()),11) and -- Data da competencia
	MDF.Modelo in('55','65') and -- 55 NFe ou 65 NFCe
	MDF.Codigo_Status in(100, 150) and -- 100 Autorizado ou 302 Denegado
	MDF.Documento_Cancelado in(0) -- 0 Autorizados ou 1 Canceladas
	and O.Entrada_Saida in('E', 'S')

group by F.CNPJ
order by F.CNPJ