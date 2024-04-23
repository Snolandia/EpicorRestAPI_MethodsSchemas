import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuoteSvc
# Description: Quote Business Object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Quotes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Quotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Quotes
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes",headers=creds) as resp:
           return await resp.json()

async def post_Quotes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Quotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum(Company, QuoteNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Quote item
   Description: Calls GetByID to retrieve the Quote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Quote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Quotes_Company_QuoteNum(Company, QuoteNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Quote for the service
   Description: Calls UpdateExt to update Quote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Quote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Quotes_Company_QuoteNum(Company, QuoteNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Quote item
   Description: Call UpdateExt to delete Quote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Quote
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QSalesRPs(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QSalesRPs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QSalesRPs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QSalesRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QSalesRPs",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QSalesRPs_Company_QuoteNum_SalesRepCode(Company, QuoteNum, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QSalesRP item
   Description: Calls GetByID to retrieve the QSalesRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QSalesRP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteCnts(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteCnts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteCnts",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company, QuoteNum, CustNum, ShipToNum, ConNum, PerConID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCnt item
   Description: Calls GetByID to retrieve the QuoteCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCnt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param PerConID: Desc: PerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteComs(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteComs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteComs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteComRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteComs",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteComs_Company_QuoteNum_CompNum(Company, QuoteNum, CompNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCom item
   Description: Calls GetByID to retrieve the QuoteCom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCom1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CompNum: Desc: CompNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteDtls(Company, QuoteNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteDtls",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteDtls_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtl item
   Description: Calls GetByID to retrieve the QuoteDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedMscs(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedMscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedMscs",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedMsc item
   Description: Calls GetByID to retrieve the QuoteHedMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedMsc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedTaxes(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedTaxes",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company, QuoteNum, TaxCode, RateCode, ClaimsTax, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedTax item
   Description: Calls GetByID to retrieve the QuoteHedTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ClaimsTax: Desc: ClaimsTax   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedAttches(Company, QuoteNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteHedAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedAttches",headers=creds) as resp:
           return await resp.json()

async def get_Quotes_Company_QuoteNum_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company, QuoteNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedAttch item
   Description: Calls GetByID to retrieve the QuoteHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Quotes(" + Company + "," + QuoteNum + ")/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QSalesRPs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QSalesRPs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QSalesRPs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QSalesRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs",headers=creds) as resp:
           return await resp.json()

async def post_QSalesRPs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QSalesRPs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QSalesRPs_Company_QuoteNum_SalesRepCode(Company, QuoteNum, SalesRepCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QSalesRP item
   Description: Calls GetByID to retrieve the QSalesRP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QSalesRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QSalesRPs_Company_QuoteNum_SalesRepCode(Company, QuoteNum, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QSalesRP for the service
   Description: Calls UpdateExt to update QSalesRP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QSalesRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QSalesRPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QSalesRPs_Company_QuoteNum_SalesRepCode(Company, QuoteNum, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QSalesRP item
   Description: Call UpdateExt to delete QSalesRP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QSalesRP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QSalesRPs(" + Company + "," + QuoteNum + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteCnts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteCnts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts",headers=creds) as resp:
           return await resp.json()

async def post_QuoteCnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company, QuoteNum, CustNum, ShipToNum, ConNum, PerConID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCnt item
   Description: Calls GetByID to retrieve the QuoteCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param PerConID: Desc: PerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company, QuoteNum, CustNum, ShipToNum, ConNum, PerConID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteCnt for the service
   Description: Calls UpdateExt to update QuoteCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param PerConID: Desc: PerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteCnts_Company_QuoteNum_CustNum_ShipToNum_ConNum_PerConID(Company, QuoteNum, CustNum, ShipToNum, ConNum, PerConID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteCnt item
   Description: Call UpdateExt to delete QuoteCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param PerConID: Desc: PerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCnts(" + Company + "," + QuoteNum + "," + CustNum + "," + ShipToNum + "," + ConNum + "," + PerConID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteComs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteComs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteComs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteComRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs",headers=creds) as resp:
           return await resp.json()

async def post_QuoteComs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteComs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteComs_Company_QuoteNum_CompNum(Company, QuoteNum, CompNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCom item
   Description: Calls GetByID to retrieve the QuoteCom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CompNum: Desc: CompNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteComs_Company_QuoteNum_CompNum(Company, QuoteNum, CompNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteCom for the service
   Description: Calls UpdateExt to update QuoteCom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CompNum: Desc: CompNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteComRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteComs_Company_QuoteNum_CompNum(Company, QuoteNum, CompNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteCom item
   Description: Call UpdateExt to delete QuoteCom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param CompNum: Desc: CompNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteComs(" + Company + "," + QuoteNum + "," + CompNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls",headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtl item
   Description: Calls GetByID to retrieve the QuoteDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteDtls_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteDtl for the service
   Description: Calls UpdateExt to update QuoteDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteDtls_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteDtl item
   Description: Call UpdateExt to delete QuoteDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteCoParts(Company, QuoteNum, QuoteLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteCoParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteCoParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCoPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteCoParts",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company, QuoteNum, QuoteLine, CoPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCoPart item
   Description: Calls GetByID to retrieve the QuoteCoPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCoPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttrValueSets(Company, QuoteNum, QuoteLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlAttrValueSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlAttrValueSets1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company, QuoteNum, QuoteLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlAttrValueSet item
   Description: Calls GetByID to retrieve the QuoteDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttrValueSet1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlTaxes(Company, QuoteNum, QuoteLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company, QuoteNum, QuoteLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlTax item
   Description: Calls GetByID to retrieve the QuoteDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteMscs(Company, QuoteNum, QuoteLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteMscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteMscs",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMsc item
   Description: Calls GetByID to retrieve the QuoteMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMsc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteQties(Company, QuoteNum, QuoteLine, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteQties items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteQties1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteQties",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company, QuoteNum, QuoteLine, QtyNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteQty item
   Description: Calls GetByID to retrieve the QuoteQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteQty1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttches(Company, QuoteNum, QuoteLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuoteDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuoteDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtls_Company_QuoteNum_QuoteLine_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company, QuoteNum, QuoteLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlAttch item
   Description: Calls GetByID to retrieve the QuoteDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtls(" + Company + "," + QuoteNum + "," + QuoteLine + ")/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteCoParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteCoParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteCoParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteCoPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts",headers=creds) as resp:
           return await resp.json()

async def post_QuoteCoParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteCoParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company, QuoteNum, QuoteLine, CoPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteCoPart item
   Description: Calls GetByID to retrieve the QuoteCoPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteCoPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company, QuoteNum, QuoteLine, CoPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteCoPart for the service
   Description: Calls UpdateExt to update QuoteCoPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteCoPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteCoPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteCoParts_Company_QuoteNum_QuoteLine_CoPartNum(Company, QuoteNum, QuoteLine, CoPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteCoPart item
   Description: Call UpdateExt to delete QuoteCoPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteCoPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteCoParts(" + Company + "," + QuoteNum + "," + QuoteLine + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlAttrValueSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlAttrValueSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlAttrValueSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company, QuoteNum, QuoteLine, AttributeValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlAttrValueSet item
   Description: Calls GetByID to retrieve the QuoteDtlAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company, QuoteNum, QuoteLine, AttributeValueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteDtlAttrValueSet for the service
   Description: Calls UpdateExt to update QuoteDtlAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteDtlAttrValueSets_Company_QuoteNum_QuoteLine_AttributeValueSeq(Company, QuoteNum, QuoteLine, AttributeValueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteDtlAttrValueSet item
   Description: Call UpdateExt to delete QuoteDtlAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param AttributeValueSeq: Desc: AttributeValueSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttrValueSets(" + Company + "," + QuoteNum + "," + QuoteLine + "," + AttributeValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes",headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company, QuoteNum, QuoteLine, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlTax item
   Description: Calls GetByID to retrieve the QuoteDtlTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company, QuoteNum, QuoteLine, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteDtlTax for the service
   Description: Calls UpdateExt to update QuoteDtlTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteDtlTaxes_Company_QuoteNum_QuoteLine_TaxCode_RateCode_ECAcquisitionSeq(Company, QuoteNum, QuoteLine, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteDtlTax item
   Description: Call UpdateExt to delete QuoteDtlTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlTaxes(" + Company + "," + QuoteNum + "," + QuoteLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteMscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteMscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs",headers=creds) as resp:
           return await resp.json()

async def post_QuoteMscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteMsc item
   Description: Calls GetByID to retrieve the QuoteMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteMsc for the service
   Description: Calls UpdateExt to update QuoteMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteMsc item
   Description: Call UpdateExt to delete QuoteMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteQties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteQties
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties",headers=creds) as resp:
           return await resp.json()

async def post_QuoteQties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteQties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company, QuoteNum, QuoteLine, QtyNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteQty item
   Description: Calls GetByID to retrieve the QuoteQty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company, QuoteNum, QuoteLine, QtyNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteQty for the service
   Description: Calls UpdateExt to update QuoteQty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteQtyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum(Company, QuoteNum, QuoteLine, QtyNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteQty item
   Description: Call UpdateExt to delete QuoteQty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteQty
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_Qtmmkups(Company, QuoteNum, QuoteLine, QtyNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Qtmmkups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Qtmmkups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/Qtmmkups",headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company, QuoteNum, QuoteLine, QtyNum, ClassCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Qtmmkup item
   Description: Calls GetByID to retrieve the Qtmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qtmmkup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_QtQtyMscs(Company, QuoteNum, QuoteLine, QtyNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QtQtyMscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QtQtyMscs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtQtyMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/QtQtyMscs",headers=creds) as resp:
           return await resp.json()

async def get_QuoteQties_Company_QuoteNum_QuoteLine_QtyNum_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QtQtyMsc item
   Description: Calls GetByID to retrieve the QtQtyMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QtQtyMsc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteQties(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + ")/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Qtmmkups(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Qtmmkups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Qtmmkups
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups",headers=creds) as resp:
           return await resp.json()

async def post_Qtmmkups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Qtmmkups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company, QuoteNum, QuoteLine, QtyNum, ClassCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Qtmmkup item
   Description: Calls GetByID to retrieve the Qtmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qtmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company, QuoteNum, QuoteLine, QtyNum, ClassCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Qtmmkup for the service
   Description: Calls UpdateExt to update Qtmmkup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Qtmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QtmmkupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Qtmmkups_Company_QuoteNum_QuoteLine_QtyNum_ClassCode(Company, QuoteNum, QuoteLine, QtyNum, ClassCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Qtmmkup item
   Description: Call UpdateExt to delete Qtmmkup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Qtmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/Qtmmkups(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QtQtyMscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QtQtyMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QtQtyMscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QtQtyMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs",headers=creds) as resp:
           return await resp.json()

async def post_QtQtyMscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QtQtyMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QtQtyMsc item
   Description: Calls GetByID to retrieve the QtQtyMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QtQtyMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QtQtyMsc for the service
   Description: Calls UpdateExt to update QtQtyMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QtQtyMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QtQtyMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QtQtyMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QtQtyMsc item
   Description: Call UpdateExt to delete QtQtyMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QtQtyMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QtQtyMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company, QuoteNum, QuoteLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlAttch item
   Description: Calls GetByID to retrieve the QuoteDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company, QuoteNum, QuoteLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteDtlAttch for the service
   Description: Calls UpdateExt to update QuoteDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteDtlAttches_Company_QuoteNum_QuoteLine_DrawingSeq(Company, QuoteNum, QuoteLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteDtlAttch item
   Description: Call UpdateExt to delete QuoteDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteDtlAttches(" + Company + "," + QuoteNum + "," + QuoteLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedMscs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedMscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedMscs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs",headers=creds) as resp:
           return await resp.json()

async def post_QuoteHedMscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedMscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedMsc item
   Description: Calls GetByID to retrieve the QuoteHedMsc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteHedMsc for the service
   Description: Calls UpdateExt to update QuoteHedMsc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteHedMscs_Company_QuoteNum_QuoteLine_QtyNum_SeqNum(Company, QuoteNum, QuoteLine, QtyNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteHedMsc item
   Description: Call UpdateExt to delete QuoteHedMsc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedMsc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param QtyNum: Desc: QtyNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedMscs(" + Company + "," + QuoteNum + "," + QuoteLine + "," + QtyNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes",headers=creds) as resp:
           return await resp.json()

async def post_QuoteHedTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company, QuoteNum, TaxCode, RateCode, ClaimsTax, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedTax item
   Description: Calls GetByID to retrieve the QuoteHedTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ClaimsTax: Desc: ClaimsTax   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company, QuoteNum, TaxCode, RateCode, ClaimsTax, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteHedTax for the service
   Description: Calls UpdateExt to update QuoteHedTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ClaimsTax: Desc: ClaimsTax   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteHedTaxes_Company_QuoteNum_TaxCode_RateCode_ClaimsTax(Company, QuoteNum, TaxCode, RateCode, ClaimsTax, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteHedTax item
   Description: Call UpdateExt to delete QuoteHedTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ClaimsTax: Desc: ClaimsTax   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedTaxes(" + Company + "," + QuoteNum + "," + TaxCode + "," + RateCode + "," + ClaimsTax + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company, QuoteNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteHedAttch item
   Description: Calls GetByID to retrieve the QuoteHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company, QuoteNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteHedAttch for the service
   Description: Calls UpdateExt to update QuoteHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteHedAttches_Company_QuoteNum_DrawingSeq(Company, QuoteNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteHedAttch item
   Description: Call UpdateExt to delete QuoteHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/QuoteHedAttches(" + Company + "," + QuoteNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_HedTaxSums(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HedTaxSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HedTaxSums
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HedTaxSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums",headers=creds) as resp:
           return await resp.json()

async def post_HedTaxSums(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HedTaxSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company, HedNum, TaxCode, RateCode, AllocDepInvcNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HedTaxSum item
   Description: Calls GetByID to retrieve the HedTaxSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HedTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param AllocDepInvcNum: Desc: AllocDepInvcNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company, HedNum, TaxCode, RateCode, AllocDepInvcNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HedTaxSum for the service
   Description: Calls UpdateExt to update HedTaxSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HedTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param AllocDepInvcNum: Desc: AllocDepInvcNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HedTaxSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HedTaxSums_Company_HedNum_TaxCode_RateCode_AllocDepInvcNum(Company, HedNum, TaxCode, RateCode, AllocDepInvcNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HedTaxSum item
   Description: Call UpdateExt to delete HedTaxSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HedTaxSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HedNum: Desc: HedNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param AllocDepInvcNum: Desc: AllocDepInvcNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/HedTaxSums(" + Company + "," + HedNum + "," + TaxCode + "," + RateCode + "," + AllocDepInvcNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartSubs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartSubs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartSubs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSubsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs",headers=creds) as resp:
           return await resp.json()

async def post_PartSubs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartSubs_Company_PartNum_SubPart(Company, PartNum, SubPart, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartSub item
   Description: Calls GetByID to retrieve the PartSub item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartSub
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartSubs_Company_PartNum_SubPart(Company, PartNum, SubPart, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartSub for the service
   Description: Calls UpdateExt to update PartSub. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartSub
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartSubs_Company_PartNum_SubPart(Company, PartNum, SubPart, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartSub item
   Description: Call UpdateExt to delete PartSub item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartSub
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/PartSubs(" + Company + "," + PartNum + "," + SubPart + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxConnectStatus(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxConnectStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxConnectStatus
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxConnectStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus",headers=creds) as resp:
           return await resp.json()

async def post_TaxConnectStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxConnectStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxConnectStatus_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxConnectStatu item
   Description: Calls GetByID to retrieve the TaxConnectStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxConnectStatu
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxConnectStatus_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxConnectStatu for the service
   Description: Calls UpdateExt to update TaxConnectStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxConnectStatu
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxConnectStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxConnectStatus_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxConnectStatu item
   Description: Call UpdateExt to delete TaxConnectStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxConnectStatu
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/TaxConnectStatus(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhatIfSchedulings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhatIfSchedulings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhatIfSchedulings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhatIfSchedulingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings",headers=creds) as resp:
           return await resp.json()

async def post_WhatIfSchedulings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhatIfSchedulings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhatIfSchedulings_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhatIfScheduling item
   Description: Calls GetByID to retrieve the WhatIfScheduling item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhatIfScheduling
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhatIfSchedulings_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhatIfScheduling for the service
   Description: Calls UpdateExt to update WhatIfScheduling. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhatIfScheduling
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhatIfSchedulingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhatIfSchedulings_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhatIfScheduling item
   Description: Call UpdateExt to delete WhatIfScheduling item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhatIfScheduling
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/WhatIfSchedulings(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuoteHed, whereClauseQuoteHedAttch, whereClauseQSalesRP, whereClauseQuoteCnt, whereClauseQuoteCom, whereClauseQuoteDtl, whereClauseQuoteDtlAttch, whereClauseQuoteCoPart, whereClauseQuoteDtlAttrValueSet, whereClauseQuoteDtlTax, whereClauseQuoteMsc, whereClauseQuoteQty, whereClauseQtmmkup, whereClauseQtQtyMsc, whereClauseQuoteHedMsc, whereClauseQuoteHedTax, whereClauseHedTaxSum, whereClausePartSubs, whereClauseTaxConnectStatus, whereClauseWhatIfScheduling, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteHed=" + whereClauseQuoteHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteHedAttch=" + whereClauseQuoteHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQSalesRP=" + whereClauseQSalesRP
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteCnt=" + whereClauseQuoteCnt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteCom=" + whereClauseQuoteCom
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteDtl=" + whereClauseQuoteDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteDtlAttch=" + whereClauseQuoteDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteCoPart=" + whereClauseQuoteCoPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteDtlAttrValueSet=" + whereClauseQuoteDtlAttrValueSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteDtlTax=" + whereClauseQuoteDtlTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteMsc=" + whereClauseQuoteMsc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteQty=" + whereClauseQuoteQty
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQtmmkup=" + whereClauseQtmmkup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQtQtyMsc=" + whereClauseQtQtyMsc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteHedMsc=" + whereClauseQuoteHedMsc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuoteHedTax=" + whereClauseQuoteHedTax
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHedTaxSum=" + whereClauseHedTaxSum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartSubs=" + whereClausePartSubs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxConnectStatus=" + whereClauseTaxConnectStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhatIfScheduling=" + whereClauseWhatIfScheduling
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(quoteNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "quoteNum=" + quoteNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofBTCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofBTCustID
   Description: This method returns the Bill To customer info.
   OperationID: OnChangeofBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofEngineered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofEngineered
   Description: This method Check the number of reference designators are equal to
the Required Ref Designators defined on JobMtl
   OperationID: OnChangeofEngineered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIncotermCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIncotermCode
   Description: This method checks incoterm
   OperationID: OnChangeIncotermCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIncotermCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIncotermCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofLineExemptTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofLineExemptTax
   Description: This method should be called when the user populates line Tax Exempt field previously being blank
record is changed.
   OperationID: OnChangeofLineExemptTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofLineExemptTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofLineExemptTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenCloseQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenCloseQuote
   Description: This method either opens or closes a Quote and returns the updated object
   OperationID: OpenCloseQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCloseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCloseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreOpenCloseQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreOpenCloseQuote
   Description: This method is to be run befor the OpenCloseQuote method so that any questions
that need to be asked before the OpenCloseQuote method can run can be asked
   OperationID: PreOpenCloseQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreOpenCloseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreOpenCloseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreRefreshQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreRefreshQty
   Description: PreRefreshQty
   OperationID: PreRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSOCreate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSOCreate
   Description: Executes validations before Sales Oreder is created:
Process all lines if Job Type is PRJ and Invoicing method is CS or MB then ask user
   OperationID: PreSOCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSOCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSOCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsCreditMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsCreditMemo
   Description: Check if a credit memo exists for a credit line
Used to validate if changing return type is allowed
   OperationID: ExistsCreditMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsCreditMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsCreditMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToCalc
   Description: Logic to calculate taxes.
Notes: Taxes are not recalculated if "Ready to Process" flag is turned off.
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuotePartNumHasSubstitutes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuotePartNumHasSubstitutes
   Description: This method detrmines if a partNum has any Substitutes defined.
   OperationID: QuotePartNumHasSubstitutes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuotePartNumHasSubstitutes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuotePartNumHasSubstitutes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcKitPriceAfterConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcKitPriceAfterConfig
   Description: When configuring a part, the QuoteDtl unit price may change during the configuration
process.  This method is to be called after running product configurator to recalculate
the kit pricing.
   OperationID: RecalcKitPriceAfterConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcKitPriceAfterConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcKitPriceAfterConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcKitPricing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcKitPricing
   Description: RecalcKitPricing
   OperationID: RecalcKitPricing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcKitPricing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcKitPricing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalcWorksheet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalcWorksheet
   Description: Each part class can have its own material markup percentage
This method calculates the Material Markup from the Qtmmkup table
   OperationID: RecalcWorksheet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalcWorksheet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalcWorksheet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveKitComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveKitComponents
   Description: To delete the QuoteDtl records created as components for a Parent Sales Kit.
   OperationID: RemoveKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetOrderDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetOrderDefaults
   Description: This method updates Order Defaults.
   OperationID: SetOrderDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetOrderDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrderDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCosts
   Description: Updates Worksheet fields.
   OperationID: UpdateCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls
   Description: This method updates the DiscountPercent, NeedByDate,TaxRegionCode and RequestDate for existing Quote Detail Lines in a Quote
   OperationID: ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateProfits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateProfits
   OperationID: ValidateProfits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateProfits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateProfits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTS(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTS
   OperationID: ValidateOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateTaskSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTaskSet
   Description: Validates the task Set Id.
   OperationID: ValidateTaskSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValReqRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValReqRefDes
   Description: Public method to call ValidateReqRefDes method and check the number of
reference designators are equal to the Required Ref Designators defined on QuoteMtl.
   OperationID: ValReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WhatIfGetDate(epicorHeaders = None):
   """  
   Summary: Invoke method WhatIfGetDate
   OperationID: WhatIfGetDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhatIfGetDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_WhatIfScheduling(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WhatIfScheduling
   OperationID: WhatIfScheduling
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WhatIfScheduling_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhatIfScheduling_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcConvUOMUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcConvUOMUnitPrice
   Description: CalcConvUOMUnitPrice
   OperationID: CalcConvUOMUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcConvUOMUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcConvUOMUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileType
   Description: FileType
   OperationID: FileType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIfCurrentSiteHasExternalMES(epicorHeaders = None):
   """  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetIfRevIsExternalMES(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIfRevIsExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfRevIsExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIfRevIsExternalMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfRevIsExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RequestEngineeringExternalMESValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RequestEngineeringExternalMESValidation
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: RequestEngineeringExternalMESValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestEngineeringExternalMESValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestEngineeringExternalMESValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfConfigured(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfConfigured
   Description: CheckIfConfigured
   OperationID: CheckIfConfigured
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfConfigured_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfConfigured_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteDtlContractID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteDtlContractID
   Description: Validate ContractID is active and approved.
   OperationID: CheckQuoteDtlContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteDtlContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteDtlContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlantConfCtrlUse3rdPartySched(epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantConfCtrlUse3rdPartySched
   Description: Get the Use3rdPartySched field from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlUse3rdPartySched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlUse3rdPartySched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetPlantConfCtrlValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantConfCtrlValues
   Description: Get the Use3rdPartySched and Rate Shopping values from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlantConfCtrlValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxCode
   OperationID: OnChangeTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRateCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRateCode
   OperationID: OnChangeRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfTaxAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfTaxAmt
   Description: This method should be called when the tax amount on the quote tax
record is changed.
   OperationID: OnChangeOfTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfReportableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfReportableAmt
   Description: This method should be called when the tax amount on the quote tax
record is changed.
   OperationID: OnChangeOfReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxableAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxableAmt
   Description: This method should be called when the taxable amount on the invoice tax
record is changed.
   OperationID: OnChangeTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfFixedAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfFixedAmount
   Description: This method should be called when the Fixed amount on the invoice tax
record is changed.
   OperationID: OnChangeOfFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfTaxPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfTaxPercent
   Description: This method should be called when the percentage amount on the quote tax
record is changed.
   OperationID: OnChangeOfTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShippingDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShippingDate
   Description: Validate the date is a working day as set in the Shipping Calendar.
   OperationID: ValidateShippingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShippingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShippingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxRegInPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxRegInPrice
   Description: Retrieve Tax Region and InPrice value from the proposed Ship To and indicated if Quote has created any Tax Record.
   OperationID: GetTaxRegInPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxRegInPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxRegInPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUpdtDtlTaxRgn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUpdtDtlTaxRgn
   Description: Defines if the system supposed to ask the user about Tax Liability change.
   OperationID: GetUpdtDtlTaxRgn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUpdtDtlTaxRgn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUpdtDtlTaxRgn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateECCType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateECCType
   Description: Validates if customer exists, a dealer licence is active and returns a warning message if current customer has a valid ECC type and the proposed one is invalid
   OperationID: ValidateECCType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateECCType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateECCType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearQuoteDtlDealerData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearQuoteDtlDealerData
   Description: Clears dealer information for all quote lines
   OperationID: ClearQuoteDtlDealerData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearQuoteDtlDealerData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearQuoteDtlDealerData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteHedSalesRepCodeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteHedSalesRepCodeChanging
   Description: Updates sales rep information when the quote primary salesperson changes
   OperationID: QuoteHedSalesRepCodeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteHedSalesRepCodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteHedSalesRepCodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteHedCustomerCustIDAfterChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteHedCustomerCustIDAfterChange
   Description: Update customer information after QuoteHed Customer ID has changed
   OperationID: QuoteHedCustomerCustIDAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteHedCustomerCustIDAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteHedCustomerCustIDAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlReadyToQuoteChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlReadyToQuoteChanging
   Description: Called when Quote Detail Ready To Quote is changing
   OperationID: QuoteDtlReadyToQuoteChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlReadyToQuoteChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlReadyToQuoteChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateQuoteDtlUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateQuoteDtlUnitPrice
   Description: This method will recalculate the Unit Price.  This should be called after the expected unit price (doc or base)
or expected price per code changes.
   OperationID: CalculateQuoteDtlUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateQuoteDtlUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateQuoteDtlUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlRefreshPriceListAndQuantities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlRefreshPriceListAndQuantities
   Description: Rrefreshes price list and quantities for a quote line.
Called when PriceListCode, BreakListCode, ProdCode, or OverridePriceList are changed.
   OperationID: QuoteDtlRefreshPriceListAndQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlRefreshPriceListAndQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlRefreshPriceListAndQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscellanousChargeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscellanousChargeType
   Description: Called when a miscellaneous charge type changed.  Sets default values based on the type.
   OperationID: ChangeMiscellanousChargeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscellanousChargeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscellanousChargeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteQtyMaterialMarkupChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteQtyMaterialMarkupChanged
   Description: Performs recalculations when the material markup value is changed.  Markup type indicates if the (M)aterial or (P)rofit markup value is what changed.
   OperationID: QuoteQtyMaterialMarkupChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyMaterialMarkupChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyMaterialMarkupChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteQtyPercentTypeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteQtyPercentTypeChanged
   Description: Performs recalculations when quote quantity percent type changed.
   OperationID: QuoteQtyPercentTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyPercentTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyPercentTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteQtyValidateAndRecalcWorksheet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteQtyValidateAndRecalcWorksheet
   Description: Validates and performs a worksheet recalculation when a field affecting worksheet values is changed.
   OperationID: QuoteQtyValidateAndRecalcWorksheet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteQtyValidateAndRecalcWorksheet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteQtyValidateAndRecalcWorksheet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxBaseTaxAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxBaseTaxAmtChange
   Description: This method should be called when the base tax amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseTaxAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseTaxAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseTaxAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxDocTaxAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxDocTaxAmtChange
   Description: This method should be called when the doc tax amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocTaxAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocTaxAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocTaxAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxBaseTaxableAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxBaseTaxableAmtChange
   Description: This method should be called when the base taxable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseTaxableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseTaxableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseTaxableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxDocTaxableAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxDocTaxableAmtChange
   Description: This method should be called when the doc taxable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocTaxableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocTaxableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocTaxableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxBaseReportableAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxBaseReportableAmtChange
   Description: This method should be called when the base reportable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseReportableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseReportableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseReportableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxDocReportableAmtChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxDocReportableAmtChange
   Description: This method should be called when the doc reportable amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocReportableAmtChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocReportableAmtChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocReportableAmtChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxBaseFixedAmountChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxBaseFixedAmountChange
   Description: This method should be called when the base fixed amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxBaseFixedAmountChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxBaseFixedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxBaseFixedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlTaxDocFixedAmountChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlTaxDocFixedAmountChange
   Description: This method should be called when the doc fixed amount on the QuoteDtlTax
   OperationID: QuoteDtlTaxDocFixedAmountChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlTaxDocFixedAmountChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlTaxDocFixedAmountChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlRevisionNumAfterChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlRevisionNumAfterChange
   Description: Additional updates to QuoteDtl after the revision has changed
   OperationID: QuoteDtlRevisionNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlRevisionNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlRevisionNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlPartNumAfterChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlPartNumAfterChange
   Description: Processing after the QuoteDtl XPartNum value has changed
   OperationID: QuoteDtlPartNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlPartNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlPartNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlXPartNumAfterChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteDtlXPartNumAfterChange
   Description: Processing after the QuoteDtl XPartNum value has changed
   OperationID: QuoteDtlXPartNumAfterChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteDtlXPartNumAfterChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteDtlXPartNumAfterChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QSalesRPPrimeRepChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QSalesRPPrimeRepChanging
   Description: Called when the primary sales rep flag on a quote salesperson record is changing.
   OperationID: QSalesRPPrimeRepChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QSalesRPPrimeRepChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QSalesRPPrimeRepChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSOCreate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSOCreate
   Description: Validation prior to creating a sales order from a quote.
   OperationID: ValidateSOCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSOCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSOCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalculateLineDiscounts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalculateLineDiscounts
   Description: Recalculate quote line discounts
   OperationID: RecalculateLineDiscounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalculateLineDiscounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateLineDiscounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateOrderFromQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrderFromQuote
   Description: Create an order from a quote.  This method will handle kit components internally rather than expecting them to be passed in as part of the dataset.
   OperationID: CreateOrderFromQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderFromQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderFromQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateOrderFromQuoteSaveOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrderFromQuoteSaveOTS
   Description: Create an order from a quote and save OTS information.  This method will handle kit components internally rather than expecting them to be passed in as part of the dataset.
   OperationID: CreateOrderFromQuoteSaveOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderFromQuoteSaveOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderFromQuoteSaveOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteHedChangesBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteHedChangesBeforeUpdate
   Description: Checks for specific changes in QuoteHed and returns a prompt asking if these changes should be propagated to the quote lines
   OperationID: CheckQuoteHedChangesBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteHedChangesBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteHedChangesBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PropagateQuoteHedChangesToQuoteDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PropagateQuoteHedChangesToQuoteDtl
   Description: Propagates changes to QuoteHed to QuoteDtl from the field list passed in.
   OperationID: PropagateQuoteHedChangesToQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PropagateQuoteHedChangesToQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PropagateQuoteHedChangesToQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesKitComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesKitComponents
   Description: Gets kit components for a quote line.
   OperationID: GetSalesKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteCntShipToConNumChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteCntShipToConNumChanged
   Description: Validates and returns contact information when the contact ShipToNum or ConNum values are changing
   OperationID: QuoteCntShipToConNumChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCntShipToConNumChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCntShipToConNumChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteCntShipToConNumChangedInactive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteCntShipToConNumChangedInactive
   Description: Validates and returns contact information when the contact ShipToNum or ConNum values are changing
   OperationID: QuoteCntShipToConNumChangedInactive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCntShipToConNumChangedInactive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCntShipToConNumChangedInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConInformation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConInformation
   Description: Call when Quote Contact PerConID is changing.
returnResult:
When 1: Prompt user asking if the person/contact should be added to customer contacts
When 4: Prompt user asking if a new person/contact record should be created
All other values are handled by this api
   OperationID: GetPerConInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConInformation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: One Time Ship To Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQSalesRP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQSalesRP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQSalesRP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQSalesRP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQSalesRP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteCom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteCom
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteCoPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteCoPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteCoPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteCoPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteCoPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteDtlAttrValueSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteDtlAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteDtlTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteDtlTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtlTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtlTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtlTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteMsc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteQty
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQtmmkup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQtmmkup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQtmmkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQtmmkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQtmmkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQtQtyMsc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQtQtyMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQtQtyMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQtQtyMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQtQtyMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteHedMsc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteHedMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteHedTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteHedTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHedTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHedTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHedTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LaunchGlobalAlerts(epicorHeaders = None):
   """  
   Summary: Invoke method LaunchGlobalAlerts
   Description: Method called at service invocation to process Quote logic related to information monitored by Global Alerts - Due Dates and/or Follow Up Dates.
   OperationID: LaunchGlobalAlerts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaunchGlobalAlerts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_MinimumDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MinimumDate
   Description: MinimumDate
   OperationID: MinimumDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MinimumDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MinimumDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Calc_QuoteDtlDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Calc_QuoteDtlDiscount
   Description: Calc_QuoteDtlDiscount
   OperationID: Calc_QuoteDtlDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Calc_QuoteDtlDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Calc_QuoteDtlDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllowUndoReadyToQuote(epicorHeaders = None):
   """  
   Summary: Invoke method AllowUndoReadyToQuote
   Description: This method exists soley for the purpose of allowing security for
unchecking the Ready To Quote flag to be defined
   OperationID: AllowUndoReadyToQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUndoReadyToQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ApplyOrderBasedDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApplyOrderBasedDiscount
   Description: This method applys the OrderBased Discount logic
   OperationID: ApplyOrderBasedDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApplyOrderBasedDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApplyOrderBasedDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDiscountAmountOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDiscountAmountOverride
   OperationID: SetDiscountAmountOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDiscountAmountOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDiscountAmountOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateQuantityUOMQuoteDtlAttribute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateQuantityUOMQuoteDtlAttribute
   OperationID: ValidateQuantityUOMQuoteDtlAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQuantityUOMQuoteDtlAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQuantityUOMQuoteDtlAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignQuoteDtlAttributeDispValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignQuoteDtlAttributeDispValues
   OperationID: AssignQuoteDtlAttributeDispValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignQuoteDtlAttributeDispValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignQuoteDtlAttributeDispValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignAttrSellingExpectedUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignAttrSellingExpectedUM
   Description: Assign QuoteDtlAttrValueSet SellingExpectedUM
   OperationID: AssignAttrSellingExpectedUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignAttrSellingExpectedUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAttrSellingExpectedUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttrQuantityToOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttrQuantityToOrder
   Description: Call this method when the value QuoteDtlAttrValueSet QuantityToOrder changes.
   OperationID: OnChangeAttrQuantityToOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttrQuantityToOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrQuantityToOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNumberOfPieces
   Description: Call this method when the Number Of Pieces changes to calculate a new quantity to order
   OperationID: OnChangeNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsPartPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsPartPriceList
   OperationID: ExistsPartPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsPartPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPartPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsProductGroupPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsProductGroupPriceList
   OperationID: ExistsProductGroupPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProductGroupPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProductGroupPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsProductGroupDiscPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsProductGroupDiscPriceList
   OperationID: ExistsProductGroupDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProductGroupDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProductGroupDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsPartDiscPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsPartDiscPriceList
   OperationID: ExistsPartDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsPartDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPartDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcMaterialMarkup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcMaterialMarkup
   Description: Each part class can have its own material markup percentage
This method calculates the Material Markup from the Qtmmkup table
   OperationID: CalcMaterialMarkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcMaterialMarkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcMaterialMarkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDiscBreakListCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDiscBreakListCode
   Description: Change the DiscBreakListCode
   OperationID: ChangeDiscBreakListCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDiscBreakListCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscBreakListCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMFCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMFCustID
   Description: Method to call when changing the Mark For Customer ID on the QuoteDtl record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMFShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMFShipToNum
   Description: Update QuoteDtl information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeMFShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMFShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMFShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUseOTMF(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUseOTMF
   Description: Method to call when changing the UseOTMF field the QuoteDtl record.
Refreshes the address list and contact info
   OperationID: ChangeUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDocOrderUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDocOrderUnitPrice
   Description: Perform the required updates when DocOrderUnitPrice changes.
   OperationID: ChangeDocOrderUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDocOrderUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDocOrderUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlReturnLineType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlReturnLineType
   Description: Method to call when changing the ReturnLineType on the QuoteDtl record.
Clears Warranty column if ReturnLineType is being changed to 'S'.
   OperationID: ChangeDtlReturnLineType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlReturnLineType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlReturnLineType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlContractNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlContractNum
   Description: Method to call when changing the ContractNum field in the Quote Line record.
Updates the QuoteDtl with values based on the new ContractNum.
   OperationID: ChangeDtlContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlRenewalNbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlRenewalNbr
   Description: Method to call when changing the RenewalNbr field in the Quote Line record.
Updates the QuoteDtl with values based on the new RenewalNbr.
   OperationID: ChangeDtlRenewalNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlRenewalNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlRenewalNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeKitPricing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeKitPricing
   Description: Recalculates the parent line's unit price when the kit pricing is set to "P", if the kit pricing is set to "C"
the price will be calculated on the AfterUpdate procedure.
   OperationID: ChangeKitPricing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeKitPricing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeKitPricing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeKitQtyPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeKitQtyPer
   Description: Used to recalculate the OrderQty of the component kit line using the parent's OrderQuantity
   OperationID: ChangeKitQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeKitQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeKitQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeManualTaxCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeManualTaxCalc
   OperationID: ChangeManualTaxCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeManualTaxCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeManualTaxCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscPercent
   Description: This method recalculates Misc Charges Amounts when Percentage was changed.
   OperationID: ChangeMiscPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscAmt
   Description: This method recalculates Misc Charges Amounts when Amount was changed.
   OperationID: ChangeMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMSRP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMSRP
   Description: This method recalculates MSRP when MSRP was changed.
   OperationID: ChangeMSRP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMSRP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMSRP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePromotionalPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePromotionalPrice
   Description: This method recalculates PromotionalPrice when PromotionalPrice was changed.
   OperationID: ChangePromotionalPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePromotionalPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePromotionalPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderQty
   Description: Gets the proposed OrderQty and if the current OrderDtl record is a sales kit then it recalculates
the order qty of each component based on the proposed OrderQty amount
   OperationID: ChangeOrderQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOverrideDiscPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOverrideDiscPriceList
   Description: Rerun the price break calculation if the override price list flag is changed from
true to false.
   OperationID: ChangeOverrideDiscPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOverrideDiscPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOverrideDiscPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationChangePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationChangePart
   Description: Update Quote Detail, Want to load PriceList Qty breaks and set new unit proce on those,
information when the Part Number is changed by Configuration Part Creation.
   OperationID: ConfigurationChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationRefreshQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationRefreshQty
   Description: Update PriceList Qty breaks and set new unit price on those
when the Part Number is changed by Document Rule.
   OperationID: ConfigurationRefreshQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationRefreshQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationRefreshQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationChangeUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfigurationChangeUnitPrice
   Description: Update Price fields when the UnitPrice or DocUnitPRice is changed by a Document Rule.
   OperationID: ConfigurationChangeUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfigurationChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfigurationChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateKBMaxConfigurator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateKBMaxConfigurator
   Description: Update the CPQ Configurator on the given Quote Line.
   OperationID: UpdateKBMaxConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateKBMaxConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateKBMaxConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetKBMaxConfigProdID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetKBMaxConfigProdID
   Description: Set the CPQ Quote Product ID on the Quote Line.
This will trigger the loading of the method from CPQ onto the Quote Assembly.
   OperationID: SetKBMaxConfigProdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetKBMaxConfigProdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetKBMaxConfigProdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PopulateCallContext(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PopulateCallContext
   Description: Allows for assigning of a generic CallContext for integrations.
   OperationID: PopulateCallContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateCallContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateCallContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartRev
   Description: Update Quote Detail information when the Part Revision is changed.
   OperationID: ChangePartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNumMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNumMaster
   Description: Perform all validations associated with the Change of the PartNum field.  This method consolidates all the seperate methods that were being
called when a partNum changes.  a flag for 'suppressUserPrompts' allows the user to suppress returning to the client for user input.  This
may be useful for webservices etc.  The following 3 bools are used to determine which validations should be run (getPartXRefInfo,
checkPartRevisionChange, and checkChangeKitParent).  From the UI, these are originally defaulted to true but if control is returned to the
UI from this method, the UI changes the setting of these fields when it calls it a subsequent time to only run the necessary code.  From
webservices, this allows more control over which validations are run.
   OperationID: ChangePartNumMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNumMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNumMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteCntCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteCntCustID
   Description: This method takes in a proposed CustID, and if valid, updates the customer-
related fields on the QuoteCnt.
   OperationID: ChangeQuoteCntCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteCntCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteCntCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteCoPartPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteCoPartPartNum
   Description: This method validates the QuoteCoPart.CoPartNum and defaults fields associated with the partnum.
This method should run when the QuoteCoPart.CoPartNum field changes.
   OperationID: ChangeQuoteCoPartPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteCoPartPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteCoPartPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteHedOTSCountryNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteHedOTSCountryNum
   Description: Method to call when changing the QuoteHed.OTSCountryNum field.
Update Tax Region Code
   OperationID: ChangeQuoteHedOTSCountryNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteHedOTSCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteHedOTSCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteHedUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteHedUseOTS
   Description: Method to call when changing the UseOTS field.
Refreshes the address list
   OperationID: ChangeQuoteHedUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteHedUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteHedUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSellingExpQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSellingExpQty
   OperationID: ChangeSellingExpQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSellingExpQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingExpQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToCustID
   Description: Update Ship To Information when Ship To is changed
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStandardPct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStandardPct
   Description: This method updates the QuoteQty markup percents and the Qtmmkup table using
the specified markup record
   OperationID: ChangeStandardPct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStandardPct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStandardPct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxRegionCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxRegionCode
   Description: Used to validate change of TaxRegionCode
   OperationID: ChangeTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProdCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProdCode
   Description: This method assigns Tax Category when changing ProdCode
   OperationID: ChangeProdCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProdCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBOMErrors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBOMErrors
   Description: This method runs through a quote's BOM and returns a list of assembly and/or
materials that are on hold or inactive.  Quote Line cannot be engineered or QuoteHed
cannot be Quoted until these errors are taken care of
   OperationID: CheckBOMErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBOMErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBOMErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCustomerCreditLimit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCustomerCreditLimit
   Description: The method returns a character string if the customer will go over their credit limit
and the user is given the choice of continuing or not.
   OperationID: CheckCustomerCreditLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCustomerCreditLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCustomerCreditLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPhaseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPhaseID
   Description: The method review if phaseid is availble in ProjPhase Table
   OperationID: CheckPhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPreCustPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPreCustPartInfo
   Description: The method is to be run on leave of the CustPartNum field
before the GetCustPartInfo or Update methods are run.
In case existance of CustomerPart it returns Part Number
which belongs this CustomerPart.
   OperationID: CheckPreCustPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreCustPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreCustPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: The method is to be run on leave of the PartNum, Revision and CustPartNum fields
before the GetCustPartInfo or Update methods are run.  This returns all the questions
that need to be asked before a part can be changed.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPreQuoteCoPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPreQuoteCoPartInfo
   Description: This method validates the QuoteCoPart.CoPartNum is not serial tracked or a configured part.
   OperationID: CheckPreQuoteCoPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreQuoteCoPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreQuoteCoPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckProjectID
   Description: The method review if projectid is availble in Project Table
   OperationID: CheckProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteNum
   Description: This method will check if the quote number entered is valid.  If the quote number
that's entered doesn't already exist and the number entered is greater than the number defined
as the starting quote number in company maintenance, then the quote number is invalid.
   OperationID: CheckQuoteNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckQuoteSecurity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckQuoteSecurity
   OperationID: CheckQuoteSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckQuoteSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckQuoteSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRateGrpCode
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CollapsePhantom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CollapsePhantom
   Description: Collapses any single Quote Assembly except Assembly 0.
   OperationID: CollapsePhantom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollapsePhantom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollapsePhantom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLines
   Description: This method copies lines from other Quotes to the current Quote
   OperationID: CopyLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_prjWBSPhaseDefinitionIsAllowed(epicorHeaders = None):
   """  
   Summary: Invoke method prjWBSPhaseDefinitionIsAllowed
   OperationID: prjWBSPhaseDefinitionIsAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/prjWBSPhaseDefinitionIsAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetExternalCRMIntegrationIsEnabled(epicorHeaders = None):
   """  
   Summary: Invoke method GetExternalCRMIntegrationIsEnabled
   OperationID: GetExternalCRMIntegrationIsEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExternalCRMIntegrationIsEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CreateOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrder
   Description: This method takes the specified QuoteDtl lines and creates a Sales Order
   OperationID: CreateOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateOrderSaveOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrderSaveOTS
   Description: This method takes the specified QuoteDtl lines and creates a Sales Order
after saving the One Time Ship To as Customer.
   OperationID: CreateOrderSaveOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderSaveOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderSaveOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuoteCntNoCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuoteCntNoCustCnt
   Description: Create Quote Contact but no creating Customer Contact
   OperationID: CreateQuoteCntNoCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteCntNoCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteCntNoCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuoteDtlComplements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuoteDtlComplements
   Description: Create new lines for every complement selected for a given Line,
   OperationID: CreateQuoteDtlComplements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteDtlComplements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteDtlComplements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_QuoteCreditAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method QuoteCreditAdd
   Description: This method takes the Quote and 'C'redit ReturnLineType quoteLines that were selected
and creates a CreditMemo type invoice and invoice lines.
   OperationID: QuoteCreditAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/QuoteCreditAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/QuoteCreditAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultOrderFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultOrderFields
   Description: This method takes the Quote and initializes the fields used during CreateOrder.
The user will then update the Quote dataset and then call the CreateOrder method
to actually create the order.
   OperationID: DefaultOrderFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultOrderFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultOrderFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSpecificPartRevIsApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSpecificPartRevIsApproved
   Description: Checks if the Revision specified is Approved
   OperationID: CheckSpecificPartRevIsApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSpecificPartRevIsApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSpecificPartRevIsApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateQuote
   Description: This method creates a new Quote from an existing quote
   OperationID: DuplicateQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCValidateAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCAfterAddressValidationOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCAfterAddressValidationOTS
   Description: After the tax integration has been called, update the Quote on one time shipment address if it
was changed.
   OperationID: ETCAfterAddressValidationOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCAfterAddressValidationOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddressValidationOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportQuoteToEST(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportQuoteToEST
   Description: ExportQuoteToEST
   OperationID: ExportQuoteToEST
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportQuoteToEST_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportQuoteToEST_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompetitorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCompetitorInfo
   Description: This method returns default information for the competitor.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetCompetitorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompetitorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompetitorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContactInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContactInfo
   Description: This method returns default information for the Contact.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetContactInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContactInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContactInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistContact
   Description: This method returns exist contact shipto  Method must use parameters instead of the dataset
   OperationID: ExistContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistShipTo
   Description: This method checks if Ship To is exist
   OperationID: ExistShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustCntInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustCntInfo
   Description: This method returns default information for the Contact.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
   OperationID: GetCustCntInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustCntInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustCntInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCustomerInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomerInfo
   Description: This method returns default information for the Customer.
   OperationID: GetCustomerInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustPartInfo
   Description: Defaults Part Information when the Customer Part Number changes
MUST RUN UPDATE AFTER THIS METHOD
   OperationID: GetCustPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlUnitPriceInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlUnitPriceInfo
   Description: This method calls InternalGetDtlUnitPriceInfo.  Need to split this out so configurator
could update the price when part changes from part creation
   OperationID: GetDtlUnitPriceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlUnitPriceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlUnitPriceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDtlUnitPriceInfo_User(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDtlUnitPriceInfo_User
   Description: This method updates the QuoteDtl unit price and revenue fields when the
SellingExpextedQty is changed by the user
   OperationID: GetDtlUnitPriceInfo_User
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDtlUnitPriceInfo_User_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDtlUnitPriceInfo_User_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExchangeRate
   Description: This method returns the Exchange Rate information for the selected Currency.  The system
may not have an exchange rate between the Quote and Base so it may use an middle Currency
so that it will go Quote Currency -> Ref Currency -> Base Currency
   OperationID: GetExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetKitComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetKitComponents
   Description: Calls GetKitComponents from SalesKitting.p, which creates a list of QuoteDtl records
that will be treated as kit components of the given QuoteLine.
   OperationID: GetKitComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetKitComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKitComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: This overload of GetList adds Quotes which ShipTo's fall within authorized territories.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Invokes GetRows filtering on quotes with the authorized territories
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForAuthorizedTerritories(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForAuthorizedTerritories
   Description: This overload of GetList adds Quotes which ShipTo's fall within authorized territories.
   OperationID: GetListForAuthorizedTerritories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForAuthorizedTerritories_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForAuthorizedTerritories_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the Quote records which will be a subset
of the QuoteHEd records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMaterialMarkup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMaterialMarkup
   Description: This procedure is used to be called from EQR10.p to get the MaterialMarkupP
and MaterialMarkupM fields since these two fields are external and they're needed
to be displayed on the report.
   OperationID: GetMaterialMarkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMaterialMarkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaterialMarkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMiscChrgDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMiscChrgDefaults
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field
as well as QuoteMsc and QtQtyMsc can the same code
   OperationID: GetMiscChrgDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMiscChrgDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMiscChrgDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMktgInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMktgInfo
   Description: This method updates the description fields for the Marketing Campaign and Event fields
   OperationID: GetMktgInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMktgInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMktgInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContractQuoteDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContractQuoteDtl
   Description: Method to call when adding a new QuoteDtl record for a Service Contract or a Renewal
   OperationID: GetNewContractQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContractQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesKit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesKit
   Description: GetNewSalesKit
   OperationID: GetNewSalesKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesKit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConInfo
   Description: This method returns default information for the QuoteCnt From Persons contact.
   OperationID: GetPerConInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPhantomComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPhantomComponents
   Description: GetPhantomComponents
   OperationID: GetPhantomComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPhantomComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPhantomComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceListInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceListInfo
   Description: Finds the default pricelist if override field is blank
updates the QuoteDtl record with the new pricebreak information
called when OverridePriceList, BreakListCode or ProdCode fields change
   OperationID: GetPriceListInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceListInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDiscountPriceListInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDiscountPriceListInfo
   Description: Finds the default Discount Price List if override field is blank
updates the QuoteDtl record with the new Discount break information
called when OverrideDiscPriceList, DiscBreakListCode or ProdCode fields change
   OperationID: GetDiscountPriceListInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDiscountPriceListInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDiscountPriceListInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQtyPriceInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQtyPriceInfo
   Description: This method updates the unitprice information when the QuoteQty SellingQty has changed
   OperationID: GetQtyPriceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyPriceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyPriceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQtyPriceInfoCfgPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQtyPriceInfoCfgPart
   Description: This method updates the unitprice information when the QuoteQty SellingQty has changed
   OperationID: GetQtyPriceInfoCfgPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyPriceInfoCfgPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyPriceInfoCfgPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQtyToOrdPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQtyToOrdPrice
   Description: This method takes the QuantityToOrder field and returns the base and doc unit price
   OperationID: GetQtyToOrdPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyToOrdPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyToOrdPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuotedInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuotedInfo
   Description: Updates the DateQuoted,ExpirationDate and FollowUpDate fields based on the Quoted field
   OperationID: GetQuotedInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuotedInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuotedInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteRelationshipMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteRelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for Quote
   OperationID: GetQuoteRelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteRelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteRelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReasonInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReasonInfo
   Description: This method returns default reason code for the specified ReasonType. Run when
the reasonType field has changed.
   OperationID: GetReasonInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReasonInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReasonInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuotesForCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuotesForCustomer
   Description: Returns quotes for a customer.
   OperationID: GetQuotesForCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuotesForCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuotesForCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForCashReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForCashReceipt
   Description: Invokes GetRows filtering on quotes for the specified Cash Receipt
   OperationID: GetRowsForCashReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForCashReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForCashReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForInvoice
   Description: Invokes GetRows filtering on quotes for the specified Invoice
   OperationID: GetRowsForInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForSalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForSalesOrder
   Description: Invokes GetRows filtering on quotes for the specified Sales Order
   OperationID: GetRowsForSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForShipment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForShipment
   Description: Invokes GetRows filtering on quotes for the specified Customer Shipment
   OperationID: GetRowsForShipment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the Quote records which will be a subset
of the QuoteHEd records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesRepInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesRepInfo
   Description: This method returns default commision information when the SalesRepCode or RoleCode
field(s) change.  Method must use parameters instead of the dataset due to the problem
changing the primary key field
   OperationID: GetSalesRepInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesRepInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesRepInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipToInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipToInfo
   Description: This method updates the ShipTo information when the ShipToNum field changes
   OperationID: GetShipToInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSmartString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSmartString
   Description: Generates the SmartString for kit component configured part
   OperationID: GetSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaskSetInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaskSetInfo
   Description: This method updates the QuoteHed.Stage field when the TaskSetId is changed
   OperationID: GetTaskSetInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaskSetInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaskSetInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CompanyTaxConnectStatus(epicorHeaders = None):
   """  
   Summary: Invoke method CompanyTaxConnectStatus
   Description: Returns the current status of Tax Connect on Company Configuration.
   OperationID: CompanyTaxConnectStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTerrInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTerrInfo
   Description: This method returns the TaskSetId when the territory ID changes
   OperationID: GetTerrInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTerrInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTerrInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWSUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWSUnitPrice
   Description: This method updates the Base and Doc Unit Prices when the Quoted Unit Price
or Price Per Code changes on the Quote Worksheet form
   OperationID: GetWSUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWSUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWSUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KitCompPartCreate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KitCompPartCreate
   Description: Configured kit component part creation
   OperationID: KitCompPartCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KitCompPartCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KitCompPartCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMktgCamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMktgCamp
   Description: Call this method when the value of MktgCamp changes.
   OperationID: OnChangeMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMktgEvnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMktgEvnt
   Description: Call this method when the value of MktgCamp changes.
   OperationID: OnChangeMktgEvnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgEvnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgEvnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HedTaxSumRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HedTaxSumRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSubsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QSalesRPRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QSalesRPRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtQtyMscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QtQtyMscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QtmmkupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QtmmkupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteCntRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteCoPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteCoPartRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteComRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteComRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlAttrValueSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlAttrValueSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedMscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedMscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedTaxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteMscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteMscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteQtyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteQtyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxConnectStatusRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxConnectStatusRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhatIfSchedulingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhatIfSchedulingRow] = obj["value"]
      pass

class Erp_Tablesets_HedTaxSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency display switch  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  Document reportable amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Document taxable amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document tax amount.  """  
      self.HedNum:int = obj["HedNum"]
      """  Order or Quote number this tax summary relates to.  """  
      self.Percent:int = obj["Percent"]
      """  Tax percent  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  Reportable amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax amount  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax code  """  
      self.TaxDescription:str = obj["TaxDescription"]
      """  Sales Tax description  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.RateCode:str = obj["RateCode"]
      """  Rate Code on the Header Tax Summary  """  
      self.AllocDepInvcNum:int = obj["AllocDepInvcNum"]
      """  Invoice Number of allocated Deposits  """  
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      """  Rate Code Description on the Header Tax Summary  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
      self.SugOrderQty:int = obj["SugOrderQty"]
      """  Suggested Quantity for Order Qty in Quote Detail  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      self.SubPartIUM:str = obj["SubPartIUM"]
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QSalesRPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote that this record is linked to.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  Identifies the Sales Rep linked to the Quote.  """  
      self.Name:str = obj["Name"]
      """  The Sales Reps Name from the SalesRep table  """  
      self.PrimeRep:bool = obj["PrimeRep"]
      """  Identifies the primary sales rep on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  """  
      self.RepRate:int = obj["RepRate"]
      """  Establishes the defaults sales rep commission rates. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepSplit:int = obj["RepSplit"]
      """  Split percent is used to calculate the "commissionable"  dollar  amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Link to the RoleCD Table where Roles are defined.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OfficePhone:str = obj["OfficePhone"]
      self.HomePhone:str = obj["HomePhone"]
      self.ReportsTo:str = obj["ReportsTo"]
      self.EmailAddress:str = obj["EmailAddress"]
      self.Fax:str = obj["Fax"]
      self.MobilePhone:str = obj["MobilePhone"]
      self.SalesRepTitle:str = obj["SalesRepTitle"]
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.SalesRepCodePerConID:int = obj["SalesRepCodePerConID"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QtQtyMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHead  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  CurrencyCode.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscChrgDescription:str = obj["MiscChrgDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QtmmkupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteHead.QuoteNum that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteDtl.QuoteLine to which the markup is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  the specific QuoteQty record that this markup is related to.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Descriptive Code assigned by the user to uniquely identify the Part Class master record. This is the unique identifier for Qtmmkup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Material cost Markup Percent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Used:bool = obj["Used"]
      """  Indicates if Markup is used by QuoteMtl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassCodeInactive:bool = obj["ClassCodeInactive"]
      self.ClassCodeDescription:str = obj["ClassCodeDescription"]
      self.QtyNumMiscCostDesc:str = obj["QtyNumMiscCostDesc"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number. This Quote Contact is linked to this QuoteHed  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Name of contact.  """  
      self.PrimeContact:bool = obj["PrimeContact"]
      """  Primary contact for this quote.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PerConID:int = obj["PerConID"]
      """  PerConID  """  
      self.Func:str = obj["Func"]
      """  CustCnt.Func  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  CustCnt.PhoneNum  """  
      self.Fax:str = obj["Fax"]
      """  CustCnt.Fax  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  CustCnt.EmailAddress  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumMiddleName:str = obj["ConNumMiddleName"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumFirstName:str = obj["ConNumFirstName"]
      self.ConNumLastName:str = obj["ConNumLastName"]
      self.ConNumCorpName:str = obj["ConNumCorpName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCoPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.CoPartNum:str = obj["CoPartNum"]
      """  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  """  
      self.CoRevisionNum:str = obj["CoRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  If true, MRP will not generate change suggestions for the co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartMasterPart:bool = obj["PartMasterPart"]
      self.EnablePreventSugg:bool = obj["EnablePreventSugg"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteComRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote that this QuoteCom is related to.  """  
      self.CompNum:int = obj["CompNum"]
      """  The unique key for the CRMComp Master table.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.PrimeComp:bool = obj["PrimeComp"]
      """  Identifies the primary Competitor on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  CRMComp  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  CRMCall.PhoneNum  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  CRMCall.EmailAddress  """  
      self.CompURL:str = obj["CompURL"]
      """  CRMCall.CompURL  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line attribute set record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote number to which this line attribute set record is associated with.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure).  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure).  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispNumberOfPiecesUOM:str = obj["DispNumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.RFQCurrBaseEst:str = obj["RFQCurrBaseEst"]
      """  RFQCurrBaseEst  """  
      self.RFQTemplate:str = obj["RFQTemplate"]
      """  RFQTemplate  """  
      self.CreateEstimate:bool = obj["CreateEstimate"]
      """  CreateEstimate  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECC Quote Line  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Ref  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  Indicates if no tax recalculation by the system is supposed to be done.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.ExternalCRMQuoteLineID:str = obj["ExternalCRMQuoteLineID"]
      """  This field holds the id of this quote line in the External CRM  """  
      self.ReturnLineType:str = obj["ReturnLineType"]
      """  Type for returns: Blank, (C)redit or (S)tandard  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  Mark For ShipToNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Contact Name  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.BasePotential:int = obj["BasePotential"]
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.DocPotential:int = obj["DocPotential"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.HasCreditMemo:bool = obj["HasCreditMemo"]
      """  Indicates if this Quote line has an associated credit memo (only for dealer portal)  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.LineStatus:str = obj["LineStatus"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  """  
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Selected:bool = obj["Selected"]
      """  Selected row  """  
      self.ShipByDate:str = obj["ShipByDate"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalQuote:int = obj["TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.UpdateReq:bool = obj["UpdateReq"]
      """   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Indicates that the Quote should be used as the BOM when creating a job for the linked order  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.ECCLineCRQ:int = obj["ECCLineCRQ"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the Dynamic Attributes button on a Quote Line  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.MarkForAddressFormatted:str = obj["MarkForAddressFormatted"]
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in Doc currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      """   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.QuoteNumInPrice:bool = obj["QuoteNumInPrice"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line related to the Tax Record  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an quote. When the sales tax field EcAquisition is checked then 2 quote tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this quote. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the tax.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the tax converted to the customers currency.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description for CurrentStage field  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill to customer id.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CustomerName:str = obj["CustomerName"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHedMsc  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the overall Quote. These will be printed on the Quote form.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """  Optional check off # 2.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """  Optional check off # 3.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional check off # 4.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional check off # 5.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.FlwAlrtSnt:bool = obj["FlwAlrtSnt"]
      """  System maintained flag - set to yes when the quote follow up alert has been sent.  """  
      self.DueAlrtSnt:bool = obj["DueAlrtSnt"]
      """  System maintained flag - set to yes when the quote due date alert has been sent.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LeadRating:str = obj["LeadRating"]
      """  A = High, Z = Low  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.ParentQuoteNum:int = obj["ParentQuoteNum"]
      """  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ExpectedClose:str = obj["ExpectedClose"]
      """  The date this quote is expected to close.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.QuoteClosed:bool = obj["QuoteClosed"]
      """  This quote is no longer updatable.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The date that the Quote was closed.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the quote.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.LockRate:bool = obj["LockRate"]
      """  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.QuoteAmt:int = obj["QuoteAmt"]
      """  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  """  
      self.DocQuoteAmt:int = obj["DocQuoteAmt"]
      """  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1QuoteAmt:int = obj["Rpt1QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2QuoteAmt:int = obj["Rpt2QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3QuoteAmt:int = obj["Rpt3QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready.  """  
      self.EDIQuote:bool = obj["EDIQuote"]
      """  Quote created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module this type of document is created.  """  
      self.OutboundQuoteDocCtr:int = obj["OutboundQuoteDocCtr"]
      """  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote header is linked to an inter-company PO header.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.VoidQuote:bool = obj["VoidQuote"]
      """  Indicates that the Quote item was closed before any shipments were made against it.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.TotalDiscPct:int = obj["TotalDiscPct"]
      """  Total discount percent.  """  
      self.TotalExpected:int = obj["TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.TotalGrossValue:int = obj["TotalGrossValue"]
      self.TotalMiscAmt:int = obj["TotalMiscAmt"]
      self.TotalPotential:int = obj["TotalPotential"]
      self.TotalWorstCs:int = obj["TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.DocTotalBestCs:int = obj["DocTotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      self.DocTotalDiscPct:int = obj["DocTotalDiscPct"]
      """  Total discount percent.  """  
      self.DocTotalExpected:int = obj["DocTotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.DocTotalGrossValue:int = obj["DocTotalGrossValue"]
      self.DocTotalMiscAmt:int = obj["DocTotalMiscAmt"]
      self.DocTotalPotential:int = obj["DocTotalPotential"]
      self.DocTotalWorstCs:int = obj["DocTotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt1TotalBestCs:int = obj["Rpt1TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      self.Rpt1TotalDiscPct:int = obj["Rpt1TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt1TotalExpected:int = obj["Rpt1TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt1TotalGrossValue:int = obj["Rpt1TotalGrossValue"]
      self.Rpt1TotalMiscAmt:int = obj["Rpt1TotalMiscAmt"]
      self.Rpt1TotalPotential:int = obj["Rpt1TotalPotential"]
      self.Rpt1TotalWorstCs:int = obj["Rpt1TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt2TotalBestCs:int = obj["Rpt2TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      self.Rpt2TotalDiscPct:int = obj["Rpt2TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt2TotalExpected:int = obj["Rpt2TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt2TotalGrossValue:int = obj["Rpt2TotalGrossValue"]
      self.Rpt2TotalMiscAmt:int = obj["Rpt2TotalMiscAmt"]
      self.Rpt2TotalPotential:int = obj["Rpt2TotalPotential"]
      self.Rpt2TotalWorstCs:int = obj["Rpt2TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt3TotalBestCs:int = obj["Rpt3TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      self.Rpt3TotalDiscPct:int = obj["Rpt3TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt3TotalExpected:int = obj["Rpt3TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt3TotalGrossValue:int = obj["Rpt3TotalGrossValue"]
      self.Rpt3TotalMiscAmt:int = obj["Rpt3TotalMiscAmt"]
      self.Rpt3TotalPotential:int = obj["Rpt3TotalPotential"]
      self.Rpt3TotalWorstCs:int = obj["Rpt3TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.TotalBestCs:int = obj["TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.LOQPrepressText:str = obj["LOQPrepressText"]
      """  LOQPrepressText  """  
      self.LOQNewPageOnQuoteLine:bool = obj["LOQNewPageOnQuoteLine"]
      """  LOQNewPageOnQuoteLine  """  
      self.LOQBookPCFinishing:bool = obj["LOQBookPCFinishing"]
      """  LOQBookPCFinishing  """  
      self.LOQBookPCPaper:bool = obj["LOQBookPCPaper"]
      """  LOQBookPCPaper  """  
      self.LOQBookPCPress:bool = obj["LOQBookPCPress"]
      """  LOQBookPCPress  """  
      self.LOQBookPCPlates:bool = obj["LOQBookPCPlates"]
      """  LOQBookPCPlates  """  
      self.LOQVariations:bool = obj["LOQVariations"]
      """  LOQVariations  """  
      self.AEPLOQType:str = obj["AEPLOQType"]
      """  AEPLOQType  """  
      self.LOQPrepressStyle:str = obj["LOQPrepressStyle"]
      """  LOQPrepressStyle  """  
      self.QuoteCSR:str = obj["QuoteCSR"]
      """  QuoteCSR  """  
      self.DueHour:str = obj["DueHour"]
      """  DueHour  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCConfirmed:bool = obj["ECCConfirmed"]
      """  Quote was confirmed/rejected by ECC Web  """  
      self.ECCConfirmedBy:str = obj["ECCConfirmedBy"]
      """  Quote was confirmed/rejected by this ECC user  """  
      self.ECCMsgType:str = obj["ECCMsgType"]
      """  ECC quote message: RFQ or GQR  """  
      self.ECCWebReady:bool = obj["ECCWebReady"]
      """  Quote is ready to be approved by user via ECC web site.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Reference Number  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ECCStatus:str = obj["ECCStatus"]
      """  ECC Quote Status  """  
      self.ECCExpirationDate:str = obj["ECCExpirationDate"]
      """  ECC Expiration Date  """  
      self.ECCCmmtRefSK:str = obj["ECCCmmtRefSK"]
      """  ECCCmmtRefSK  """  
      self.ExternalCRMQuote:bool = obj["ExternalCRMQuote"]
      """  This field defines if the Quote  is synchronized to an External CRM.  """  
      self.ExternalCRMQuoteID:str = obj["ExternalCRMQuoteID"]
      """  This field holds the  id of this quote in the External CRM  """  
      self.ExternalCRMOrderID:str = obj["ExternalCRMOrderID"]
      """  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  """  
      self.ECCSalesRepID:str = obj["ECCSalesRepID"]
      """  Web Sales Rep ID  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  HdrTaxNoUpdt  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  """  
      self.TotalClaimsCredit:int = obj["TotalClaimsCredit"]
      """  Total of claims credit lines  """  
      self.DocTotalClaimsCredit:int = obj["DocTotalClaimsCredit"]
      """  Total of claims credit lines in customer currency  """  
      self.Rpt1TotalClaimsCredit:int = obj["Rpt1TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt2TotalClaimsCredit:int = obj["Rpt2TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt3TotalClaimsCredit:int = obj["Rpt3TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.TotalClaimsTax:int = obj["TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes.  """  
      self.DocTotalClaimsTax:int = obj["DocTotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in customer currency.  """  
      self.Rpt1TotalClaimsTax:int = obj["Rpt1TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt2TotalClaimsTax:int = obj["Rpt2TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt3TotalClaimsTax:int = obj["Rpt3TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.TotalClaimsSATax:int = obj["TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes.  """  
      self.DocTotalClaimsSATax:int = obj["DocTotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt1TotalClaimsSATax:int = obj["Rpt1TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt2TotalClaimsSATax:int = obj["Rpt2TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt3TotalClaimsSATax:int = obj["Rpt3TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.TotalClaimsWHTax:int = obj["TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes.  """  
      self.DocTotalClaimsWHTax:int = obj["DocTotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in customer currency.  """  
      self.Rpt1TotalClaimsWHTax:int = obj["Rpt1TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt2TotalClaimsWHTax:int = obj["Rpt2TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt3TotalClaimsWHTax:int = obj["Rpt3TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill To Customer Name.  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  Audit Log change description  """  
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.Conclusion:str = obj["Conclusion"]
      self.ConName:str = obj["ConName"]
      """  Primary Contact Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description of the CurrentStage field  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Value of the Customer.AllowOTS (customer allows one time shipment)  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DaysOpen:int = obj["DaysOpen"]
      """  Number of days Quote has been open  """  
      self.DiscountPercentCalc:int = obj["DiscountPercentCalc"]
      """   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the quote.  """  
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      self.EnableOrderBasedDisc:bool = obj["EnableOrderBasedDisc"]
      """  Indicates if it's okay to enable OrderBased Pricing  """  
      self.ExpectedCsPct:int = obj["ExpectedCsPct"]
      """   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  """  
      self.FaxNum:str = obj["FaxNum"]
      self.FOB:str = obj["FOB"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HasQuoteLines:bool = obj["HasQuoteLines"]
      """  Used by IU to disabled Currency Code  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  EqSyst.LogChanges  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date  """  
      self.OrderDiscount:int = obj["OrderDiscount"]
      self.OrderPONum:str = obj["OrderPONum"]
      self.OrderShipVia:str = obj["OrderShipVia"]
      self.OrderTerms:str = obj["OrderTerms"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PreventQQChange:bool = obj["PreventQQChange"]
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.TotalQuote:int = obj["TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.WorseCsPctCalc:int = obj["WorseCsPctCalc"]
      """   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BestCsPctCalc:int = obj["BestCsPctCalc"]
      """   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID of the bill to customer.  """  
      self.HasCreditLines:bool = obj["HasCreditLines"]
      """  Indicates if the order contains any credit type line  """  
      self.IsValidECC:bool = obj["IsValidECC"]
      """  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  """  
      self.EnableHDCaseNum:bool = obj["EnableHDCaseNum"]
      """  Flag indicating whether to enable CaseNum or not  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  Indicates if the quote can be updated  """  
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Formatted address  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To Address formatted  """  
      self.PromptTaxRegionCode:bool = obj["PromptTaxRegionCode"]
      """  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the quote is inactive.  """  
      self.UpdatePrimContact:bool = obj["UpdatePrimContact"]
      """  Update primary contact on save of the quote header  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskTaskDescription:str = obj["ActiveTaskTaskDescription"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyBaseCurr:bool = obj["CurrencyBaseCurr"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCheckDuplicatePO:bool = obj["CustomerCheckDuplicatePO"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.LastTaskTaskDescription:str = obj["LastTaskTaskDescription"]
      self.MktgCpgnCampDescription:str = obj["MktgCpgnCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ResponseCallTypeDesc:str = obj["ResponseCallTypeDesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaInactive:bool = obj["ShipViaInactive"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.XbSystCalcQuoteTax:bool = obj["XbSystCalcQuoteTax"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax ID from Sales Tax  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code on the Header Tax Summary  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this quote  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount for this quote  """  
      self.Percent:int = obj["Percent"]
      """  Calculated Tax Percent  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this quote  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount for this quote  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ClaimsTax:bool = obj["ClaimsTax"]
      """  Tax for claims credit tax.  This tax should not be included with regular tax.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteHedCurrencyCode:str = obj["QuoteHedCurrencyCode"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteQtyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote # that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  """  
      self.OurQuantity:int = obj["OurQuantity"]
      """  Represents one of the requested Quote Quantities for the line item using QuoteQty.IUM.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Quoted unit price for the given quantity. This value is entered by the user.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed).
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteQty.Quantity by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Material Bur Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Material Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  SubContract Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.MiscCostDesc:str = obj["MiscCostDesc"]
      """  Miscellaneous Cost description.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Miscellaneous Cost amount that will be considered in the unit price calculations.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Miscellaneous Cost Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values. Prices can be calculated either as a straight markup of cost ( Cost + (Cost *  x %)) or a percent of profit ( Cost / (100% -  x%).   PercentType "M" = straight markup, "P" = Profit Percent. Defaulted from referenced QMarkup, from EQSyst.PercentType if not blank, else default as "M".  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure (how it is stocked).  Use the default Part.IUM if its a valid part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Quote Quantities for the line item using QuoteQty.SUM.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Reserved for future use  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reserved for future use  """  
      self.PriceSource:str = obj["PriceSource"]
      """  PriceSource  """  
      self.PricePerAdl1000:int = obj["PricePerAdl1000"]
      """  PricePerAdl1000  """  
      self.TotalSellPrice:int = obj["TotalSellPrice"]
      """  TotalSellPrice  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocPricePerAdl1000:int = obj["DocPricePerAdl1000"]
      """  DocPricePerAdl1000  """  
      self.DocTotalSellPrice:int = obj["DocTotalSellPrice"]
      """  DocTotalSellPrice  """  
      self.UserChangedUnitPrice:bool = obj["UserChangedUnitPrice"]
      """  Indicates if the unit price for the qty break has been manually modified  """  
      self.CalcProfit:int = obj["CalcProfit"]
      """  Worksheet field  """  
      self.CalcProfitProfit:int = obj["CalcProfitProfit"]
      """  CalcProfit Profit calculation  """  
      self.CalcUnitCost:int = obj["CalcUnitCost"]
      """  Worksheet field  """  
      self.CalcUnitPriceMarkup:int = obj["CalcUnitPriceMarkup"]
      """  Worksheet field  """  
      self.CalcUnitPriceProfit:int = obj["CalcUnitPriceProfit"]
      """  Worksheet field  """  
      self.CalcUPCommMarkup:int = obj["CalcUPCommMarkup"]
      """  Worksheet field  """  
      self.CalcUPCommProfit:int = obj["CalcUPCommProfit"]
      """  Worksheet field  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DisableMtlMarkup:bool = obj["DisableMtlMarkup"]
      """  Flag to indicate when to disable/enable material markup field  """  
      self.MaterialMarkupM:int = obj["MaterialMarkupM"]
      """  External field for MaterialMarkup Markup calculations  """  
      self.MaterialMarkupP:int = obj["MaterialMarkupP"]
      """  External field for MaterialMarkup Profit calculations  """  
      self.MiscChrg:str = obj["MiscChrg"]
      """  Indicates if the record has a miscellaneous charge associated with it  """  
      self.PriceBurMarkup:int = obj["PriceBurMarkup"]
      """  Worksheet field  """  
      self.PriceBurProfit:int = obj["PriceBurProfit"]
      """  Worksheet field  """  
      self.PriceLbrMarkup:int = obj["PriceLbrMarkup"]
      """  Worksheet field  """  
      self.PriceLbrProfit:int = obj["PriceLbrProfit"]
      """  Worksheet field  """  
      self.PriceMscChrgMarkup:int = obj["PriceMscChrgMarkup"]
      """  Worksheet field  """  
      self.PriceMscChrgProfit:int = obj["PriceMscChrgProfit"]
      """  Worksheet field  """  
      self.PriceMtlBurMarkup:int = obj["PriceMtlBurMarkup"]
      """  Worksheet field  """  
      self.PriceMtlBurProfit:int = obj["PriceMtlBurProfit"]
      """  Worksheet field  """  
      self.PriceMtlMarkup:int = obj["PriceMtlMarkup"]
      """  Worksheet field  """  
      self.PriceMtlProfit:int = obj["PriceMtlProfit"]
      """  Worksheet field  """  
      self.PricePerFactor:int = obj["PricePerFactor"]
      """  Integer value of the PricePerCode field (for calculations)  """  
      self.PriceSubMarkup:int = obj["PriceSubMarkup"]
      """  Worksheet field  """  
      self.PriceSubProfit:int = obj["PriceSubProfit"]
      """  Worksheet field  """  
      self.PriceTotalCommMarkup:int = obj["PriceTotalCommMarkup"]
      """  Worksheet field  """  
      self.PriceTotalCommProfit:int = obj["PriceTotalCommProfit"]
      """  Worksheet field  """  
      self.PriceTotalMarkup:int = obj["PriceTotalMarkup"]
      """  Worksheet field  """  
      self.PriceTotalProfit:int = obj["PriceTotalProfit"]
      """  Worksheet field  """  
      self.QuotedMarkup:int = obj["QuotedMarkup"]
      """  Worksheet field  """  
      self.QuotedProfit:int = obj["QuotedProfit"]
      """  Worksheet field  """  
      self.RollUpCostNeeded:bool = obj["RollUpCostNeeded"]
      """  If marked then the totals are not updated and a ?Roll up costs? is needed.  """  
      self.TotalBurCost:int = obj["TotalBurCost"]
      """  QuoteCst.TotalBurCost - Worksheet temp field  """  
      self.TotalCommission:int = obj["TotalCommission"]
      """  Worksheet field  """  
      self.TotalCommProfit:int = obj["TotalCommProfit"]
      """  Total Commision Profit calculation  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Worksheet field  """  
      self.TotalLbrCost:int = obj["TotalLbrCost"]
      """  QuoteCst.TotalLbrCost - Worksheet temp field  """  
      self.TotalMarkup:int = obj["TotalMarkup"]
      """  Worksheet field  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  QuoteCst.TotalMtlBurCost - Worksheet temp field  """  
      self.TotalMtlCost:int = obj["TotalMtlCost"]
      """  QuoteCst.TotalMtlCost - Worksheet temp field  """  
      self.TotalProdBurHrs:int = obj["TotalProdBurHrs"]
      """  QuoteCst.TotalProdBurHrs - Worksheet temp field  """  
      self.TotalProdLbrHrs:int = obj["TotalProdLbrHrs"]
      """  QuoteCst.TotalProdLbrHrs - Worksheet temp field  """  
      self.TotalProfit:int = obj["TotalProfit"]
      """  Worksheet field  """  
      self.TotalQuotedPrice:int = obj["TotalQuotedPrice"]
      """  Worksheet field  """  
      self.TotalSetupBurHrs:int = obj["TotalSetupBurHrs"]
      """  QuoteCst.TotalSetupBurHrs - Worksheet temp field  """  
      self.TotalSetupLbrHrs:int = obj["TotalSetupLbrHrs"]
      """  QuoteCst.TotalSetupLbrHrs - Worksheet temp field  """  
      self.TotalSubCost:int = obj["TotalSubCost"]
      """  QuoteCst.TotalSubCost - Worksheet temp field  """  
      self.WQUnitPrice:int = obj["WQUnitPrice"]
      """  Worksheet Quoted Unit Price  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CalcMarkup:int = obj["CalcMarkup"]
      """  Worksheet field  """  
      self.CalcMarkupProfit:int = obj["CalcMarkupProfit"]
      """  CalcMarkup Profit calculation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxConnectStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ETCOffline:bool = obj["ETCOffline"]
      """  If true, service is down. If false, service is up.  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error message returned from the call to the tax service.  """  
      self.TCStatus:bool = obj["TCStatus"]
      """  This is the success/failure status of the call to tax connect. If false, the call failed, if true it was successful  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhatIfSchedulingRow:
   def __init__(self, obj):
      self.CompletionDate:str = obj["CompletionDate"]
      self.ConsiderLeadTime:bool = obj["ConsiderLeadTime"]
      self.ProdQty:int = obj["ProdQty"]
      """  Production Qty  """  
      self.ProdStartDate:str = obj["ProdStartDate"]
      self.SchedFinitely:bool = obj["SchedFinitely"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AllowUndoReadyToQuote_output:
   def __init__(self, obj):
      pass

class ApplyOrderBasedDiscount_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      pass

class ApplyOrderBasedDiscount_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_input:
   """ Required : 
   quoteNum
   quoteLines
   quoteFields
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLines:str = obj["quoteLines"]
      self.quoteFields:str = obj["quoteFields"]
      pass

class ApplyQuoteHeadPropagatedFieldsToExistingQuoteDtls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class AssignAttrSellingExpectedUM_input:
   """ Required : 
   quoteNum
   quoteLine
   sellingExpectedUM
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum  """  
      self.quoteLine:int = obj["quoteLine"]
      """  QuoteNum  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Quote sellingExpectedUM  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class AssignAttrSellingExpectedUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignQuoteDtlAttributeDispValues_input:
   """ Required : 
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class AssignQuoteDtlAttributeDispValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalcConvUOMUnitPrice_input:
   """ Required : 
   inQuoteQtyUM
   inPartNum
   inSellingUM
   inKitParentUnitPrice
   inquantity
   """  
   def __init__(self, obj):
      self.inQuoteQtyUM:str = obj["inQuoteQtyUM"]
      self.inPartNum:str = obj["inPartNum"]
      self.inSellingUM:str = obj["inSellingUM"]
      self.inKitParentUnitPrice:int = obj["inKitParentUnitPrice"]
      self.inquantity:int = obj["inquantity"]
      pass

class CalcConvUOMUnitPrice_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class CalcMaterialMarkup_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Num  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Qty Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CalcMaterialMarkup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Calc_QuoteDtlDiscount_input:
   """ Required : 
   quoteNum
   quoteLine
   quantityToOrder
   sellingUM
   OrderHedDiscountPercent
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.quantityToOrder:int = obj["quantityToOrder"]
      self.sellingUM:str = obj["sellingUM"]
      self.OrderHedDiscountPercent:int = obj["OrderHedDiscountPercent"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class Calc_QuoteDtlDiscount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateQuoteDtlUnitPrice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CalculateQuoteDtlUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDiscBreakListCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeDiscBreakListCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDocOrderUnitPrice_input:
   """ Required : 
   newDocOrderUnitPrice
   ds
   """  
   def __init__(self, obj):
      self.newDocOrderUnitPrice:int = obj["newDocOrderUnitPrice"]
      """  The new DocOrderUnitPrice value.  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeDocOrderUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlContractNum_input:
   """ Required : 
   ipContractNum
   ds
   """  
   def __init__(self, obj):
      self.ipContractNum:int = obj["ipContractNum"]
      """  Proposed Contract Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeDtlContractNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlRenewalNbr_input:
   """ Required : 
   ipRenewalNbr
   ds
   """  
   def __init__(self, obj):
      self.ipRenewalNbr:int = obj["ipRenewalNbr"]
      """  Proposed Renewal Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeDtlRenewalNbr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlReturnLineType_input:
   """ Required : 
   ipReturnLineType
   ds
   """  
   def __init__(self, obj):
      self.ipReturnLineType:str = obj["ipReturnLineType"]
      """  The proposed Return Line Type  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeDtlReturnLineType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeKitPricing_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeKitPricing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeKitQtyPer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeKitQtyPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMFCustID_input:
   """ Required : 
   ipMFCustID
   ds
   """  
   def __init__(self, obj):
      self.ipMFCustID:str = obj["ipMFCustID"]
      """  The proposed Mark For Customer ID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeMFCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMFShipToNum_input:
   """ Required : 
   proposedMFShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedMFShipToNum:str = obj["proposedMFShipToNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeMFShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMSRP_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeMSRP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeManualTaxCalc_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   RateCode
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote line number.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Code  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate code  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeManualTaxCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscAmt_input:
   """ Required : 
   ds
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      pass

class ChangeMiscAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscPercent_input:
   """ Required : 
   ds
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      pass

class ChangeMiscPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscellanousChargeType_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The name of the table  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeMiscellanousChargeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeOrderQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOverrideDiscPriceList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeOverrideDiscPriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNumMaster_input:
   """ Required : 
   partNum
   lIsPhantom
   lIsSalesKit
   uomCode
   rowType
   SysRowID
   salesKitView
   removeKitComponents
   suppressUserPrompts
   runChkPrePartInfo
   getPartXRefInfo
   checkChangeKitParent
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  proposed PartNum  """  
      self.lIsPhantom:bool = obj["lIsPhantom"]
      """  bool which identifies whether this is a phantom part.  set in 'getPartXRefInfo' logic  """  
      self.lIsSalesKit:bool = obj["lIsSalesKit"]
      """  bool which identifies whether this is a saleskit part.  set in 'getPartXRefInfo' logic  """  
      self.uomCode:str = obj["uomCode"]
      """  associated uomCode for this part.  maybe overwritten in chkPartXRefInfo  """  
      self.rowType:str = obj["rowType"]
      """  part Type for this row  """  
      self.SysRowID:str = obj["SysRowID"]
      """  sysRowID for current row  """  
      self.salesKitView:bool = obj["salesKitView"]
      """  flag to identify whether this OrderDtl record is from salesKitView (or OrderDtlView)  """  
      self.removeKitComponents:bool = obj["removeKitComponents"]
      """  flag (set by user unless suppressUserPrompts is true) to ok removing kit components if kit parent changes  """  
      self.suppressUserPrompts:bool = obj["suppressUserPrompts"]
      """  flag to determine is user wants to be able to respond to messages and return to UI  """  
      self.runChkPrePartInfo:bool = obj["runChkPrePartInfo"]
      """  flag to determine whether the logic in runChkPrePartInfo is run  """  
      self.getPartXRefInfo:bool = obj["getPartXRefInfo"]
      """  flag to determine whether a particular part of validation logic is run  """  
      self.checkChangeKitParent:bool = obj["checkChangeKitParent"]
      """  flag to determine whether a particular part of validation logic is run  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangePartNumMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.lIsPhantom:bool = obj["lIsPhantom"]
      self.lIsSalesKit:bool = obj["lIsSalesKit"]
      self.uomCode:str = obj["parameters"]
      self.vMessage:str = obj["parameters"]
      self.vPMessage:str = obj["parameters"]
      self.vBMessage:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      self.cDeleteComponentsMessage:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.promptToExplodeBOM:bool = obj["promptToExplodeBOM"]
      self.explodeBOMerrMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   ds
   lSubstitutePartsExist
   uomCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.lSubstitutePartsExist:bool = obj["lSubstitutePartsExist"]
      """  Flag to indicate if a substitute part exists  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartRev_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangePartRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeProdCode_input:
   """ Required : 
   ds
   prodCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.prodCode:str = obj["prodCode"]
      """  product group  """  
      pass

class ChangeProdCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePromotionalPrice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangePromotionalPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteCntCustID_input:
   """ Required : 
   pcCustID
   ds
   """  
   def __init__(self, obj):
      self.pcCustID:str = obj["pcCustID"]
      """  Proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeQuoteCntCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteCoPartPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeQuoteCoPartPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteHedOTSCountryNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeQuoteHedOTSCountryNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteHedUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeQuoteHedUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSellingExpQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeSellingExpQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToCustID_input:
   """ Required : 
   iShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.iShipToCustID:str = obj["iShipToCustID"]
      """  Ship To Customer ID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStandardPct_input:
   """ Required : 
   markupId
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.markupId:str = obj["markupId"]
      """  Standard Percent Markup Id  """  
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Quantity Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeStandardPct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxRegionCode_input:
   """ Required : 
   ds
   FromTable
   ipNewCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.FromTable:str = obj["FromTable"]
      self.ipNewCode:str = obj["ipNewCode"]
      pass

class ChangeTaxRegionCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.promptTaxRegionCodeMsg:bool = obj["promptTaxRegionCodeMsg"]
      pass

      """  output parameters  """  

class ChangeUseOTMF_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ChangeUseOTMF_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBOMErrors_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  QuoteLine, 0 for all lines, otherwise only looks a specific line  """  
      pass

class CheckBOMErrors_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorList:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCustomerCreditLimit_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CheckCustomerCreditLimit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.cCreditLimitMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckIfConfigured_input:
   """ Required : 
   relatedToTable
   relatedSysRowID
   """  
   def __init__(self, obj):
      self.relatedToTable:str = obj["relatedToTable"]
      self.relatedSysRowID:str = obj["relatedSysRowID"]
      pass

class CheckIfConfigured_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isConfigured:bool = obj["isConfigured"]
      self.groupSeq:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPhaseID_input:
   """ Required : 
   ipProjectID
   ipPhaseID
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  Project ID  """  
      self.ipPhaseID:str = obj["ipPhaseID"]
      """  Phase ID  """  
      pass

class CheckPhaseID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opProjMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPreCustPartInfo_input:
   """ Required : 
   xPartNum
   custNum
   partNum
   """  
   def __init__(self, obj):
      self.xPartNum:str = obj["xPartNum"]
      """  The new Customenr Part Number  """  
      self.custNum:int = obj["custNum"]
      """  The current QuoteHed.CustNum  """  
      self.partNum:str = obj["partNum"]
      """  The new Part Num for this Customer Part  """  
      pass

class CheckPreCustPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   quoteNum
   quoteLine
   fieldName
   partNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      self.quoteLine:int = obj["quoteLine"]
      """  The current QuoteDtl.QuoteLine field  """  
      self.fieldName:str = obj["fieldName"]
      """  The name of the field you are leaving  """  
      self.partNum:str = obj["partNum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMessage:str = obj["parameters"]
      self.vBMessage:str = obj["parameters"]
      self.vPMessage:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPreQuoteCoPartInfo_input:
   """ Required : 
   ipProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPartNum:str = obj["ipProposedPartNum"]
      """  The new proposed QuoteCoPart.CoPartNum value  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CheckPreQuoteCoPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckProjectID_input:
   """ Required : 
   ds
   ipProjectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.ipProjectID:str = obj["ipProjectID"]
      """  Project ID  """  
      pass

class CheckProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.ipProjectID:str = obj["parameters"]
      self.opProjMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckQuoteDtlContractID_input:
   """ Required : 
   QuoteNum
   QuoteLine
   ipContractID
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.ipContractID:str = obj["ipContractID"]
      """  Contract ID to return  """  
      pass

class CheckQuoteDtlContractID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipContractID:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckQuoteHedChangesBeforeUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CheckQuoteHedChangesBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.propagateChangesMessage:str = obj["parameters"]
      self.fieldsToPropagate:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckQuoteNum_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      pass

class CheckQuoteNum_output:
   def __init__(self, obj):
      pass

class CheckQuoteSecurity_input:
   """ Required : 
   ipquoteNum
   """  
   def __init__(self, obj):
      self.ipquoteNum:int = obj["ipquoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      pass

class CheckQuoteSecurity_output:
   def __init__(self, obj):
      pass

class CheckRateGrpCode_input:
   """ Required : 
   ipRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Currency Rate Group Code  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CheckRateGrpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckSpecificPartRevIsApproved_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class CheckSpecificPartRevIsApproved_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ClearQuoteDtlDealerData_input:
   """ Required : 
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The quote number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ClearQuoteDtlDealerData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CollapsePhantom_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipAsmSeq
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      self.ipAsmSeq:int = obj["ipAsmSeq"]
      pass

class CollapsePhantom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class CompanyTaxConnectStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ConfigurationChangePart_input:
   """ Required : 
   QuoteDtlSysRowID
   """  
   def __init__(self, obj):
      self.QuoteDtlSysRowID:str = obj["QuoteDtlSysRowID"]
      """  QuoteDtl SysRowID  """  
      pass

class ConfigurationChangePart_output:
   def __init__(self, obj):
      pass

class ConfigurationChangeUnitPrice_input:
   """ Required : 
   quoteDtlSysRowID
   commitValues
   currencySwitch
   """  
   def __init__(self, obj):
      self.quoteDtlSysRowID:str = obj["quoteDtlSysRowID"]
      """  QuoteDtl SysRowID  """  
      self.commitValues:bool = obj["commitValues"]
      """  True to indicate if the changes should be committed to the DB. False if the logic only needs to compare the entity before and after the changes without commit them.  """  
      self.currencySwitch:bool = obj["currencySwitch"]
      """  Flag to indicate which currency was affected by the Document Rule, true for Base Currency and false for Document Currency.  """  
      pass

class ConfigurationChangeUnitPrice_output:
   def __init__(self, obj):
      pass

class ConfigurationRefreshQty_input:
   """ Required : 
   QuoteDtlSysRowID
   """  
   def __init__(self, obj):
      self.QuoteDtlSysRowID:str = obj["QuoteDtlSysRowID"]
      """  QuoteDtl SysRowID  """  
      pass

class ConfigurationRefreshQty_output:
   def __init__(self, obj):
      pass

class CopyLines_input:
   """ Required : 
   targetQuoteNum
   sourceQuoteLines
   mtlCosts
   opStds
   ds
   """  
   def __init__(self, obj):
      self.targetQuoteNum:int = obj["targetQuoteNum"]
      """  The Quote to write the lines to  """  
      self.sourceQuoteLines:str = obj["sourceQuoteLines"]
      """  A delimited list of quote lines to be copied.  Format - QuoteNum tick QuoteLine tilde QuoteNum tick QuoteLine  """  
      self.mtlCosts:bool = obj["mtlCosts"]
      """  Indicates if Material/Operation Costs should be refreshed  """  
      self.opStds:bool = obj["opStds"]
      """  Indicates if Operation Standards should be refreshed  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CopyLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateOrderFromQuoteSaveOTS_input:
   """ Required : 
   otsDS
   recalculateDiscount
   ds
   """  
   def __init__(self, obj):
      self.otsDS:list[Erp_Tablesets_SaveQuoteOTSParamsTableset] = obj["otsDS"]
      self.recalculateDiscount:bool = obj["recalculateDiscount"]
      """  Recalculate discount percent  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CreateOrderFromQuoteSaveOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.orderNum:int = obj["parameters"]
      self.newOrderMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateOrderFromQuote_input:
   """ Required : 
   recalculateDiscount
   ds
   """  
   def __init__(self, obj):
      self.recalculateDiscount:bool = obj["recalculateDiscount"]
      """  Recalculate discount percent  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CreateOrderFromQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.orderNum:int = obj["parameters"]
      self.newOrderMessage:str = obj["parameters"]
      self.warningMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateOrderSaveOTS_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SaveQuoteOTSParamsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_QuoteTableset] = obj["ds1"]
      pass

class CreateOrderSaveOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds1:list[Erp_Tablesets_QuoteTableset] = obj["ds1"]
      self.orderNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class CreateOrder_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CreateOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.orderNum:int = obj["parameters"]
      self.warningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateQuoteCntNoCustCnt_input:
   """ Required : 
   quoteNum
   custNum
   perConID
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.custNum:int = obj["custNum"]
      self.perConID:int = obj["perConID"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CreateQuoteCntNoCustCnt_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateQuoteDtlComplements_input:
   """ Required : 
   iQuoteNum
   ds
   """  
   def __init__(self, obj):
      self.iQuoteNum:int = obj["iQuoteNum"]
      """  The Quote Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class CreateQuoteDtlComplements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultOrderFields_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      pass

class DefaultOrderFields_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.creditMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateQuote_input:
   """ Required : 
   sourceQuote
   sourceLines
   mtlCosts
   opStds
   """  
   def __init__(self, obj):
      self.sourceQuote:int = obj["sourceQuote"]
      """  The Quote to duplicate  """  
      self.sourceLines:str = obj["sourceLines"]
      """  List of lines from the source Quote to be copied. If blank
            all lines will be copied Format:QuoteLine~QuoteLine  """  
      self.mtlCosts:bool = obj["mtlCosts"]
      """  Indicates if Material/Operation Costs should be refreshed  """  
      self.opStds:bool = obj["opStds"]
      """  Indicates if Operation Standards should be refreshed  """  
      pass

class DuplicateQuote_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class ETCAfterAddressValidationOTS_input:
   """ Required : 
   ds
   ds1
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds1"]
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteHed.QuoteNum  """  
      pass

class ETCAfterAddressValidationOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ETCValidateAddress_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteHed.QuoteNum  """  
      self.quoteLine:int = obj["quoteLine"]
      """  QuoteDtl.QuoteLine  """  
      pass

class ETCValidateAddress_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.errorFlag:bool = obj["errorFlag"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ETCAddrValidationTableset:
   def __init__(self, obj):
      self.ETCAddress:list[Erp_Tablesets_ETCAddressRow] = obj["ETCAddress"]
      self.ETCMessage:list[Erp_Tablesets_ETCMessageRow] = obj["ETCMessage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ETCAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.City:str = obj["City"]
      """  City name  """  
      self.Country:str = obj["Country"]
      """  Country name  """  
      self.Line1:str = obj["Line1"]
      """  Address line 1  """  
      self.Line2:str = obj["Line2"]
      """  Address line 2  """  
      self.Line3:str = obj["Line3"]
      """  Address line 3  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal or ZIP code  """  
      self.Region:str = obj["Region"]
      """  State or province name  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.UpdateAddr:bool = obj["UpdateAddr"]
      """  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  """  
      self.RequestID:str = obj["RequestID"]
      """  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  """  
      self.AddressCode:str = obj["AddressCode"]
      """  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  """  
      self.CarrierRoute:str = obj["CarrierRoute"]
      """  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  """  
      self.ValidCity:str = obj["ValidCity"]
      """  City name  """  
      self.ValidCountry:str = obj["ValidCountry"]
      """  Country name  """  
      self.County:str = obj["County"]
      """  County name  """  
      self.FipsCode:str = obj["FipsCode"]
      """  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  """  
      self.ValidLine1:str = obj["ValidLine1"]
      """  Line one of the valid address returned by the tax integration.  """  
      self.ValidLine2:str = obj["ValidLine2"]
      """  Line two of the valid address returned by the tax integration.  """  
      self.ValidLine3:str = obj["ValidLine3"]
      """  Line three of the valid address returned by the tax integration.  """  
      self.ValidLine4:str = obj["ValidLine4"]
      """  Line four of the valid address returned by the tax integration.  """  
      self.ValidPostalCode:str = obj["ValidPostalCode"]
      """  Postal code returned by the tax integration.  """  
      self.PostNet:str = obj["PostNet"]
      """  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  """  
      self.ValidRegion:str = obj["ValidRegion"]
      """  State or province name or abbreviation returned by the tax integration.  """  
      self.ResultCode:str = obj["ResultCode"]
      """  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.ResultSeq:int = obj["ResultSeq"]
      """  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  """  
      self.CarrierRouteDesc:str = obj["CarrierRouteDesc"]
      """  Carrier Route description  """  
      self.AddressTypeDesc:str = obj["AddressTypeDesc"]
      """  Address type description  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ETCMessageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Details:str = obj["Details"]
      self.Helplink:str = obj["Helplink"]
      """  URL to help page for this message  """  
      self.Name:str = obj["Name"]
      """  Gets the name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  """  
      self.Severity:str = obj["Severity"]
      """  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.Source:str = obj["Source"]
      """  source of the message  """  
      self.Summary:str = obj["Summary"]
      """  concise summary of the message  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.RequestID:str = obj["RequestID"]
      """  Programitically assigned.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HedTaxSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency display switch  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  Document reportable amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Document taxable amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document tax amount.  """  
      self.HedNum:int = obj["HedNum"]
      """  Order or Quote number this tax summary relates to.  """  
      self.Percent:int = obj["Percent"]
      """  Tax percent  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  Reportable amount  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable amount  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax amount  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax code  """  
      self.TaxDescription:str = obj["TaxDescription"]
      """  Sales Tax description  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.RateCode:str = obj["RateCode"]
      """  Rate Code on the Header Tax Summary  """  
      self.AllocDepInvcNum:int = obj["AllocDepInvcNum"]
      """  Invoice Number of allocated Deposits  """  
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      """  Rate Code Description on the Header Tax Summary  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
      self.SugOrderQty:int = obj["SugOrderQty"]
      """  Suggested Quantity for Order Qty in Quote Detail  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      self.SubPartIUM:str = obj["SubPartIUM"]
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QSalesRPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote that this record is linked to.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  Identifies the Sales Rep linked to the Quote.  """  
      self.Name:str = obj["Name"]
      """  The Sales Reps Name from the SalesRep table  """  
      self.PrimeRep:bool = obj["PrimeRep"]
      """  Identifies the primary sales rep on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  """  
      self.RepRate:int = obj["RepRate"]
      """  Establishes the defaults sales rep commission rates. Default is the SALESREP.COMMISSIONPERCENT.  """  
      self.RepSplit:int = obj["RepSplit"]
      """  Split percent is used to calculate the "commissionable"  dollar  amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Link to the RoleCD Table where Roles are defined.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OfficePhone:str = obj["OfficePhone"]
      self.HomePhone:str = obj["HomePhone"]
      self.ReportsTo:str = obj["ReportsTo"]
      self.EmailAddress:str = obj["EmailAddress"]
      self.Fax:str = obj["Fax"]
      self.MobilePhone:str = obj["MobilePhone"]
      self.SalesRepTitle:str = obj["SalesRepTitle"]
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.SalesRepCodePerConID:int = obj["SalesRepCodePerConID"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QtQtyMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHead  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  CurrencyCode.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscChrgDescription:str = obj["MiscChrgDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QtmmkupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteHead.QuoteNum that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteDtl.QuoteLine to which the markup is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  the specific QuoteQty record that this markup is related to.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Descriptive Code assigned by the user to uniquely identify the Part Class master record. This is the unique identifier for Qtmmkup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Material cost Markup Percent  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Used:bool = obj["Used"]
      """  Indicates if Markup is used by QuoteMtl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassCodeInactive:bool = obj["ClassCodeInactive"]
      self.ClassCodeDescription:str = obj["ClassCodeDescription"]
      self.QtyNumMiscCostDesc:str = obj["QtyNumMiscCostDesc"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number. This Quote Contact is linked to this QuoteHed  """  
      self.CustNum:int = obj["CustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Name of contact.  """  
      self.PrimeContact:bool = obj["PrimeContact"]
      """  Primary contact for this quote.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PerConID:int = obj["PerConID"]
      """  PerConID  """  
      self.Func:str = obj["Func"]
      """  CustCnt.Func  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  CustCnt.PhoneNum  """  
      self.Fax:str = obj["Fax"]
      """  CustCnt.Fax  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  CustCnt.EmailAddress  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumMiddleName:str = obj["ConNumMiddleName"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumFirstName:str = obj["ConNumFirstName"]
      self.ConNumLastName:str = obj["ConNumLastName"]
      self.ConNumCorpName:str = obj["ConNumCorpName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCoPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.CoPartNum:str = obj["CoPartNum"]
      """  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  """  
      self.CoRevisionNum:str = obj["CoRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  If true, MRP will not generate change suggestions for the co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartMasterPart:bool = obj["PartMasterPart"]
      self.EnablePreventSugg:bool = obj["EnablePreventSugg"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteComRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote that this QuoteCom is related to.  """  
      self.CompNum:int = obj["CompNum"]
      """  The unique key for the CRMComp Master table.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.PrimeComp:bool = obj["PrimeComp"]
      """  Identifies the primary Competitor on the quote.  The first one assigned will be defaulted as prime.  If manually changed then the existing one must be unchecked.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  CRMComp  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  CRMCall.PhoneNum  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  CRMCall.EmailAddress  """  
      self.CompURL:str = obj["CompURL"]
      """  CRMCall.CompURL  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCustTrkRow:
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      """  from QuoteHed.QuoteNum  """  
      self.Quoted:bool = obj["Quoted"]
      """  from QuoteHed.Quoted  """  
      self.Expired:bool = obj["Expired"]
      """  from QuoteHed.Expired  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  from QuoteHed.ExpirationDate  """  
      self.Company:str = obj["Company"]
      """  from QuoteHed.Company  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  form QuoteHed.CustomerCustID  """  
      self.CustomerName:str = obj["CustomerName"]
      """  from QuoteHed.CustomeName  """  
      self.PartNum:str = obj["PartNum"]
      """  from QuoteDtl.PartNum  """  
      self.LineDesc:str = obj["LineDesc"]
      """  from QuoteDtl.LineDesc  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """  from QuoteHed.CurrentStage  """  
      self.EntryDate:str = obj["EntryDate"]
      """  from QuoteHed.EntryDate  """  
      self.DueDate:str = obj["DueDate"]
      """  from QuoteHed.DueDate  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  from QuoteHed.MktgCampaignID  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  from QuoteDlt.DocExpectedRevenue  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  from QuoteDtl.ExpectedRevenue  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  from QuoteHed.MktgEvntSeq  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  from QuoteHed.ShipToNum  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  from QuoteHed.PrcConNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  from QuoteDtl.QuoteLine  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  from QuoteDtl.TerritoryID  """  
      self.ProdCode:str = obj["ProdCode"]
      """  from QuoteDtl.ProdCode  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  from QuoteDtl.ProdCodeDescription  """  
      self.CustNum:int = obj["CustNum"]
      """  from QuoteHed.CustNum  """  
      self.ShipConNum:int = obj["ShipConNum"]
      """  from QuoteHed.ShipConNum  """  
      self.Reference:str = obj["Reference"]
      """  from QuoteHed.Reference  """  
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  from QuoteHed.CurrentStageDesc  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  from QuoteDtl.RevisionNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  from QuoteDtl.xPartNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  from QuoteDtl.XRevisionNum  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill to customer number  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill to customer ID  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill to address list  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteCustTrkTableset:
   def __init__(self, obj):
      self.QuoteCustTrk:list[Erp_Tablesets_QuoteCustTrkRow] = obj["QuoteCustTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line attribute set record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote number to which this line attribute set record is associated with.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  Dynamic Attribute Value Set ID for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure).  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure).  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispNumberOfPiecesUOM:str = obj["DispNumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.RFQCurrBaseEst:str = obj["RFQCurrBaseEst"]
      """  RFQCurrBaseEst  """  
      self.RFQTemplate:str = obj["RFQTemplate"]
      """  RFQTemplate  """  
      self.CreateEstimate:bool = obj["CreateEstimate"]
      """  CreateEstimate  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECC Quote Line  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Ref  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  Indicates if no tax recalculation by the system is supposed to be done.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.ExternalCRMQuoteLineID:str = obj["ExternalCRMQuoteLineID"]
      """  This field holds the id of this quote line in the External CRM  """  
      self.ReturnLineType:str = obj["ReturnLineType"]
      """  Type for returns: Blank, (C)redit or (S)tandard  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  Mark For ShipToNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Contact Name  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.BasePotential:int = obj["BasePotential"]
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.DocPotential:int = obj["DocPotential"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.HasCreditMemo:bool = obj["HasCreditMemo"]
      """  Indicates if this Quote line has an associated credit memo (only for dealer portal)  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.LineStatus:str = obj["LineStatus"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  """  
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Selected:bool = obj["Selected"]
      """  Selected row  """  
      self.ShipByDate:str = obj["ShipByDate"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalQuote:int = obj["TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.UpdateReq:bool = obj["UpdateReq"]
      """   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Indicates that the Quote should be used as the BOM when creating a job for the linked order  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.ECCLineCRQ:int = obj["ECCLineCRQ"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the Dynamic Attributes button on a Quote Line  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.MarkForAddressFormatted:str = obj["MarkForAddressFormatted"]
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in Doc currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      """   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.QuoteNumInPrice:bool = obj["QuoteNumInPrice"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line related to the Tax Record  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code.  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an quote. When the sales tax field EcAquisition is checked then 2 quote tax records are created.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  QuoteDtl.TaxCode and QuoteDtl.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount. Manually entered if QuoteDtlTax.Manual = Yes else set equal to SysCalcReportableAmt.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (quotedtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the quotedtl.TaxCat and the QuoteDtlTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this quote. This is defaulted from the SalesTax.Percent.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the QuoteDtlTax.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the QuoteDtlTax.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax line is for a Reverse Charge.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the tax.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the tax converted to the customers currency.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution date.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.DefTaxableAmt:int = obj["DefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.DocDefTaxableAmt:int = obj["DocDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment  """  
      self.Rpt1DefTaxableAmt:int = obj["Rpt1DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxableAmt:int = obj["Rpt2DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxableAmt:int = obj["Rpt3DefTaxableAmt"]
      """  Reporting currency value of this field  """  
      self.DefTaxAmt:int = obj["DefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.DocDefTaxAmt:int = obj["DocDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment  """  
      self.Rpt1DefTaxAmt:int = obj["Rpt1DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DefTaxAmt:int = obj["Rpt2DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DefTaxAmt:int = obj["Rpt3DefTaxAmt"]
      """  Reporting currency value of this field  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.DedTaxAmt:int = obj["DedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.DocDedTaxAmt:int = obj["DocDedTaxAmt"]
      """  Deducatable Tax Amount  """  
      self.Rpt1DedTaxAmt:int = obj["Rpt1DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DedTaxAmt:int = obj["Rpt2DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DedTaxAmt:int = obj["Rpt3DedTaxAmt"]
      """  Reporting currency value of this field  """  
      self.FixedAmount:int = obj["FixedAmount"]
      """  Fixed Tax Amount  """  
      self.DocFixedAmount:int = obj["DocFixedAmount"]
      """  Fixed Tax Amount  """  
      self.Rpt1FixedAmount:int = obj["Rpt1FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2FixedAmount:int = obj["Rpt2FixedAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3FixedAmount:int = obj["Rpt3FixedAmount"]
      """  Reporting currency value of this field  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description for CurrentStage field  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill to customer id.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CustomerName:str = obj["CustomerName"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedListTableset:
   def __init__(self, obj):
      self.QuoteHedList:list[Erp_Tablesets_QuoteHedListRow] = obj["QuoteHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteHedMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHedMsc  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the overall Quote. These will be printed on the Quote form.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """  Optional check off # 2.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """  Optional check off # 3.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional check off # 4.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional check off # 5.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.FlwAlrtSnt:bool = obj["FlwAlrtSnt"]
      """  System maintained flag - set to yes when the quote follow up alert has been sent.  """  
      self.DueAlrtSnt:bool = obj["DueAlrtSnt"]
      """  System maintained flag - set to yes when the quote due date alert has been sent.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LeadRating:str = obj["LeadRating"]
      """  A = High, Z = Low  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.ParentQuoteNum:int = obj["ParentQuoteNum"]
      """  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ExpectedClose:str = obj["ExpectedClose"]
      """  The date this quote is expected to close.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.QuoteClosed:bool = obj["QuoteClosed"]
      """  This quote is no longer updatable.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The date that the Quote was closed.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the quote.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.LockRate:bool = obj["LockRate"]
      """  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.QuoteAmt:int = obj["QuoteAmt"]
      """  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  """  
      self.DocQuoteAmt:int = obj["DocQuoteAmt"]
      """  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1QuoteAmt:int = obj["Rpt1QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2QuoteAmt:int = obj["Rpt2QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3QuoteAmt:int = obj["Rpt3QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready.  """  
      self.EDIQuote:bool = obj["EDIQuote"]
      """  Quote created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module this type of document is created.  """  
      self.OutboundQuoteDocCtr:int = obj["OutboundQuoteDocCtr"]
      """  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote header is linked to an inter-company PO header.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.VoidQuote:bool = obj["VoidQuote"]
      """  Indicates that the Quote item was closed before any shipments were made against it.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.TotalDiscPct:int = obj["TotalDiscPct"]
      """  Total discount percent.  """  
      self.TotalExpected:int = obj["TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.TotalGrossValue:int = obj["TotalGrossValue"]
      self.TotalMiscAmt:int = obj["TotalMiscAmt"]
      self.TotalPotential:int = obj["TotalPotential"]
      self.TotalWorstCs:int = obj["TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.DocTotalBestCs:int = obj["DocTotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      self.DocTotalDiscPct:int = obj["DocTotalDiscPct"]
      """  Total discount percent.  """  
      self.DocTotalExpected:int = obj["DocTotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.DocTotalGrossValue:int = obj["DocTotalGrossValue"]
      self.DocTotalMiscAmt:int = obj["DocTotalMiscAmt"]
      self.DocTotalPotential:int = obj["DocTotalPotential"]
      self.DocTotalWorstCs:int = obj["DocTotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt1TotalBestCs:int = obj["Rpt1TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      self.Rpt1TotalDiscPct:int = obj["Rpt1TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt1TotalExpected:int = obj["Rpt1TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt1TotalGrossValue:int = obj["Rpt1TotalGrossValue"]
      self.Rpt1TotalMiscAmt:int = obj["Rpt1TotalMiscAmt"]
      self.Rpt1TotalPotential:int = obj["Rpt1TotalPotential"]
      self.Rpt1TotalWorstCs:int = obj["Rpt1TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt2TotalBestCs:int = obj["Rpt2TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      self.Rpt2TotalDiscPct:int = obj["Rpt2TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt2TotalExpected:int = obj["Rpt2TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt2TotalGrossValue:int = obj["Rpt2TotalGrossValue"]
      self.Rpt2TotalMiscAmt:int = obj["Rpt2TotalMiscAmt"]
      self.Rpt2TotalPotential:int = obj["Rpt2TotalPotential"]
      self.Rpt2TotalWorstCs:int = obj["Rpt2TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt3TotalBestCs:int = obj["Rpt3TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      self.Rpt3TotalDiscPct:int = obj["Rpt3TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt3TotalExpected:int = obj["Rpt3TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt3TotalGrossValue:int = obj["Rpt3TotalGrossValue"]
      self.Rpt3TotalMiscAmt:int = obj["Rpt3TotalMiscAmt"]
      self.Rpt3TotalPotential:int = obj["Rpt3TotalPotential"]
      self.Rpt3TotalWorstCs:int = obj["Rpt3TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.TotalBestCs:int = obj["TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.LOQPrepressText:str = obj["LOQPrepressText"]
      """  LOQPrepressText  """  
      self.LOQNewPageOnQuoteLine:bool = obj["LOQNewPageOnQuoteLine"]
      """  LOQNewPageOnQuoteLine  """  
      self.LOQBookPCFinishing:bool = obj["LOQBookPCFinishing"]
      """  LOQBookPCFinishing  """  
      self.LOQBookPCPaper:bool = obj["LOQBookPCPaper"]
      """  LOQBookPCPaper  """  
      self.LOQBookPCPress:bool = obj["LOQBookPCPress"]
      """  LOQBookPCPress  """  
      self.LOQBookPCPlates:bool = obj["LOQBookPCPlates"]
      """  LOQBookPCPlates  """  
      self.LOQVariations:bool = obj["LOQVariations"]
      """  LOQVariations  """  
      self.AEPLOQType:str = obj["AEPLOQType"]
      """  AEPLOQType  """  
      self.LOQPrepressStyle:str = obj["LOQPrepressStyle"]
      """  LOQPrepressStyle  """  
      self.QuoteCSR:str = obj["QuoteCSR"]
      """  QuoteCSR  """  
      self.DueHour:str = obj["DueHour"]
      """  DueHour  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCConfirmed:bool = obj["ECCConfirmed"]
      """  Quote was confirmed/rejected by ECC Web  """  
      self.ECCConfirmedBy:str = obj["ECCConfirmedBy"]
      """  Quote was confirmed/rejected by this ECC user  """  
      self.ECCMsgType:str = obj["ECCMsgType"]
      """  ECC quote message: RFQ or GQR  """  
      self.ECCWebReady:bool = obj["ECCWebReady"]
      """  Quote is ready to be approved by user via ECC web site.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Reference Number  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ECCStatus:str = obj["ECCStatus"]
      """  ECC Quote Status  """  
      self.ECCExpirationDate:str = obj["ECCExpirationDate"]
      """  ECC Expiration Date  """  
      self.ECCCmmtRefSK:str = obj["ECCCmmtRefSK"]
      """  ECCCmmtRefSK  """  
      self.ExternalCRMQuote:bool = obj["ExternalCRMQuote"]
      """  This field defines if the Quote  is synchronized to an External CRM.  """  
      self.ExternalCRMQuoteID:str = obj["ExternalCRMQuoteID"]
      """  This field holds the  id of this quote in the External CRM  """  
      self.ExternalCRMOrderID:str = obj["ExternalCRMOrderID"]
      """  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  """  
      self.ECCSalesRepID:str = obj["ECCSalesRepID"]
      """  Web Sales Rep ID  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  HdrTaxNoUpdt  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  """  
      self.TotalClaimsCredit:int = obj["TotalClaimsCredit"]
      """  Total of claims credit lines  """  
      self.DocTotalClaimsCredit:int = obj["DocTotalClaimsCredit"]
      """  Total of claims credit lines in customer currency  """  
      self.Rpt1TotalClaimsCredit:int = obj["Rpt1TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt2TotalClaimsCredit:int = obj["Rpt2TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt3TotalClaimsCredit:int = obj["Rpt3TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.TotalClaimsTax:int = obj["TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes.  """  
      self.DocTotalClaimsTax:int = obj["DocTotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in customer currency.  """  
      self.Rpt1TotalClaimsTax:int = obj["Rpt1TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt2TotalClaimsTax:int = obj["Rpt2TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt3TotalClaimsTax:int = obj["Rpt3TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.TotalClaimsSATax:int = obj["TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes.  """  
      self.DocTotalClaimsSATax:int = obj["DocTotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt1TotalClaimsSATax:int = obj["Rpt1TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt2TotalClaimsSATax:int = obj["Rpt2TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt3TotalClaimsSATax:int = obj["Rpt3TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.TotalClaimsWHTax:int = obj["TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes.  """  
      self.DocTotalClaimsWHTax:int = obj["DocTotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in customer currency.  """  
      self.Rpt1TotalClaimsWHTax:int = obj["Rpt1TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt2TotalClaimsWHTax:int = obj["Rpt2TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt3TotalClaimsWHTax:int = obj["Rpt3TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill To Customer Name.  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  Audit Log change description  """  
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.Conclusion:str = obj["Conclusion"]
      self.ConName:str = obj["ConName"]
      """  Primary Contact Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description of the CurrentStage field  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Value of the Customer.AllowOTS (customer allows one time shipment)  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DaysOpen:int = obj["DaysOpen"]
      """  Number of days Quote has been open  """  
      self.DiscountPercentCalc:int = obj["DiscountPercentCalc"]
      """   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the quote.  """  
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      self.EnableOrderBasedDisc:bool = obj["EnableOrderBasedDisc"]
      """  Indicates if it's okay to enable OrderBased Pricing  """  
      self.ExpectedCsPct:int = obj["ExpectedCsPct"]
      """   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  """  
      self.FaxNum:str = obj["FaxNum"]
      self.FOB:str = obj["FOB"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HasQuoteLines:bool = obj["HasQuoteLines"]
      """  Used by IU to disabled Currency Code  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  EqSyst.LogChanges  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date  """  
      self.OrderDiscount:int = obj["OrderDiscount"]
      self.OrderPONum:str = obj["OrderPONum"]
      self.OrderShipVia:str = obj["OrderShipVia"]
      self.OrderTerms:str = obj["OrderTerms"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PreventQQChange:bool = obj["PreventQQChange"]
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.TotalQuote:int = obj["TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.WorseCsPctCalc:int = obj["WorseCsPctCalc"]
      """   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BestCsPctCalc:int = obj["BestCsPctCalc"]
      """   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID of the bill to customer.  """  
      self.HasCreditLines:bool = obj["HasCreditLines"]
      """  Indicates if the order contains any credit type line  """  
      self.IsValidECC:bool = obj["IsValidECC"]
      """  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  """  
      self.EnableHDCaseNum:bool = obj["EnableHDCaseNum"]
      """  Flag indicating whether to enable CaseNum or not  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  Indicates if the quote can be updated  """  
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Formatted address  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To Address formatted  """  
      self.PromptTaxRegionCode:bool = obj["PromptTaxRegionCode"]
      """  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the quote is inactive.  """  
      self.UpdatePrimContact:bool = obj["UpdatePrimContact"]
      """  Update primary contact on save of the quote header  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskTaskDescription:str = obj["ActiveTaskTaskDescription"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyBaseCurr:bool = obj["CurrencyBaseCurr"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCheckDuplicatePO:bool = obj["CustomerCheckDuplicatePO"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.LastTaskTaskDescription:str = obj["LastTaskTaskDescription"]
      self.MktgCpgnCampDescription:str = obj["MktgCpgnCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ResponseCallTypeDesc:str = obj["ResponseCallTypeDesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaInactive:bool = obj["ShipViaInactive"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.XbSystCalcQuoteTax:bool = obj["XbSystCalcQuoteTax"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax ID from Sales Tax  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code on the Header Tax Summary  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this quote  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount for this quote  """  
      self.Percent:int = obj["Percent"]
      """  Calculated Tax Percent  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this quote  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount for this quote  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ClaimsTax:bool = obj["ClaimsTax"]
      """  Tax for claims credit tax.  This tax should not be included with regular tax.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteHedCurrencyCode:str = obj["QuoteHedCurrencyCode"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.SalesTaxDescDescription:str = obj["SalesTaxDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  The QtyNum of the QuoteQty record that this miscellaneous record is related to. If zero then it is related to the QuoteDtl record.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  An internally assigned integer which uniquely identifies the QuoteMsc record within the Quote/Line/QtySeq.  Assigned by using last number on file for the Quote/Line/QtySeq plus 1.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing.  The default is provided by MiscChrg.Description, but it can be overridden by the user. This cannot be blank.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  The amount of the Miscellaneous Charge/Credit (display value).  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.FreqCode:str = obj["FreqCode"]
      """  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  Reserved for future use  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reserved for future use  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reserved for future use  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DspMiscAmt:int = obj["DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.DocDspMiscAmt:int = obj["DocDspMiscAmt"]
      """  Display Document amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt1DspMiscAmt:int = obj["Rpt1DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt2DspMiscAmt:int = obj["Rpt2DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.Rpt3DspMiscAmt:int = obj["Rpt3DspMiscAmt"]
      """  Display amount of the Miscellaneous Charge/Credit.  Cannot be zero.  Use MiscChrg.MiscAmt as a default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteQtyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote # that this record is linked to.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine to which this QuoteQty record is related to.  """  
      self.QtyNum:int = obj["QtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file. Allowing virtually unlimited quantities to be quoted for each detail line on a quote. This number is assigned as one greater than last one on file for the given QuoteDtl record.  """  
      self.OurQuantity:int = obj["OurQuantity"]
      """  Represents one of the requested Quote Quantities for the line item using QuoteQty.IUM.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Quoted unit price for the given quantity. This value is entered by the user.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed).
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteQty.Quantity by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Material Bur Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Material Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  SubContract Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Labor Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.MiscCostDesc:str = obj["MiscCostDesc"]
      """  Miscellaneous Cost description.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Miscellaneous Cost amount that will be considered in the unit price calculations.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Miscellaneous Cost Markup Percent for this quoted quantity. May default from the QMarkUp file. By either using the default established for the customer (Customer.QMarkUpID) or the one established for the system (EQSyst.QMarkUpID) otherwise zero.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values. Prices can be calculated either as a straight markup of cost ( Cost + (Cost *  x %)) or a percent of profit ( Cost / (100% -  x%).   PercentType "M" = straight markup, "P" = Profit Percent. Defaulted from referenced QMarkup, from EQSyst.PercentType if not blank, else default as "M".  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure (how it is stocked).  Use the default Part.IUM if its a valid part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Quote Quantities for the line item using QuoteQty.SUM.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Reserved for future use  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reserved for future use  """  
      self.PriceSource:str = obj["PriceSource"]
      """  PriceSource  """  
      self.PricePerAdl1000:int = obj["PricePerAdl1000"]
      """  PricePerAdl1000  """  
      self.TotalSellPrice:int = obj["TotalSellPrice"]
      """  TotalSellPrice  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocPricePerAdl1000:int = obj["DocPricePerAdl1000"]
      """  DocPricePerAdl1000  """  
      self.DocTotalSellPrice:int = obj["DocTotalSellPrice"]
      """  DocTotalSellPrice  """  
      self.UserChangedUnitPrice:bool = obj["UserChangedUnitPrice"]
      """  Indicates if the unit price for the qty break has been manually modified  """  
      self.CalcProfit:int = obj["CalcProfit"]
      """  Worksheet field  """  
      self.CalcProfitProfit:int = obj["CalcProfitProfit"]
      """  CalcProfit Profit calculation  """  
      self.CalcUnitCost:int = obj["CalcUnitCost"]
      """  Worksheet field  """  
      self.CalcUnitPriceMarkup:int = obj["CalcUnitPriceMarkup"]
      """  Worksheet field  """  
      self.CalcUnitPriceProfit:int = obj["CalcUnitPriceProfit"]
      """  Worksheet field  """  
      self.CalcUPCommMarkup:int = obj["CalcUPCommMarkup"]
      """  Worksheet field  """  
      self.CalcUPCommProfit:int = obj["CalcUPCommProfit"]
      """  Worksheet field  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DisableMtlMarkup:bool = obj["DisableMtlMarkup"]
      """  Flag to indicate when to disable/enable material markup field  """  
      self.MaterialMarkupM:int = obj["MaterialMarkupM"]
      """  External field for MaterialMarkup Markup calculations  """  
      self.MaterialMarkupP:int = obj["MaterialMarkupP"]
      """  External field for MaterialMarkup Profit calculations  """  
      self.MiscChrg:str = obj["MiscChrg"]
      """  Indicates if the record has a miscellaneous charge associated with it  """  
      self.PriceBurMarkup:int = obj["PriceBurMarkup"]
      """  Worksheet field  """  
      self.PriceBurProfit:int = obj["PriceBurProfit"]
      """  Worksheet field  """  
      self.PriceLbrMarkup:int = obj["PriceLbrMarkup"]
      """  Worksheet field  """  
      self.PriceLbrProfit:int = obj["PriceLbrProfit"]
      """  Worksheet field  """  
      self.PriceMscChrgMarkup:int = obj["PriceMscChrgMarkup"]
      """  Worksheet field  """  
      self.PriceMscChrgProfit:int = obj["PriceMscChrgProfit"]
      """  Worksheet field  """  
      self.PriceMtlBurMarkup:int = obj["PriceMtlBurMarkup"]
      """  Worksheet field  """  
      self.PriceMtlBurProfit:int = obj["PriceMtlBurProfit"]
      """  Worksheet field  """  
      self.PriceMtlMarkup:int = obj["PriceMtlMarkup"]
      """  Worksheet field  """  
      self.PriceMtlProfit:int = obj["PriceMtlProfit"]
      """  Worksheet field  """  
      self.PricePerFactor:int = obj["PricePerFactor"]
      """  Integer value of the PricePerCode field (for calculations)  """  
      self.PriceSubMarkup:int = obj["PriceSubMarkup"]
      """  Worksheet field  """  
      self.PriceSubProfit:int = obj["PriceSubProfit"]
      """  Worksheet field  """  
      self.PriceTotalCommMarkup:int = obj["PriceTotalCommMarkup"]
      """  Worksheet field  """  
      self.PriceTotalCommProfit:int = obj["PriceTotalCommProfit"]
      """  Worksheet field  """  
      self.PriceTotalMarkup:int = obj["PriceTotalMarkup"]
      """  Worksheet field  """  
      self.PriceTotalProfit:int = obj["PriceTotalProfit"]
      """  Worksheet field  """  
      self.QuotedMarkup:int = obj["QuotedMarkup"]
      """  Worksheet field  """  
      self.QuotedProfit:int = obj["QuotedProfit"]
      """  Worksheet field  """  
      self.RollUpCostNeeded:bool = obj["RollUpCostNeeded"]
      """  If marked then the totals are not updated and a ?Roll up costs? is needed.  """  
      self.TotalBurCost:int = obj["TotalBurCost"]
      """  QuoteCst.TotalBurCost - Worksheet temp field  """  
      self.TotalCommission:int = obj["TotalCommission"]
      """  Worksheet field  """  
      self.TotalCommProfit:int = obj["TotalCommProfit"]
      """  Total Commision Profit calculation  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Worksheet field  """  
      self.TotalLbrCost:int = obj["TotalLbrCost"]
      """  QuoteCst.TotalLbrCost - Worksheet temp field  """  
      self.TotalMarkup:int = obj["TotalMarkup"]
      """  Worksheet field  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  QuoteCst.TotalMtlBurCost - Worksheet temp field  """  
      self.TotalMtlCost:int = obj["TotalMtlCost"]
      """  QuoteCst.TotalMtlCost - Worksheet temp field  """  
      self.TotalProdBurHrs:int = obj["TotalProdBurHrs"]
      """  QuoteCst.TotalProdBurHrs - Worksheet temp field  """  
      self.TotalProdLbrHrs:int = obj["TotalProdLbrHrs"]
      """  QuoteCst.TotalProdLbrHrs - Worksheet temp field  """  
      self.TotalProfit:int = obj["TotalProfit"]
      """  Worksheet field  """  
      self.TotalQuotedPrice:int = obj["TotalQuotedPrice"]
      """  Worksheet field  """  
      self.TotalSetupBurHrs:int = obj["TotalSetupBurHrs"]
      """  QuoteCst.TotalSetupBurHrs - Worksheet temp field  """  
      self.TotalSetupLbrHrs:int = obj["TotalSetupLbrHrs"]
      """  QuoteCst.TotalSetupLbrHrs - Worksheet temp field  """  
      self.TotalSubCost:int = obj["TotalSubCost"]
      """  QuoteCst.TotalSubCost - Worksheet temp field  """  
      self.WQUnitPrice:int = obj["WQUnitPrice"]
      """  Worksheet Quoted Unit Price  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CalcMarkup:int = obj["CalcMarkup"]
      """  Worksheet field  """  
      self.CalcMarkupProfit:int = obj["CalcMarkupProfit"]
      """  CalcMarkup Profit calculation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteTableset:
   def __init__(self, obj):
      self.QuoteHed:list[Erp_Tablesets_QuoteHedRow] = obj["QuoteHed"]
      self.QuoteHedAttch:list[Erp_Tablesets_QuoteHedAttchRow] = obj["QuoteHedAttch"]
      self.QSalesRP:list[Erp_Tablesets_QSalesRPRow] = obj["QSalesRP"]
      self.QuoteCnt:list[Erp_Tablesets_QuoteCntRow] = obj["QuoteCnt"]
      self.QuoteCom:list[Erp_Tablesets_QuoteComRow] = obj["QuoteCom"]
      self.QuoteDtl:list[Erp_Tablesets_QuoteDtlRow] = obj["QuoteDtl"]
      self.QuoteDtlAttch:list[Erp_Tablesets_QuoteDtlAttchRow] = obj["QuoteDtlAttch"]
      self.QuoteCoPart:list[Erp_Tablesets_QuoteCoPartRow] = obj["QuoteCoPart"]
      self.QuoteDtlAttrValueSet:list[Erp_Tablesets_QuoteDtlAttrValueSetRow] = obj["QuoteDtlAttrValueSet"]
      self.QuoteDtlTax:list[Erp_Tablesets_QuoteDtlTaxRow] = obj["QuoteDtlTax"]
      self.QuoteMsc:list[Erp_Tablesets_QuoteMscRow] = obj["QuoteMsc"]
      self.QuoteQty:list[Erp_Tablesets_QuoteQtyRow] = obj["QuoteQty"]
      self.Qtmmkup:list[Erp_Tablesets_QtmmkupRow] = obj["Qtmmkup"]
      self.QtQtyMsc:list[Erp_Tablesets_QtQtyMscRow] = obj["QtQtyMsc"]
      self.QuoteHedMsc:list[Erp_Tablesets_QuoteHedMscRow] = obj["QuoteHedMsc"]
      self.QuoteHedTax:list[Erp_Tablesets_QuoteHedTaxRow] = obj["QuoteHedTax"]
      self.HedTaxSum:list[Erp_Tablesets_HedTaxSumRow] = obj["HedTaxSum"]
      self.PartSubs:list[Erp_Tablesets_PartSubsRow] = obj["PartSubs"]
      self.TaxConnectStatus:list[Erp_Tablesets_TaxConnectStatusRow] = obj["TaxConnectStatus"]
      self.WhatIfScheduling:list[Erp_Tablesets_WhatIfSchedulingRow] = obj["WhatIfScheduling"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SaveOTSParamsRow:
   def __init__(self, obj):
      self.OTSAddress1:str = obj["OTSAddress1"]
      self.OTSAddress2:str = obj["OTSAddress2"]
      self.OTSAddress3:str = obj["OTSAddress3"]
      self.OTSCity:str = obj["OTSCity"]
      self.OTSContact:str = obj["OTSContact"]
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      self.OTSName:str = obj["OTSName"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      self.OTSResaleID:str = obj["OTSResaleID"]
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      self.OTSState:str = obj["OTSState"]
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      self.OTSZIP:str = obj["OTSZIP"]
      self.OTSOverride:bool = obj["OTSOverride"]
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SaveQuoteOTSParamsTableset:
   def __init__(self, obj):
      self.SaveOTSParams:list[Erp_Tablesets_SaveOTSParamsRow] = obj["SaveOTSParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxConnectStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ETCOffline:bool = obj["ETCOffline"]
      """  If true, service is down. If false, service is up.  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error message returned from the call to the tax service.  """  
      self.TCStatus:bool = obj["TCStatus"]
      """  This is the success/failure status of the call to tax connect. If false, the call failed, if true it was successful  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtQuoteTableset:
   def __init__(self, obj):
      self.QuoteHed:list[Erp_Tablesets_QuoteHedRow] = obj["QuoteHed"]
      self.QuoteHedAttch:list[Erp_Tablesets_QuoteHedAttchRow] = obj["QuoteHedAttch"]
      self.QSalesRP:list[Erp_Tablesets_QSalesRPRow] = obj["QSalesRP"]
      self.QuoteCnt:list[Erp_Tablesets_QuoteCntRow] = obj["QuoteCnt"]
      self.QuoteCom:list[Erp_Tablesets_QuoteComRow] = obj["QuoteCom"]
      self.QuoteDtl:list[Erp_Tablesets_QuoteDtlRow] = obj["QuoteDtl"]
      self.QuoteDtlAttch:list[Erp_Tablesets_QuoteDtlAttchRow] = obj["QuoteDtlAttch"]
      self.QuoteCoPart:list[Erp_Tablesets_QuoteCoPartRow] = obj["QuoteCoPart"]
      self.QuoteDtlAttrValueSet:list[Erp_Tablesets_QuoteDtlAttrValueSetRow] = obj["QuoteDtlAttrValueSet"]
      self.QuoteDtlTax:list[Erp_Tablesets_QuoteDtlTaxRow] = obj["QuoteDtlTax"]
      self.QuoteMsc:list[Erp_Tablesets_QuoteMscRow] = obj["QuoteMsc"]
      self.QuoteQty:list[Erp_Tablesets_QuoteQtyRow] = obj["QuoteQty"]
      self.Qtmmkup:list[Erp_Tablesets_QtmmkupRow] = obj["Qtmmkup"]
      self.QtQtyMsc:list[Erp_Tablesets_QtQtyMscRow] = obj["QtQtyMsc"]
      self.QuoteHedMsc:list[Erp_Tablesets_QuoteHedMscRow] = obj["QuoteHedMsc"]
      self.QuoteHedTax:list[Erp_Tablesets_QuoteHedTaxRow] = obj["QuoteHedTax"]
      self.HedTaxSum:list[Erp_Tablesets_HedTaxSumRow] = obj["HedTaxSum"]
      self.PartSubs:list[Erp_Tablesets_PartSubsRow] = obj["PartSubs"]
      self.TaxConnectStatus:list[Erp_Tablesets_TaxConnectStatusRow] = obj["TaxConnectStatus"]
      self.WhatIfScheduling:list[Erp_Tablesets_WhatIfSchedulingRow] = obj["WhatIfScheduling"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhatIfSchedulingRow:
   def __init__(self, obj):
      self.CompletionDate:str = obj["CompletionDate"]
      self.ConsiderLeadTime:bool = obj["ConsiderLeadTime"]
      self.ProdQty:int = obj["ProdQty"]
      """  Production Qty  """  
      self.ProdStartDate:str = obj["ProdStartDate"]
      self.SchedFinitely:bool = obj["SchedFinitely"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ExistContact_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QuoteCnt record  """  
      self.custNum:int = obj["custNum"]
      """  Customer Number of the QuoteCnt record  """  
      self.shipToNum:str = obj["shipToNum"]
      """  ShipTo Number of the QuoteCnt record  """  
      self.conNum:int = obj["conNum"]
      """  Contact Number of the QuoteCnt record  """  
      pass

class ExistContact_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistShipTo_input:
   """ Required : 
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number of the QuoteCnt record  """  
      self.shipToNum:str = obj["shipToNum"]
      """  ShipTo Number of the QuoteCnt record  """  
      pass

class ExistShipTo_output:
   def __init__(self, obj):
      pass

class ExistsCreditMemo_input:
   """ Required : 
   returnLineType
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.returnLineType:str = obj["returnLineType"]
      """  Return type selected  """  
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote line number  """  
      pass

class ExistsCreditMemo_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsPartDiscPriceList_input:
   """ Required : 
   quoteNum
   partNum
   sellingExpectedUM
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Selling Expected Unit Of Measure  """  
      pass

class ExistsPartDiscPriceList_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsPartPriceList_input:
   """ Required : 
   quoteNum
   partNum
   sellingExpectedUM
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Selling Expected Unit Of Measure  """  
      pass

class ExistsPartPriceList_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsProductGroupDiscPriceList_input:
   """ Required : 
   quoteNum
   prodCode
   sellingExpectedUM
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Selling Expected Unit Of Measure  """  
      pass

class ExistsProductGroupDiscPriceList_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsProductGroupPriceList_input:
   """ Required : 
   quoteNum
   prodCode
   sellingExpectedUM
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.prodCode:str = obj["prodCode"]
      """  Product Group  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Selling Expected Unit Of Measure  """  
      pass

class ExistsProductGroupPriceList_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExportQuoteToEST_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      pass

class ExportQuoteToEST_output:
   def __init__(self, obj):
      pass

class FileType_input:
   """ Required : 
   FileInfo
   """  
   def __init__(self, obj):
      self.FileInfo:str = obj["FileInfo"]
      pass

class FileType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCompetitorInfo_input:
   """ Required : 
   quoteNum
   compNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QuoteCom record  """  
      self.compNum:int = obj["compNum"]
      """  Competitor Number of the QuoteCom record  """  
      pass

class GetCompetitorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.name:str = obj["parameters"]
      self.faxNum:str = obj["parameters"]
      self.phoneNum:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      self.compURL:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetContactInfo_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QuoteCom record  """  
      self.custNum:int = obj["custNum"]
      """  Customr Number of the QuoteCom record  """  
      self.shipToNum:str = obj["shipToNum"]
      """  ShipTo Number of the QuoteCom record  """  
      self.conNum:int = obj["conNum"]
      """  Contact Number of the QuoteCom record  """  
      pass

class GetContactInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.perConID:int = obj["parameters"]
      self.perConName:str = obj["parameters"]
      self.name:str = obj["parameters"]
      self.func:str = obj["parameters"]
      self.phoneNum:str = obj["parameters"]
      self.fax:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCustCntInfo_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   perConID
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QuoteCom record  """  
      self.custNum:int = obj["custNum"]
      """  Customr Number of the QuoteCom record  """  
      self.shipToNum:str = obj["shipToNum"]
      """  input - output - ShipTo Number of the QuoteCom record  """  
      self.conNum:int = obj["conNum"]
      """  input output - Contact Number of the QuoteCom record  """  
      self.perConID:int = obj["perConID"]
      """  input output - The Contact PerConID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetCustCntInfo_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCustPartInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetCustPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCustomerInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetCustomerInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDiscountPriceListInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetDiscountPriceListInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlUnitPriceInfo_User_input:
   """ Required : 
   skipDiscLookup
   preserveAmt
   pIsGridPasting
   pChangedByUser
   ds
   """  
   def __init__(self, obj):
      self.skipDiscLookup:bool = obj["skipDiscLookup"]
      """  Skip lookup of DiscPercent  """  
      self.preserveAmt:bool = obj["preserveAmt"]
      """  Preserve the DiscountAmt  """  
      self.pIsGridPasting:bool = obj["pIsGridPasting"]
      """  Is a Paste Insert in the Grid  """  
      self.pChangedByUser:bool = obj["pChangedByUser"]
      """  The user typed the Unit Price  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetDtlUnitPriceInfo_User_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDtlUnitPriceInfo_input:
   """ Required : 
   skipDiscLookup
   preserveAmt
   ds
   """  
   def __init__(self, obj):
      self.skipDiscLookup:bool = obj["skipDiscLookup"]
      """  Skip lookup of DiscPercent  """  
      self.preserveAmt:bool = obj["preserveAmt"]
      """  Preserve the DiscountAmt  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetDtlUnitPriceInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetExchangeRate_input:
   """ Required : 
   vCurrencyCode
   vRateGrpCode
   """  
   def __init__(self, obj):
      self.vCurrencyCode:str = obj["vCurrencyCode"]
      """  Currency selected for the Quote  """  
      self.vRateGrpCode:str = obj["vRateGrpCode"]
      """  Currency Rate Group selected for the quote  """  
      pass

class GetExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vExchangeRate:int = obj["parameters"]
      self.vXRateLabel:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetExternalCRMIntegrationIsEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetIfCurrentSiteHasExternalMES_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetIfRevIsExternalMES_input:
   """ Required : 
   PartNum
   RevisionNum
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      pass

class GetIfRevIsExternalMES_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetKitComponents_input:
   """ Required : 
   iPartNum
   iRevisionNum
   iAltMethod
   iTargetAsm
   quoteNum
   quoteLine
   iUseMethodForParts
   regenerateKit
   errorMsg
   ds
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number of the given QuoteLine  """  
      self.iRevisionNum:str = obj["iRevisionNum"]
      """  Revision Number selected for the given PartNum  """  
      self.iAltMethod:str = obj["iAltMethod"]
      """  Aletrnate Method of the given Part number  """  
      self.iTargetAsm:int = obj["iTargetAsm"]
      """  Target assembly to be exploded (usually asm 0)  """  
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number to be exploded  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote line which will be the Kit Parent  """  
      self.iUseMethodForParts:bool = obj["iUseMethodForParts"]
      """  -  """  
      self.regenerateKit:bool = obj["regenerateKit"]
      """  If TRUE then it will delete all components before getting them again  """  
      self.errorMsg:str = obj["errorMsg"]
      """  Input-Output parameter that will hold the error messages in case something went wrong  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetKitComponents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListCustom_input:
   """ Required : 
   whereClause
   whereClauseDtl
   pageSize
   absolutePage
   customClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.whereClauseDtl:str = obj["whereClauseDtl"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      self.customClause:str = obj["customClause"]
      """  Custom WhereClause  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForAuthorizedTerritories_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListForAuthorizedTerritories_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteHedListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteHedListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMaterialMarkup_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Num  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Qty Number  """  
      pass

class GetMaterialMarkup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mtlMarkupP:int = obj["parameters"]
      self.mtlMarkupM:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetMiscChrgDefaults_input:
   """ Required : 
   ds
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      pass

class GetMiscChrgDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetMktgInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetMktgInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContractQuoteDtl_input:
   """ Required : 
   ds
   ipQuoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The quote number to add the line to  """  
      pass

class GetNewContractQuoteDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQSalesRP_input:
   """ Required : 
   ds
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetNewQSalesRP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQtQtyMsc_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   qtyNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.qtyNum:int = obj["qtyNum"]
      pass

class GetNewQtQtyMsc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQtmmkup_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   qtyNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.qtyNum:int = obj["qtyNum"]
      pass

class GetNewQtmmkup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteCnt_input:
   """ Required : 
   ds
   quoteNum
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.conNum:int = obj["conNum"]
      pass

class GetNewQuoteCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteCoPart_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetNewQuoteCoPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteCom_input:
   """ Required : 
   ds
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetNewQuoteCom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteDtlAttch_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetNewQuoteDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteDtlAttrValueSet_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetNewQuoteDtlAttrValueSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteDtlTax_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewQuoteDtlTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteDtl_input:
   """ Required : 
   ds
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetNewQuoteDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteHedAttch_input:
   """ Required : 
   ds
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetNewQuoteHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteHedMsc_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   qtyNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.qtyNum:int = obj["qtyNum"]
      pass

class GetNewQuoteHedMsc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteHedTax_input:
   """ Required : 
   ds
   quoteNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewQuoteHedTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetNewQuoteHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteMsc_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   qtyNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.qtyNum:int = obj["qtyNum"]
      pass

class GetNewQuoteMsc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuoteQty_input:
   """ Required : 
   ds
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetNewQuoteQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesKit_input:
   """ Required : 
   quoteNum
   quoteLine
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetNewSalesKit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   uomCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetPerConInfo_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   ipPerConID
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QuoteCom record  """  
      self.custNum:int = obj["custNum"]
      """  Customr Number of the QuoteCom record  """  
      self.shipToNum:str = obj["shipToNum"]
      """  ShipTo Number of the QuoteCom record  """  
      self.conNum:int = obj["conNum"]
      """  Contact Number of the QuoteCom record  """  
      self.ipPerConID:int = obj["ipPerConID"]
      """  the Contact PerConID  """  
      pass

class GetPerConInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.perConName:str = obj["parameters"]
      self.name:str = obj["parameters"]
      self.func:str = obj["parameters"]
      self.phoneNum:str = obj["parameters"]
      self.fax:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPerConInformation_input:
   """ Required : 
   perConID
   ds
   """  
   def __init__(self, obj):
      self.perConID:int = obj["perConID"]
      """  Person/Contact ID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetPerConInformation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.result:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPhantomComponents_input:
   """ Required : 
   phPartNum
   quoteNum
   quoteLine
   errMessage
   ds
   """  
   def __init__(self, obj):
      self.phPartNum:str = obj["phPartNum"]
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.errMessage:str = obj["errMessage"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetPhantomComponents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPlantConfCtrlUse3rdPartySched_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool: the value  """  
      pass

class GetPlantConfCtrlValues_input:
   """ Required : 
   ipCompanyID
   ipPlant
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      """  The company for the quote  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The login plant for the session  """  
      pass

class GetPlantConfCtrlValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opUse3rdPartySched:bool = obj["opUse3rdPartySched"]
      self.opEnableManifestRateShopping:bool = obj["opEnableManifestRateShopping"]
      self.opManifestRateShoppingURL:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPriceListInfo_input:
   """ Required : 
   ds
   refreshQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.refreshQty:bool = obj["refreshQty"]
      """  Indicate if the app needs to refresh the Quantity Breaks  """  
      pass

class GetPriceListInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetQtyPriceInfoCfgPart_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetQtyPriceInfoCfgPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.hasPriceBreak:bool = obj["hasPriceBreak"]
      pass

      """  output parameters  """  

class GetQtyPriceInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetQtyPriceInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.hasPriceBreak:bool = obj["hasPriceBreak"]
      pass

      """  output parameters  """  

class GetQtyToOrdPrice_input:
   """ Required : 
   quoteNum
   quoteLine
   quantityToOrder
   sellingUM
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.quantityToOrder:int = obj["quantityToOrder"]
      """  Quantity used to create order  """  
      self.sellingUM:str = obj["sellingUM"]
      """  Selling UM  """  
      pass

class GetQtyToOrdPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.orderUnitPrice:int = obj["parameters"]
      self.docOrderUnitPrice:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetQuoteRelationshipMap_input:
   """ Required : 
   quoteNum
   maxNumOfCards
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.maxNumOfCards:int = obj["maxNumOfCards"]
      pass

class GetQuoteRelationshipMap_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetQuotedInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetQuotedInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetQuotesForCustomer_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for quote retrieval.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetQuotesForCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetReasonInfo_input:
   """ Required : 
   vReasonType
   vQuoteNum
   vOrdered
   vReasonCode
   """  
   def __init__(self, obj):
      self.vReasonType:str = obj["vReasonType"]
      """  ReasonType of the Quote (Win, Task)  """  
      self.vQuoteNum:int = obj["vQuoteNum"]
      """  Unique key of the Quote  """  
      self.vOrdered:bool = obj["vOrdered"]
      """  Flag indicating if an order has been created from the quote  """  
      self.vReasonCode:str = obj["vReasonCode"]
      """  Default ReasonCode for the Quote Task/ReasonType  """  
      pass

class GetReasonInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vReasonCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      """  Whereclause for QuoteHed table.  """  
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      """  Whereclause for QuoteHedAttch table.  """  
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      """  Whereclause for QSalesRP table.  """  
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      """  Whereclause for QuoteCnt table.  """  
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      """  Whereclause for QuoteCom table.  """  
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      """  Whereclause for QuoteDtl table.  """  
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      """  Whereclause for QuoteDtlAt table.  """  
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      """  Whereclause for QuoteMsc table.  """  
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      """  Whereclause for QuoteHedMsc table.  """  
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      """  Whereclause for QuoteQty table.  """  
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      """  Whereclause for Qtmmkup table.  """  
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      """  Whereclause for QtQtyMsc table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteCustTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForCashReceipt_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   groupID
   headNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForCashReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForInvoice_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   invoiceNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.invoiceNum:int = obj["invoiceNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForInvoice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForSalesOrder_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   orderNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.orderNum:int = obj["orderNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForSalesOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForShipment_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   packNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.packNum:int = obj["packNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForShipment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuoteHed
   whereClauseQuoteHedAttch
   whereClauseQSalesRP
   whereClauseQuoteCnt
   whereClauseQuoteCom
   whereClauseQuoteDtl
   whereClauseQuoteDtlAttch
   whereClauseQuoteCoPart
   whereClauseQuoteDtlAttrValueSet
   whereClauseQuoteDtlTax
   whereClauseQuoteMsc
   whereClauseQuoteQty
   whereClauseQtmmkup
   whereClauseQtQtyMsc
   whereClauseQuoteHedMsc
   whereClauseQuoteHedTax
   whereClauseHedTaxSum
   whereClausePartSubs
   whereClauseTaxConnectStatus
   whereClauseWhatIfScheduling
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.whereClauseQuoteHedAttch:str = obj["whereClauseQuoteHedAttch"]
      self.whereClauseQSalesRP:str = obj["whereClauseQSalesRP"]
      self.whereClauseQuoteCnt:str = obj["whereClauseQuoteCnt"]
      self.whereClauseQuoteCom:str = obj["whereClauseQuoteCom"]
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.whereClauseQuoteDtlAttch:str = obj["whereClauseQuoteDtlAttch"]
      self.whereClauseQuoteCoPart:str = obj["whereClauseQuoteCoPart"]
      self.whereClauseQuoteDtlAttrValueSet:str = obj["whereClauseQuoteDtlAttrValueSet"]
      self.whereClauseQuoteDtlTax:str = obj["whereClauseQuoteDtlTax"]
      self.whereClauseQuoteMsc:str = obj["whereClauseQuoteMsc"]
      self.whereClauseQuoteQty:str = obj["whereClauseQuoteQty"]
      self.whereClauseQtmmkup:str = obj["whereClauseQtmmkup"]
      self.whereClauseQtQtyMsc:str = obj["whereClauseQtQtyMsc"]
      self.whereClauseQuoteHedMsc:str = obj["whereClauseQuoteHedMsc"]
      self.whereClauseQuoteHedTax:str = obj["whereClauseQuoteHedTax"]
      self.whereClauseHedTaxSum:str = obj["whereClauseHedTaxSum"]
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.whereClauseTaxConnectStatus:str = obj["whereClauseTaxConnectStatus"]
      self.whereClauseWhatIfScheduling:str = obj["whereClauseWhatIfScheduling"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesKitComponents_input:
   """ Required : 
   quoteNum
   quoteLine
   regenerateKits
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote line  """  
      self.regenerateKits:bool = obj["regenerateKits"]
      """  Regenerate kits  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetSalesKitComponents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.returnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSalesRepInfo_input:
   """ Required : 
   defaultRoleCode
   quoteNum
   salesRepCode
   roleCode
   """  
   def __init__(self, obj):
      self.defaultRoleCode:bool = obj["defaultRoleCode"]
      """  Indicates whether to default the RoleCode from the SalesRep  """  
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum of the QSalesRP record  """  
      self.salesRepCode:str = obj["salesRepCode"]
      """  Salesperson of the QSalesRP record  """  
      self.roleCode:str = obj["roleCode"]
      """  RoleCode of the QSalesRP record, if defaultRoleCode is checked, then
            a different value may be returned  """  
      pass

class GetSalesRepInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.roleCode:str = obj["parameters"]
      self.name:str = obj["parameters"]
      self.repRate:int = obj["parameters"]
      self.repSplit:int = obj["parameters"]
      self.officePhone:str = obj["parameters"]
      self.homePhone:str = obj["parameters"]
      self.reportsTo:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      self.fax:str = obj["parameters"]
      self.mobilePhone:str = obj["parameters"]
      self.salesRepTitle:str = obj["parameters"]
      self.roleCodeRoleDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetShipToInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetShipToInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSmartString_input:
   """ Required : 
   QuoteNum
   QuoteLine
   PartNum
   RevisionNum
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      """  Kit component quote number  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Kit component quote line  """  
      self.PartNum:str = obj["PartNum"]
      """  The part being configured  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision being configured  """  
      pass

class GetSmartString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SmartString:str = obj["parameters"]
      self.CreatePart:bool = obj["CreatePart"]
      self.PromptForPartNum:bool = obj["PromptForPartNum"]
      self.NotifyOfExistingPart:bool = obj["NotifyOfExistingPart"]
      self.NewPartNum:str = obj["parameters"]
      self.CreateCustPart:bool = obj["CreateCustPart"]
      self.PromptForCustPartNum:bool = obj["PromptForCustPartNum"]
      self.NewCustPartNum:str = obj["parameters"]
      self.PromptForAutoCreatePart:bool = obj["PromptForAutoCreatePart"]
      pass

      """  output parameters  """  

class GetTaskSetInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetTaskSetInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTaxRegInPrice_input:
   """ Required : 
   ipCompanyID
   ipQuoteNum
   ipCustNum
   ipShipToNum
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipCustNum:int = obj["ipCustNum"]
      self.ipShipToNum:str = obj["ipShipToNum"]
      pass

class GetTaxRegInPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTaxRegionCode:str = obj["parameters"]
      self.opInPrice:bool = obj["opInPrice"]
      self.opTaxRecords:bool = obj["opTaxRecords"]
      pass

      """  output parameters  """  

class GetTerrInfo_input:
   """ Required : 
   vQuoteNum
   vTerritoryID
   vActiveTaskID
   vTaskSetId
   """  
   def __init__(self, obj):
      self.vQuoteNum:int = obj["vQuoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      self.vTerritoryID:str = obj["vTerritoryID"]
      """  The QuoteHed.TerritoryID  """  
      self.vActiveTaskID:str = obj["vActiveTaskID"]
      """  The QuoteHed.ActiveTaskID  """  
      self.vTaskSetId:str = obj["vTaskSetId"]
      """  Returns the correct TaskSet for the Territory  """  
      pass

class GetTerrInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vTaskSetId:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetUpdtDtlTaxRgn_input:
   """ Required : 
   ipCompanyID
   ipQuoteNum
   ipCustNum
   ipShipToNum
   """  
   def __init__(self, obj):
      self.ipCompanyID:str = obj["ipCompanyID"]
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipCustNum:int = obj["ipCustNum"]
      self.ipShipToNum:str = obj["ipShipToNum"]
      pass

class GetUpdtDtlTaxRgn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opUpdtDtlTaxRgn:bool = obj["opUpdtDtlTaxRgn"]
      pass

      """  output parameters  """  

class GetWSUnitPrice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class GetWSUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class KitCompPartCreate_input:
   """ Required : 
   QuoteNum
   QuoteLine
   PartNum
   RevisionNum
   SmartString
   NewPartNum
   NewCustPartNum
   ResponseAutoCrtPart
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      """  Kit component quote number  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Kit component quote line  """  
      self.PartNum:str = obj["PartNum"]
      """  The part being configured  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision being configured  """  
      self.SmartString:str = obj["SmartString"]
      """  The generated smartstring of the configuration  """  
      self.NewPartNum:str = obj["NewPartNum"]
      """  The Part Number to be used for a new part creation.  If blank, a part will not be created.  """  
      self.NewCustPartNum:str = obj["NewCustPartNum"]
      """  The Customer Part Number to stored on the quote line.  """  
      self.ResponseAutoCrtPart:bool = obj["ResponseAutoCrtPart"]
      """  Answer to the question presented to user about auto creating a part.  """  
      pass

class KitCompPartCreate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NewPartAlreadyExists:bool = obj["NewPartAlreadyExists"]
      pass

      """  output parameters  """  

class LaunchGlobalAlerts_output:
   def __init__(self, obj):
      pass

class MinimumDate_input:
   """ Required : 
   date1
   date2
   """  
   def __init__(self, obj):
      self.date1:str = obj["date1"]
      self.date2:str = obj["date2"]
      pass

class MinimumDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class OnChangeAttrQuantityToOrder_input:
   """ Required : 
   attributeValueSeq
   quantityToOrder
   ds
   """  
   def __init__(self, obj):
      self.attributeValueSeq:int = obj["attributeValueSeq"]
      """  Attribute Value Sequence  """  
      self.quantityToOrder:int = obj["quantityToOrder"]
      """  Quantity To Order  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeAttrQuantityToOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeIncotermCode_input:
   """ Required : 
   incotermCode
   """  
   def __init__(self, obj):
      self.incotermCode:str = obj["incotermCode"]
      """  Incoterm Code  """  
      pass

class OnChangeIncotermCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.incotermLocation:str = obj["parameters"]
      self.enableIncotermLocation:bool = obj["enableIncotermLocation"]
      pass

      """  output parameters  """  

class OnChangeMktgCamp_input:
   """ Required : 
   mktgCampID
   ds
   """  
   def __init__(self, obj):
      self.mktgCampID:str = obj["mktgCampID"]
      """  The CampID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeMktgCamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMktgEvnt_input:
   """ Required : 
   mktgEvntSeq
   ds
   """  
   def __init__(self, obj):
      self.mktgEvntSeq:int = obj["mktgEvntSeq"]
      """  The EvntSeq  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeMktgEvnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeNumberOfPieces_input:
   """ Required : 
   attributeValueSeq
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.attributeValueSeq:int = obj["attributeValueSeq"]
      """  Attribute Value Sequence  """  
      self.numberOfPieces:int = obj["numberOfPieces"]
      """  Number Of Pieces  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfFixedAmount_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   RateCode
   NewFixedAmount
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TaxCode:str = obj["TaxCode"]
      self.RateCode:str = obj["RateCode"]
      self.NewFixedAmount:int = obj["NewFixedAmount"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeOfFixedAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfReportableAmt_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   NewReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TaxCode:str = obj["TaxCode"]
      self.NewReportableAmt:int = obj["NewReportableAmt"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeOfReportableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfTaxAmt_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   NewTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TaxCode:str = obj["TaxCode"]
      self.NewTaxAmt:int = obj["NewTaxAmt"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeOfTaxAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfTaxPercent_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   NewPercent
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TaxCode:str = obj["TaxCode"]
      self.NewPercent:int = obj["NewPercent"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeOfTaxPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRateCode_input:
   """ Required : 
   proposedRateCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateCode:str = obj["proposedRateCode"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeRateCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxCode_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   ipTaxCode
   ds
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      self.ipTaxCode:str = obj["ipTaxCode"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxableAmt_input:
   """ Required : 
   QuoteNum
   QuoteLine
   TaxCode
   RateCode
   NewTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TaxCode:str = obj["TaxCode"]
      self.RateCode:str = obj["RateCode"]
      self.NewTaxableAmt:int = obj["NewTaxableAmt"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeTaxableAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofBTCustID_input:
   """ Required : 
   newBillToCustID
   ds
   """  
   def __init__(self, obj):
      self.newBillToCustID:str = obj["newBillToCustID"]
      """  Proposed bill to custid  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeofBTCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofEngineered_input:
   """ Required : 
   newReadyToQuote
   ds
   """  
   def __init__(self, obj):
      self.newReadyToQuote:bool = obj["newReadyToQuote"]
      """  Proposed ReadyToQuote  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class OnChangeofEngineered_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofLineExemptTax_input:
   """ Required : 
   QuoteNum
   QuoteLine
   """  
   def __init__(self, obj):
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote line number.  """  
      pass

class OnChangeofLineExemptTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AskManualQuestion:bool = obj["AskManualQuestion"]
      pass

      """  output parameters  """  

class OpenCloseQuote_input:
   """ Required : 
   quoteNum
   closeQuote
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  QuoteNum to be opened or closed  """  
      self.closeQuote:bool = obj["closeQuote"]
      """  Yes to close Quote, no to open Quote  """  
      pass

class OpenCloseQuote_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class PopulateCallContext_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class PopulateCallContext_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.callContext:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreOpenCloseQuote_input:
   """ Required : 
   quoteNum
   closeQuote
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      self.closeQuote:bool = obj["closeQuote"]
      """  Yes to close Quote, no to open Quote  """  
      pass

class PreOpenCloseQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreRefreshQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class PreRefreshQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strquestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreSOCreate_input:
   """ Required : 
   ipQuoteNum
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  Quote number  """  
      pass

class PreSOCreate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ouAskMess:str = obj["parameters"]
      pass

      """  output parameters  """  

class PropagateQuoteHedChangesToQuoteDtl_input:
   """ Required : 
   quoteNum
   fieldList
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.fieldList:str = obj["fieldList"]
      """  List of fields to propagate  """  
      pass

class PropagateQuoteHedChangesToQuoteDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class QSalesRPPrimeRepChanging_input:
   """ Required : 
   proposedPrimRep
   ds
   """  
   def __init__(self, obj):
      self.proposedPrimRep:bool = obj["proposedPrimRep"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QSalesRPPrimeRepChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteCntShipToConNumChangedInactive_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.custNum:int = obj["custNum"]
      """  Customer number  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Number  """  
      self.conNum:int = obj["conNum"]
      """  Contact Number  """  
      pass

class QuoteCntShipToConNumChangedInactive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.perConID:int = obj["parameters"]
      self.perConName:str = obj["parameters"]
      self.name:str = obj["parameters"]
      self.contactFunc:str = obj["parameters"]
      self.phoneNum:str = obj["parameters"]
      self.faxNum:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      self.shipToInactive:bool = obj["shipToInactive"]
      pass

      """  output parameters  """  

class QuoteCntShipToConNumChanged_input:
   """ Required : 
   quoteNum
   custNum
   shipToNum
   conNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.custNum:int = obj["custNum"]
      """  Customer number  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Number  """  
      self.conNum:int = obj["conNum"]
      """  Contact Number  """  
      pass

class QuoteCntShipToConNumChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.perConID:int = obj["parameters"]
      self.perConName:str = obj["parameters"]
      self.name:str = obj["parameters"]
      self.contactFunc:str = obj["parameters"]
      self.phoneNum:str = obj["parameters"]
      self.faxNum:str = obj["parameters"]
      self.emailAddress:str = obj["parameters"]
      pass

      """  output parameters  """  

class QuoteCreditAdd_input:
   """ Required : 
   quoteNum
   quoteLines
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLines:str = obj["quoteLines"]
      """  delimited list of quotelines (e.g., "1~2~3"  """  
      pass

class QuoteCreditAdd_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.newInvoiceNum:int = obj["parameters"]
      self.opErrMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class QuoteDtlPartNumAfterChange_input:
   """ Required : 
   partHasSubstitutes
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.partHasSubstitutes:bool = obj["partHasSubstitutes"]
      """  Does the part have substitutes  """  
      self.uomCode:str = obj["uomCode"]
      """  Unit of measure code  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlPartNumAfterChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlReadyToQuoteChanging_input:
   """ Required : 
   readyToQuote
   ds
   """  
   def __init__(self, obj):
      self.readyToQuote:bool = obj["readyToQuote"]
      """  The propoesd Ready To Quote value  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlReadyToQuoteChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.returnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class QuoteDtlRefreshPriceListAndQuantities_input:
   """ Required : 
   refreshQty
   getDiscountPriceListInfo
   clearQuoteQty
   ds
   """  
   def __init__(self, obj):
      self.refreshQty:bool = obj["refreshQty"]
      """  Refresh quantities  """  
      self.getDiscountPriceListInfo:bool = obj["getDiscountPriceListInfo"]
      """  Get discount price list info  """  
      self.clearQuoteQty:bool = obj["clearQuoteQty"]
      """  Clear quote quanities before refresh  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlRefreshPriceListAndQuantities_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlRevisionNumAfterChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlRevisionNumAfterChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxBaseFixedAmountChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   rateCode
   newFixedAmount
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.rateCode:str = obj["rateCode"]
      """  Rate Code  """  
      self.newFixedAmount:int = obj["newFixedAmount"]
      """  New base fixed amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxBaseFixedAmountChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxBaseReportableAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   newReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.newReportableAmt:int = obj["newReportableAmt"]
      """  New base reportable amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxBaseReportableAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxBaseTaxAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   newTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.newTaxAmt:int = obj["newTaxAmt"]
      """  New base tax amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxBaseTaxAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxBaseTaxableAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   rateCode
   newTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.rateCode:str = obj["rateCode"]
      """  Rate Code  """  
      self.newTaxableAmt:int = obj["newTaxableAmt"]
      """  New base taxable amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxBaseTaxableAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxDocFixedAmountChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   rateCode
   newFixedAmount
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.rateCode:str = obj["rateCode"]
      """  Rate Code  """  
      self.newFixedAmount:int = obj["newFixedAmount"]
      """  New base fixed amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxDocFixedAmountChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxDocReportableAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   newReportableAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.newReportableAmt:int = obj["newReportableAmt"]
      """  New base reportable amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxDocReportableAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxDocTaxAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   newTaxAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.newTaxAmt:int = obj["newTaxAmt"]
      """  New base tax amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxDocTaxAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlTaxDocTaxableAmtChange_input:
   """ Required : 
   quoteNum
   quoteLine
   taxCode
   rateCode
   newTaxableAmt
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.taxCode:str = obj["taxCode"]
      """  Tax Code  """  
      self.rateCode:str = obj["rateCode"]
      """  Rate Code  """  
      self.newTaxableAmt:int = obj["newTaxableAmt"]
      """  New base taxable amount  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlTaxDocTaxableAmtChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteDtlXPartNumAfterChange_input:
   """ Required : 
   partIsInactiveOrOnHold
   partHasSubstitutes
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.partIsInactiveOrOnHold:bool = obj["partIsInactiveOrOnHold"]
      """  Is the part inactive or on hold  """  
      self.partHasSubstitutes:bool = obj["partHasSubstitutes"]
      """  Does the part have substitutes  """  
      self.uomCode:str = obj["uomCode"]
      """  Unit of measure code  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteDtlXPartNumAfterChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteHedCustomerCustIDAfterChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteHedCustomerCustIDAfterChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteHedSalesRepCodeChanging_input:
   """ Required : 
   salesRepCode
   ds
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      """  Proposed sales rep code  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteHedSalesRepCodeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuotePartNumHasSubstitutes_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number to be evaluated  """  
      pass

class QuotePartNumHasSubstitutes_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class QuoteQtyMaterialMarkupChanged_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   markupType
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote quantity number  """  
      self.markupType:str = obj["markupType"]
      """  (M)aterial, (P)rofit  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteQtyMaterialMarkupChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteQtyPercentTypeChanged_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Quantity number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteQtyPercentTypeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class QuoteQtyValidateAndRecalcWorksheet_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Quantity number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class QuoteQtyValidateAndRecalcWorksheet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecalcKitPriceAfterConfig_input:
   """ Required : 
   iQuoteNum
   iQuoteLine
   """  
   def __init__(self, obj):
      self.iQuoteNum:int = obj["iQuoteNum"]
      """  Quote Number for configured part  """  
      self.iQuoteLine:int = obj["iQuoteLine"]
      """  Quote Line for configured part  """  
      pass

class RecalcKitPriceAfterConfig_output:
   def __init__(self, obj):
      pass

class RecalcKitPricing_input:
   """ Required : 
   pCompany
   pQuoteNum
   parentLine
   """  
   def __init__(self, obj):
      self.pCompany:str = obj["pCompany"]
      self.pQuoteNum:int = obj["pQuoteNum"]
      self.parentLine:int = obj["parentLine"]
      pass

class RecalcKitPricing_output:
   def __init__(self, obj):
      pass

class RecalcWorksheet_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Num  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.qtyNum:int = obj["qtyNum"]
      """  Quote Qty Number  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class RecalcWorksheet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecalculateLineDiscounts_input:
   """ Required : 
   quoteHedDiscountPercent
   ds
   """  
   def __init__(self, obj):
      self.quoteHedDiscountPercent:int = obj["quoteHedDiscountPercent"]
      """  The quote header discount percent  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class RecalculateLineDiscounts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveKitComponents_input:
   """ Required : 
   iPartNum
   quoteNum
   quoteLine
   ds
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Parent Sales Kit number  """  
      self.quoteNum:int = obj["quoteNum"]
      """  Quote number of the QuoteDtl record (0 if an Order is being processed)  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line of the QuoteDtl record (0 if an Order is being processed  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class RemoveKitComponents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RequestEngineeringExternalMESValidation_input:
   """ Required : 
   quoteNum
   quoteLine
   partNum
   revision
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.partNum:str = obj["partNum"]
      self.revision:str = obj["revision"]
      pass

class RequestEngineeringExternalMESValidation_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SetDiscountAmountOverride_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class SetDiscountAmountOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetKBMaxConfigProdID_input:
   """ Required : 
   quoteNum
   quoteLine
   kbConfigProdID
   assemblySeq
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.kbConfigProdID:int = obj["kbConfigProdID"]
      """  CPQ Quote Product ID  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly sequence  """  
      pass

class SetKBMaxConfigProdID_output:
   def __init__(self, obj):
      pass

class SetOrderDefaults_input:
   """ Required : 
   quoteNum
   setReqShipDt
   setOrdQty
   reqShipDate
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The current QuoteHed.QuoteNum field  """  
      self.setReqShipDt:bool = obj["setReqShipDt"]
      """  Yes to set the QuoteDtl.ReqShipDate to the specified date  """  
      self.setOrdQty:bool = obj["setOrdQty"]
      """  Yes to set the Order Qty equal to the Expected Qty  """  
      self.reqShipDate:str = obj["reqShipDate"]
      """  Requested Ship Date  """  
      pass

class SetOrderDefaults_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteTableset] = obj["returnObj"]
      pass

class SetReadyToCalc_input:
   """ Required : 
   ipQuoteNum
   UserIntiatedCall
   ds
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The Quote Number  """  
      self.UserIntiatedCall:bool = obj["UserIntiatedCall"]
      """  Indicates if the user initiated the tax calculation.  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class SetReadyToCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateCosts_input:
   """ Required : 
   quoteNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The current QuoteQty.QuoteNum field  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class UpdateCosts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuoteTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuoteTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateKBMaxConfigurator_input:
   """ Required : 
   quoteNum
   quoteLine
   assemblySeq
   configuredProductJson
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  Quote Number  """  
      self.quoteLine:int = obj["quoteLine"]
      """  Quote Line  """  
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly sequence  """  
      self.configuredProductJson:str = obj["configuredProductJson"]
      """  CPQ Configurator data passed from the embed API  """  
      pass

class UpdateKBMaxConfigurator_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValReqRefDes_input:
   """ Required : 
   ipQuoteNum
   ipQuoteLine
   """  
   def __init__(self, obj):
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  Quote Number to validate  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  Quote Line of the Quote Number to validate  """  
      pass

class ValReqRefDes_output:
   def __init__(self, obj):
      pass

class ValidateECCType_input:
   """ Required : 
   customerID
   ds
   """  
   def __init__(self, obj):
      self.customerID:str = obj["customerID"]
      """  Proposed customer ID  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ValidateECCType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateOTS_output:
   def __init__(self, obj):
      pass

class ValidateProfits_input:
   """ Required : 
   quoteNum
   quoteLine
   qtyNum
   ds
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.qtyNum:int = obj["qtyNum"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ValidateProfits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateQuantityUOMQuoteDtlAttribute_input:
   """ Required : 
   partNum
   sellingExpectedUM
   attributeValueSeq
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  PartNum  """  
      self.sellingExpectedUM:str = obj["sellingExpectedUM"]
      """  Selling Expected UOM  """  
      self.attributeValueSeq:int = obj["attributeValueSeq"]
      """  Attribute Value Sequence  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ValidateQuantityUOMQuoteDtlAttribute_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSOCreate_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      """  The quote number  """  
      pass

class ValidateSOCreate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateShippingDate_input:
   """ Required : 
   proposedDate
   dateColumnName
   dateColumnTable
   ds
   """  
   def __init__(self, obj):
      self.proposedDate:str = obj["proposedDate"]
      """  New date to be validated  """  
      self.dateColumnName:str = obj["dateColumnName"]
      """  The column the proposed date is from  """  
      self.dateColumnTable:str = obj["dateColumnTable"]
      """  The table that the validating date belongs to  """  
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

class ValidateShippingDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.invalidDateMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuoteTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateTaskSet_input:
   """ Required : 
   ipTaskSetId
   ipActiveTaskID
   """  
   def __init__(self, obj):
      self.ipTaskSetId:str = obj["ipTaskSetId"]
      """  Task Set Id to validate  """  
      self.ipActiveTaskID:str = obj["ipActiveTaskID"]
      """  Active Task Id  """  
      pass

class ValidateTaskSet_output:
   def __init__(self, obj):
      pass

class WhatIfGetDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.schedDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class WhatIfScheduling_input:
   """ Required : 
   quoteNum
   quoteLine
   prodQty
   schedDate
   schedFinite
   considerLeadTime
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      self.prodQty:int = obj["prodQty"]
      self.schedDate:str = obj["schedDate"]
      self.schedFinite:bool = obj["schedFinite"]
      self.considerLeadTime:bool = obj["considerLeadTime"]
      pass

class WhatIfScheduling_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.completionDate:str = obj["parameters"]
      self.isProdQtyAvailable:bool = obj["isProdQtyAvailable"]
      pass

      """  output parameters  """  

class prjWBSPhaseDefinitionIsAllowed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

