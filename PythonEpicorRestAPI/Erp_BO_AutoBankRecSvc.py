import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AutoBankRecSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AutoBankRecs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AutoBankRecs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs",headers=creds) as resp:
           return await resp.json()

async def post_AutoBankRecs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AutoBankRecs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashBHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum(Company, CashBookNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AutoBankRec item
   Description: Calls GetByID to retrieve the AutoBankRec item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AutoBankRec
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AutoBankRecs_Company_CashBookNum(Company, CashBookNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AutoBankRec for the service
   Description: Calls UpdateExt to update AutoBankRec. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AutoBankRec
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AutoBankRecs_Company_CashBookNum(Company, CashBookNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AutoBankRec item
   Description: Call UpdateExt to delete AutoBankRec item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AutoBankRec
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBFilterOptions(Company, CashBookNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashBFilterOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBFilterOptions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBFilterOptionsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBFilterOptions",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company, CashBookNum, BankAcctID, LineType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBFilterOption item
   Description: Calls GetByID to retrieve the CashBFilterOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBFilterOption1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param LineType: Desc: LineType   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_SubLedgerDocs(Company, CashBookNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SubLedgerDocs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SubLedgerDocs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SubLedgerDocsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/SubLedgerDocs",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company, CashBookNum, BankAcctID, DocumentType, Reference, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SubLedgerDoc item
   Description: Calls GetByID to retrieve the SubLedgerDoc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SubLedgerDoc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param DocumentType: Desc: DocumentType   Required: True
      :param Reference: Desc: Reference   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBDtls(Company, CashBookNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashBDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBDtls",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBDtls_Company_CashBookNum_CashbookLine(Company, CashBookNum, CashbookLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBDtl item
   Description: Calls GetByID to retrieve the CashBDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBHedAttches(Company, CashBookNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashBHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBHedAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBHedAttches",headers=creds) as resp:
           return await resp.json()

async def get_AutoBankRecs_Company_CashBookNum_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company, CashBookNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBHedAttch item
   Description: Calls GetByID to retrieve the CashBHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBHedAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/AutoBankRecs(" + Company + "," + CashBookNum + ")/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBFilterOptions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashBFilterOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBFilterOptions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBFilterOptionsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions",headers=creds) as resp:
           return await resp.json()

async def post_CashBFilterOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBFilterOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company, BankAcctID, CashBookNum, LineType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBFilterOption item
   Description: Calls GetByID to retrieve the CashBFilterOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBFilterOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param LineType: Desc: LineType   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company, BankAcctID, CashBookNum, LineType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashBFilterOption for the service
   Description: Calls UpdateExt to update CashBFilterOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBFilterOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param LineType: Desc: LineType   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBFilterOptionsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashBFilterOptions_Company_BankAcctID_CashBookNum_LineType(Company, BankAcctID, CashBookNum, LineType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashBFilterOption item
   Description: Call UpdateExt to delete CashBFilterOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBFilterOption
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param LineType: Desc: LineType   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBFilterOptions(" + Company + "," + BankAcctID + "," + CashBookNum + "," + LineType + ")",headers=creds) as resp:
           return await resp.json()

async def get_SubLedgerDocs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SubLedgerDocs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SubLedgerDocs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SubLedgerDocsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs",headers=creds) as resp:
           return await resp.json()

async def post_SubLedgerDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SubLedgerDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company, BankAcctID, CashBookNum, DocumentType, Reference, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SubLedgerDoc item
   Description: Calls GetByID to retrieve the SubLedgerDoc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SubLedgerDoc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DocumentType: Desc: DocumentType   Required: True
      :param Reference: Desc: Reference   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company, BankAcctID, CashBookNum, DocumentType, Reference, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SubLedgerDoc for the service
   Description: Calls UpdateExt to update SubLedgerDoc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SubLedgerDoc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DocumentType: Desc: DocumentType   Required: True
      :param Reference: Desc: Reference   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SubLedgerDocsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SubLedgerDocs_Company_BankAcctID_CashBookNum_DocumentType_Reference(Company, BankAcctID, CashBookNum, DocumentType, Reference, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SubLedgerDoc item
   Description: Call UpdateExt to delete SubLedgerDoc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SubLedgerDoc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DocumentType: Desc: DocumentType   Required: True
      :param Reference: Desc: Reference   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/SubLedgerDocs(" + Company + "," + BankAcctID + "," + CashBookNum + "," + DocumentType + "," + Reference + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashBDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls",headers=creds) as resp:
           return await resp.json()

async def post_CashBDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls_Company_CashBookNum_CashbookLine(Company, CashBookNum, CashbookLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBDtl item
   Description: Calls GetByID to retrieve the CashBDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashBDtls_Company_CashBookNum_CashbookLine(Company, CashBookNum, CashbookLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashBDtl for the service
   Description: Calls UpdateExt to update CashBDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashBDtls_Company_CashBookNum_CashbookLine(Company, CashBookNum, CashbookLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashBDtl item
   Description: Call UpdateExt to delete CashBDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls_Company_CashBookNum_CashbookLine_MatchedDocuments(Company, CashBookNum, CashbookLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MatchedDocuments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MatchedDocuments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MatchedDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/MatchedDocuments",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls_Company_CashBookNum_CashbookLine_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company, CashBookNum, CashbookLine, BankAcctID, CashBookLine, MatchLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MatchedDocument item
   Description: Calls GetByID to retrieve the MatchedDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MatchedDocument1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookLine: Desc: CashBookLine   Required: True
      :param MatchLineNum: Desc: MatchLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls_Company_CashBookNum_CashbookLine_CashBDtlAttches(Company, CashBookNum, CashbookLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashBDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashBDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/CashBDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtls_Company_CashBookNum_CashbookLine_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company, CashBookNum, CashbookLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBDtlAttch item
   Description: Calls GetByID to retrieve the CashBDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtls(" + Company + "," + CashBookNum + "," + CashbookLine + ")/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MatchedDocuments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MatchedDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MatchedDocuments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MatchedDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments",headers=creds) as resp:
           return await resp.json()

async def post_MatchedDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MatchedDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company, BankAcctID, CashBookNum, CashBookLine, MatchLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MatchedDocument item
   Description: Calls GetByID to retrieve the MatchedDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MatchedDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashBookLine: Desc: CashBookLine   Required: True
      :param MatchLineNum: Desc: MatchLineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company, BankAcctID, CashBookNum, CashBookLine, MatchLineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MatchedDocument for the service
   Description: Calls UpdateExt to update MatchedDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MatchedDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashBookLine: Desc: CashBookLine   Required: True
      :param MatchLineNum: Desc: MatchLineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MatchedDocumentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MatchedDocuments_Company_BankAcctID_CashBookNum_CashBookLine_MatchLineNum(Company, BankAcctID, CashBookNum, CashBookLine, MatchLineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MatchedDocument item
   Description: Call UpdateExt to delete MatchedDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MatchedDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashBookLine: Desc: CashBookLine   Required: True
      :param MatchLineNum: Desc: MatchLineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/MatchedDocuments(" + Company + "," + BankAcctID + "," + CashBookNum + "," + CashBookLine + "," + MatchLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashBDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_CashBDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company, CashBookNum, CashbookLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBDtlAttch item
   Description: Calls GetByID to retrieve the CashBDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company, CashBookNum, CashbookLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashBDtlAttch for the service
   Description: Calls UpdateExt to update CashBDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashBDtlAttches_Company_CashBookNum_CashbookLine_DrawingSeq(Company, CashBookNum, CashbookLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashBDtlAttch item
   Description: Call UpdateExt to delete CashBDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param CashbookLine: Desc: CashbookLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBDtlAttches(" + Company + "," + CashBookNum + "," + CashbookLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashBHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashBHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashBHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_CashBHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashBHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company, CashBookNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashBHedAttch item
   Description: Calls GetByID to retrieve the CashBHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashBHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company, CashBookNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashBHedAttch for the service
   Description: Calls UpdateExt to update CashBHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashBHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashBHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashBHedAttches_Company_CashBookNum_DrawingSeq(Company, CashBookNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashBHedAttch item
   Description: Call UpdateExt to delete CashBHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashBHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashBookNum: Desc: CashBookNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/CashBHedAttches(" + Company + "," + CashBookNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankRecExchangeRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankRecExchangeRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankRecExchangeRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankRecExchangeRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates",headers=creds) as resp:
           return await resp.json()

async def post_BankRecExchangeRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankRecExchangeRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankRecExchangeRates_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankRecExchangeRate item
   Description: Calls GetByID to retrieve the BankRecExchangeRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankRecExchangeRate
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankRecExchangeRates_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankRecExchangeRate for the service
   Description: Calls UpdateExt to update BankRecExchangeRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankRecExchangeRate
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankRecExchangeRatesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankRecExchangeRates_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankRecExchangeRate item
   Description: Call UpdateExt to delete BankRecExchangeRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankRecExchangeRate
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecExchangeRates(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankRecMessages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankRecMessages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankRecMessages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankRecMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages",headers=creds) as resp:
           return await resp.json()

async def post_BankRecMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankRecMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankRecMessages_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankRecMessage item
   Description: Calls GetByID to retrieve the BankRecMessage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankRecMessage
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankRecMessages_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankRecMessage for the service
   Description: Calls UpdateExt to update BankRecMessage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankRecMessage
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankRecMessagesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankRecMessages_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankRecMessage item
   Description: Call UpdateExt to delete BankRecMessage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankRecMessage
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/BankRecMessages(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashBHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashBHed, whereClauseCashBHedAttch, whereClauseCashBFilterOptions, whereClauseSubLedgerDocs, whereClauseCashBDtl, whereClauseCashBDtlAttch, whereClauseMatchedDocuments, whereClauseBankRecExchangeRates, whereClauseBankRecMessages, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCashBHed=" + whereClauseCashBHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashBHedAttch=" + whereClauseCashBHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashBFilterOptions=" + whereClauseCashBFilterOptions
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSubLedgerDocs=" + whereClauseSubLedgerDocs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashBDtl=" + whereClauseCashBDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashBDtlAttch=" + whereClauseCashBDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMatchedDocuments=" + whereClauseMatchedDocuments
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankRecExchangeRates=" + whereClauseBankRecExchangeRates
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankRecMessages=" + whereClauseBankRecMessages
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(cashBookNum, epicorHeaders = None):
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
   params += "cashBookNum=" + cashBookNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddStatement
   Description: Add Statement.  It is similar to GetNewCashBHed in functionality.
It should be used to create CashBHed with BankAcctID as input.
   OperationID: AddStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AutoMatchStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoMatchStatement
   Description: Used for Automated Bank Reconciliation
Auto match statement Lines
   OperationID: AutoMatchStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoMatchStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoMatchStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BankStGetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BankStGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: BankStGetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BankStGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankStGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsUnconvertedStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsUnconvertedStatement
   Description: Check for unconverted statement
   OperationID: IsUnconvertedStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsUnconvertedStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsUnconvertedStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateLine
   Description: Call this method before calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method creates the CashBDtl record and any other records
required to call the business object.
   OperationID: CreateLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateManualLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateManualLine
   Description: This method creates the CashBDtl record and any other records
required to call the business object.
   OperationID: CreateManualLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateManualLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateManualLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMatchedLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMatchedLink
   Description: Used for conversion from old Bank Statement
   OperationID: UpdateMatchedLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMatchedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMatchedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenDocument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenDocument
   Description: Use this method to open Payments/Cash receipts for non-matched
Bank Statement lines
   OperationID: OpenDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NewDocumentWithUpdateStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NewDocumentWithUpdateStatement
   Description: Create Payments/Cash receipts for non-matched Bank Statement lines
   OperationID: NewDocumentWithUpdateStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NewDocumentWithUpdateStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NewDocumentWithUpdateStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewDocuments
   Description: Used for Automated Bank Reconciliation
Use this method to create Payments/Cash receipts for non-matched
Bank Statement lines
   OperationID: CreateNewDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateNewCashMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateNewCashMove
   Description: Used for Automated Bank Reconciliation
   OperationID: GenerateNewCashMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNewCashMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCashMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatement
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImporMultiStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImporMultiStatement
   Description: Import Multi-Bank Statement file
   OperationID: ImporMultiStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImporMultiStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImporMultiStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatementContinue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatementContinue
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file. Continue processing.
Importing of Bank Statement file could be interrupted by question message throwed to UI.
   OperationID: ImportStatementContinue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatementContinue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementContinue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatementDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatementDelete
   Description: Delete Bank Statement file.
   OperationID: ImportStatementDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatementDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewFiscalPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFiscalPer
   OperationID: GetNewFiscalPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetStatement
   Description: Get Statement.  Call this method when the user enters the Statement#.
It is similar to GetByID in functionality.
   OperationID: GetStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchDocument2Line(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchDocument2Line
   Description: Used for Automated Bank Reconciliation
Match Transaction 2 statement Line.
   OperationID: MatchDocument2Line
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchDocument2Line_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchDocument2Line_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDocDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDocDiscount
   Description: Used for Automated Bank Reconciliation
   OperationID: OnChangeDocDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDocDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDocDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofApplyDate
   Description: This method should be called before the apply date has been updated.
   OperationID: OnChangeofApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranDocTypeId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranDocTypeId
   Description: Sets default values when the TranDocTypeID changes
   OperationID: OnChangeTranDocTypeId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMXRecDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMXRecDate
   Description: Used to validate new Reconciled Date.
   OperationID: OnChangingMXRecDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMXRecDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMXRecDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDocClosingBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDocClosingBalance
   Description: Sets default values when Document Closing Balance is changes
   OperationID: OnChangingDocClosingBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDocClosingBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDocClosingBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshCashBDtlAuto(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshCashBDtlAuto
   Description: This method similar to RefreshCashBDtl but uses for auto bank reconciliation
   OperationID: RefreshCashBDtlAuto
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshCashBDtlAuto_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCashBDtlAuto_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshCashBDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshCashBDtl
   Description: Call this method after calling other business objects like
Cash Receipts, PaymentEntry, Bank Adjustment etc.
This method updates the CashBDtl record with the
data from other business objects.
   OperationID: RefreshCashBDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshCashBDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCashBDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshRatesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshRatesList
   Description: Refresh Rates.
   OperationID: RefreshRatesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRemittanceInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRemittanceInfo
   Description: (Auto bank reconciliation) load remittance info dataset
   OperationID: GetRemittanceInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRemittanceInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRemittanceInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProcessStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetProcessStatus
   Description: Returns Statement status
   OperationID: GetProcessStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProcessStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProcessStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveDocuments
   Description: Used for Automated Bank Reconciliation
   OperationID: RetrieveDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectBank
   Description: Select a Bank.
   OperationID: SelectBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockGroup
   Description: Lock Group by Bank Account ID
   OperationID: LockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchDocument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchDocument
   Description: Used for Automated Bank Reconciliation
Unmatch single document.
   OperationID: UnmatchDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchDocuments
   Description: Used for Automated Bank Reconciliation
   OperationID: UnmatchDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnSelectBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnSelectBank
   Description: Unlocks the group record locked by group name pcBankAcctID and by the user DCD-USERID.
   OperationID: UnSelectBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnSelectBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockStatement
   Description: Unlocks the bank statement
   OperationID: UnlockStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAPPay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAPPay
   Description: Delete obsolete Check
   OperationID: UpdateAPPay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAPPay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAPPay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllowPostStatement(epicorHeaders = None):
   """  
   Summary: Invoke method AllowPostStatement
   OperationID: AllowPostStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowPostStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNextCashBookNum(epicorHeaders = None):
   """  
   Summary: Invoke method GetNextCashBookNum
   Description: Get next CashBookNum.
   OperationID: GetNextCashBookNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextCashBookNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ReCalcAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReCalcAmount
   Description: Used for Automated Bank Reconciliation
   OperationID: ReCalcAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReCalcAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReCalcAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetBalances(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetBalances
   Description: Used for Automated Bank Reconciliation
Set balances amounts.
   OperationID: SetBalances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetBalances_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetBalances_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_enableAddNewStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method enableAddNewStatement
   Description: Method to determine the existence of a non posted Statement within the current bank account id.
   OperationID: enableAddNewStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/enableAddNewStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/enableAddNewStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExtractInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExtractInvoices
   Description: Extracts Invoice numbers from text
   OperationID: ExtractInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExtractInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtractInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseText
   Description: Parse text using Regular Expressions
   OperationID: ParseText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SplitKeywords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SplitKeywords
   Description: Split keys string into string array
   OperationID: SplitKeywords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SplitKeywords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SplitKeywords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConcatenateKeywords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConcatenateKeywords
   Description: Concatenate keys array into string
   OperationID: ConcatenateKeywords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConcatenateKeywords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConcatenateKeywords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsUnverifiedTransfers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsUnverifiedTransfers
   Description: Checks if there are any unposted transfers to or from this bank created from automatic bank reconciliation,
or if there are any uncleared posted transfers which are not already loaded as posible transfers for that statement line.
   OperationID: ExistsUnverifiedTransfers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsUnverifiedTransfers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsUnverifiedTransfers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPartnerInfoChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPartnerInfoChanged
   Description: Tries to recognize partner using transaction code, partner ID (XRef), partner bank code, partner bank account.
   OperationID: OnPartnerInfoChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPartnerInfoChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartnerInfoChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPartnerNameChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPartnerNameChanged
   Description: Tries to recognize partner using partner ID (XRef).
   OperationID: OnPartnerNameChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPartnerNameChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPartnerNameChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshTranCodeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshTranCodeList
   OperationID: RefreshTranCodeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshTranCodeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshTranCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPeriodThresholdDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPeriodThresholdDate
   OperationID: GetPeriodThresholdDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPeriodThresholdDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriodThresholdDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StorePartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StorePartner
   Description: Stores Partner
   OperationID: StorePartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StorePartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StorePartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartnerExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartnerExists
   Description: Search partner by Partner name
   OperationID: PartnerExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartnerExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartnerExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearSuggestion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearSuggestion
   Description: Clear suggestion from documents for specified line.
   OperationID: ClearSuggestion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearSuggestion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearSuggestion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReLoadBatchSubLedgerDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReLoadBatchSubLedgerDocs
   OperationID: ReLoadBatchSubLedgerDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReLoadBatchSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReLoadBatchSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddMissingBankBatchSubLedgerDoc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMissingBankBatchSubLedgerDoc
   OperationID: AddMissingBankBatchSubLedgerDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMissingBankBatchSubLedgerDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingBankBatchSubLedgerDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddMissingBatchedSubLedgerDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMissingBatchedSubLedgerDocs
   OperationID: AddMissingBatchedSubLedgerDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMissingBatchedSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingBatchedSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSubLedgerDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSubLedgerDocs
   Description: Check if SubLedgerDocs was modified outside AutoBankRec.
   OperationID: CheckSubLedgerDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsExistingSearchIDForPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsExistingSearchIDForPartner
   OperationID: IsExistingSearchIDForPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsExistingSearchIDForPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsExistingSearchIDForPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTolerance
   OperationID: CheckTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransactionCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransactionCodes
   Description: Get Transaction Code list
   OperationID: GetTransactionCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransactionCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDocumentList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDocumentList
   Description: Used for Automated Bank Reconciliation
Get documents with manual legal number entry.
   OperationID: GetDocumentList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDocumentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDocumentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasLinkedReverseLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasLinkedReverseLines
   Description: Check whether exists matched reversed
   OperationID: HasLinkedReverseLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasLinkedReverseLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasLinkedReverseLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchLinkedReverseLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchLinkedReverseLines
   OperationID: UnmatchLinkedReverseLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchLinkedReverseLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchLinkedReverseLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecognizePartners(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecognizePartners
   Description: Used for Automated Bank Reconciliation
Recognize partners in statement lines
   OperationID: RecognizePartners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecognizePartners_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecognizePartners_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindObsoleteReceiptsPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindObsoleteReceiptsPayments
   Description: The method 1. finds and deletes obsolete payments (created in statement, but not matched)
2. finds obsolete receipts (with NO customer)
   OperationID: FindObsoleteReceiptsPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindObsoleteReceiptsPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindObsoleteReceiptsPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExtendedProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExtendedProperties
   Description: Get Amounts Extended properties
   OperationID: GetExtendedProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExtendedProperties_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedProperties_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegNumDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegNumDefaults
   Description: This method will return a record in the LegalNumGenOpts data table if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetLegNumDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegNumDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegNumDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsAutomaticVoiding(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAutomaticVoiding
   Description: Determines whether legal number configuration for bank statement is automatic voiding for a the specified date.
   OperationID: IsAutomaticVoiding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAutomaticVoiding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutomaticVoiding_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the Bank Statement.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectBankLockGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectBankLockGroups
   Description: Select a Bank.
   OperationID: SelectBankLockGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectBankLockGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectBankLockGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankInfo
   Description: Gets Bank account info.
   OperationID: GetBankInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddNewStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewStatement
   Description: Add Statement.  It is similar to GetNewCashBHed in functionality.
It should be used to create CashBHed with BankAcctID as input.
   OperationID: AddNewStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatementSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatementSlip
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatementSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatementSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportStatementSlipContinue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportStatementSlipContinue
   Description: Used for Automated Bank Reconciliation
Import Bank Statement file
   OperationID: ImportStatementSlipContinue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportStatementSlipContinue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportStatementSlipContinue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BankStmtGetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BankStmtGetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: BankStmtGetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BankStmtGetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BankStmtGetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankStatement
   OperationID: GetBankStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBankSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBankSlip
   Description: Valid Bank slip check
   OperationID: CheckBankSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBankSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockStatement
   Description: Locks the bank statement
   OperationID: LockStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClosingDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClosingDate
   Description: This method should be called before the closing date has been updated.
   OperationID: OnChangeClosingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClosingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClosingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOpeningDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOpeningDate
   Description: This method should be called before the opening date has been updated.
   OperationID: OnChangeOpeningDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOpeningDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpeningDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClearDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClearDate
   Description: This method should be called before the clear date has been updated.
   OperationID: OnChangeClearDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClearDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClearDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostStatement
   Description: Prepost statement
   OperationID: PrePostStatement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostStatement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostStatement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SearchPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SearchPartner
   Description: Prepost statement
   OperationID: SearchPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SearchPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SearchPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshLineRatesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshLineRatesList
   Description: Refresh Rates.
   OperationID: RefreshLineRatesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshLineRatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshLineRatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashBHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashBHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashBHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashBHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashBHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashBHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashBFilterOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashBFilterOptions
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBFilterOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashBFilterOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBFilterOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSubLedgerDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSubLedgerDocs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSubLedgerDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSubLedgerDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSubLedgerDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashBDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashBDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashBDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashBDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashBDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashBDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashBDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashBDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMatchedDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMatchedDocuments
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMatchedDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMatchedDocuments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMatchedDocuments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AutoBankRecSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecExchangeRatesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankRecExchangeRatesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankRecMessagesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankRecMessagesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBFilterOptionsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBFilterOptionsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashBHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashBHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MatchedDocumentsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MatchedDocumentsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SubLedgerDocsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SubLedgerDocsRow] = obj["value"]
      pass

class Erp_Tablesets_BankRecExchangeRatesRow:
   def __init__(self, obj):
      self.CashBookLine:int = obj["CashBookLine"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankRecMessagesRow:
   def __init__(self, obj):
      self.MessageType:int = obj["MessageType"]
      self.MessageText:str = obj["MessageText"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashBookNum:int = obj["CashBookNum"]
      self.CashbookLine:int = obj["CashbookLine"]
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

class Erp_Tablesets_CashBDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LineNum:int = obj["LineNum"]
      """  Indicates the line number.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TranType:str = obj["TranType"]
      """  Identifies the type of transaction. Possible values are 'Banktran' for bank adjustments, 'manual' for manual A/P payments, 'appay' for A/P payments, 'prpay' for P/R payments, 'crpay' for cashreceipts which are entered in the Cash Receipt Entry program, 'payinv' for invoice cash receipts, 'deposit' for deposit cash receipts and 'mispay' for miscellaneous cash receipts.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user.  """  
      self.TranDate:str = obj["TranDate"]
      """  Indicates the transaction date in the statement line.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of transaction that is being applied.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Amount of transaction that is being applied.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is not entered by the user on each record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.LinkedTranType:str = obj["LinkedTranType"]
      """  Used on Bank Fees created from Bank Reconciliation, Identifies the type of transaction from was created. Possible values are 'Manual' for Manual A/P payments and ?PayInv? for Invoice Cash Receipt.  """  
      self.LinkedHeadNum:int = obj["LinkedHeadNum"]
      """  Used on Bank Fees, this field will be used to link Checks or AR Payments created from Bank Reconciliation.  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Partner:str = obj["Partner"]
      """  Indicates the name of the partner in the statement line.  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the ID of the partner. The bank uses this ID to specify the partner in the statement line.  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  Partner Number  """  
      self.PartnerType:int = obj["PartnerType"]
      """  Partner Type  """  
      self.DebitCreditMark:str = obj["DebitCreditMark"]
      """  Debit Credit Mark  """  
      self.ImportTranAmount:int = obj["ImportTranAmount"]
      """  Indicates the statement line amount in line currency.  """  
      self.ImportTranUnclearedAmount:int = obj["ImportTranUnclearedAmount"]
      """  Indicates the part of statement line amount that is not matched with an existing document in transaction currency.  """  
      self.ImportUnclearedAmount:int = obj["ImportUnclearedAmount"]
      """  Indicates the part of statement line amount that is not matched with an existing document.  """  
      self.ImportRpt1UnclearedAmount:int = obj["ImportRpt1UnclearedAmount"]
      """  Import Report 1 Uncleared Amount  """  
      self.ImportRpt2UnclearedAmount:int = obj["ImportRpt2UnclearedAmount"]
      """  Import Report 2 Uncleared Amount  """  
      self.ImportRpt3UnclearedAmount:int = obj["ImportRpt3UnclearedAmount"]
      """  Import Report 3 Uncleared Amount  """  
      self.ImportTranCurrency:str = obj["ImportTranCurrency"]
      """  Indicates the currency code for the transaction amount.  """  
      self.ImportBankAmount:int = obj["ImportBankAmount"]
      """  Indicates the statement line amount in bank currency.  """  
      self.ImportBankVariance:int = obj["ImportBankVariance"]
      """  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  """  
      self.ImportAmount:int = obj["ImportAmount"]
      """  Import Amount  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Indicates the exchange rate between the line currency and the bank currency.  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Indicates the statement line's status.  """  
      self.LineType:int = obj["LineType"]
      """  Indicates the type of the statement line.  """  
      self.LineDescription:str = obj["LineDescription"]
      """  Indicates the statement line transaction text.  """  
      self.DocumentList:str = obj["DocumentList"]
      """  Document List  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.ImportError:str = obj["ImportError"]
      """  The application displays here the information explaining why it did not perform correctly automatic line recognition, document creation or matching.  """  
      self.FilterByPartner:bool = obj["FilterByPartner"]
      """  Filter By Partner  """  
      self.ImportBankGainLoss:int = obj["ImportBankGainLoss"]
      """  Import Bank Gain Loss  """  
      self.ImportGainLoss:int = obj["ImportGainLoss"]
      """  Gain/Loss  """  
      self.ImportRpt1GainLoss:int = obj["ImportRpt1GainLoss"]
      """  Import Report 1 Gain Loss  """  
      self.ImportRpt2GainLoss:int = obj["ImportRpt2GainLoss"]
      """  Import Report 2 Gain Loss  """  
      self.ImportRpt3GainLoss:int = obj["ImportRpt3GainLoss"]
      """  Import Report 3 Gain Loss  """  
      self.BankTranType:str = obj["BankTranType"]
      """  BankTranType  """  
      self.ImportBankUnclearedAmount:int = obj["ImportBankUnclearedAmount"]
      """  Indicates the difference between the total line amount in bank currency and the applied transactions amount  """  
      self.ImportTranType:str = obj["ImportTranType"]
      """  Indicates the type of the transaction.  """  
      self.ImportTranCode:str = obj["ImportTranCode"]
      """  Indicates the code of the transaction.  """  
      self.TranRef:str = obj["TranRef"]
      """  Indicates the number of the business document related to the line which is known to the bank.  """  
      self.PartnerBank:str = obj["PartnerBank"]
      """  Indicates the code of the partner bank.  """  
      self.PartnerBankAcct:str = obj["PartnerBankAcct"]
      """  Indicates the account of the partner bank.  """  
      self.ReverseFlag:bool = obj["ReverseFlag"]
      """  This check box is selected if the line is of the Reverse Cash Receipt or Voided AP Payment type.  """  
      self.TotalChrgAmt:int = obj["TotalChrgAmt"]
      """  Indicates the total charges amount.  """  
      self.ChrgCurrCode:str = obj["ChrgCurrCode"]
      """  Indicates the currency code for the total charges.  """  
      self.RawData:str = obj["RawData"]
      """  RawData  """  
      self.MatchingInfo:str = obj["MatchingInfo"]
      """  Indicates the reference details of the invoice.  """  
      self.RemitData:str = obj["RemitData"]
      """  RemitData  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Bank Fee ID  """  
      self.TransferBankID:str = obj["TransferBankID"]
      """  Transfer Bank ID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.CreateMode:int = obj["CreateMode"]
      """  CreateMode  """  
      self.UserComment:str = obj["UserComment"]
      """  Add any comments in this field if required.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableMXRecDate:bool = obj["DisableMXRecDate"]
      """  Disable MXRecDate  """  
      self.DocTotalCandAmt:int = obj["DocTotalCandAmt"]
      self.DocTotalRemAmt:int = obj["DocTotalRemAmt"]
      self.DocTotalSelAmt:int = obj["DocTotalSelAmt"]
      self.DocumentsRefData:str = obj["DocumentsRefData"]
      """  Contains description of imported line with potential Invoices numbers list.  """  
      self.DspLineNum:str = obj["DspLineNum"]
      self.ExchangeRates:str = obj["ExchangeRates"]
      self.HeadNum:int = obj["HeadNum"]
      """  Stores HeadNum or TranNum value.  Used to call BankAdjEntry, PaymentEntry or CashRec - GetByID method.  """  
      self.ImportBankVarianceDsp:int = obj["ImportBankVarianceDsp"]
      """  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  """  
      self.ImportCreditAmount:int = obj["ImportCreditAmount"]
      self.ImportDebitAmount:int = obj["ImportDebitAmount"]
      self.ImportDspBankAmount:int = obj["ImportDspBankAmount"]
      self.ImportTranCodeDesc:str = obj["ImportTranCodeDesc"]
      """  Transaction Code Description  """  
      self.isCleared:bool = obj["isCleared"]
      self.NewDoc:bool = obj["NewDoc"]
      self.Reference:str = obj["Reference"]
      """  Reference field.  """  
      self.Rounding:int = obj["Rounding"]
      self.Rpt1TotalCandAmt:int = obj["Rpt1TotalCandAmt"]
      self.Rpt1TotalRemAmt:int = obj["Rpt1TotalRemAmt"]
      self.Rpt1TotalSelAmt:int = obj["Rpt1TotalSelAmt"]
      self.Rpt2TotalCandAmt:int = obj["Rpt2TotalCandAmt"]
      self.Rpt2TotalRemAmt:int = obj["Rpt2TotalRemAmt"]
      self.Rpt2TotalSelAmt:int = obj["Rpt2TotalSelAmt"]
      self.Rpt3TotalCandAmt:int = obj["Rpt3TotalCandAmt"]
      self.Rpt3TotalRemAmt:int = obj["Rpt3TotalRemAmt"]
      self.Rpt3TotalSelAmt:int = obj["Rpt3TotalSelAmt"]
      self.TotalCandAmt:int = obj["TotalCandAmt"]
      """  AP Clearing Total Candidates  """  
      self.TotalRemAmt:int = obj["TotalRemAmt"]
      """  AP Clearing Total Remaining  """  
      self.TotalSelAmt:int = obj["TotalSelAmt"]
      """  AP Clearing Total Selected  """  
      self.TranRef1:str = obj["TranRef1"]
      """  Transaction Reference 1  """  
      self.TranRef2:str = obj["TranRef2"]
      """  Transaction Reference 2  """  
      self.TranRef3:str = obj["TranRef3"]
      """  Transaction Reference 3  """  
      self.TranTemplateID:str = obj["TranTemplateID"]
      self.TranTypeDescription:str = obj["TranTypeDescription"]
      """  Tran Type description  """  
      self.DspUnallocatedAmount:int = obj["DspUnallocatedAmount"]
      self.DspUnallocatedCurrency:str = obj["DspUnallocatedCurrency"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBFilterOptionsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.LineType:int = obj["LineType"]
      """  Line Type  """  
      self.FilterAPInvoices:bool = obj["FilterAPInvoices"]
      """  Filter AP Invoices  """  
      self.FilterAPPay:bool = obj["FilterAPPay"]
      """  Filter AP Pay  """  
      self.FilterAPPI:bool = obj["FilterAPPI"]
      """  Filter AP Payment Instruments  """  
      self.FilterARPI:bool = obj["FilterARPI"]
      """  Filter AR Payment Instruments  """  
      self.FilterARInvoices:bool = obj["FilterARInvoices"]
      """  Filter AR Invoices  """  
      self.FilterBankAdj:bool = obj["FilterBankAdj"]
      """  Filter Bank Adjustments  """  
      self.FilterBankTran:bool = obj["FilterBankTran"]
      """  Filter Bank Transactions  """  
      self.FilterCRPay:bool = obj["FilterCRPay"]
      """  Filter Cash Receipts Payments  """  
      self.FilterRevAPPay:bool = obj["FilterRevAPPay"]
      """  Filter Reversed AP Payments  """  
      self.FilterRevCRPay:bool = obj["FilterRevCRPay"]
      """  Filter Reversed Cash Receipts Payments  """  
      self.FilterAll:bool = obj["FilterAll"]
      """  Filter All  """  
      self.FilterPayments:bool = obj["FilterPayments"]
      """  Filter Payments  """  
      self.FilterReceipts:bool = obj["FilterReceipts"]
      """  Filter Receipts  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilterPRPay:bool = obj["FilterPRPay"]
      """  Filter PR Pay  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashBookNum:int = obj["CashBookNum"]
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

class Erp_Tablesets_CashBHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Specifies the identifier for the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.Bankslip:int = obj["Bankslip"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.Description:str = obj["Description"]
      """  Indicates a description of the statement.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  Specifies opening balance for the statement.  """  
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      """  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  Specifies the opening date for transactions for the bank account.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  Specifies the closing amount for the statement.  """  
      self.DocClosingBalance:int = obj["DocClosingBalance"]
      """  The Closing Balance of the Bank Account.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  Specifies the closing date for transactions for the bank account.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year of the transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period of the transaction.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  The currency of the Bank Account  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Rpt1ClosingBalance:int = obj["Rpt1ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClosingBalance:int = obj["Rpt2ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClosingBalance:int = obj["Rpt3ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Specifies the date for which the statement applies.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocNetChange:int = obj["DocNetChange"]
      self.LineTotal:int = obj["LineTotal"]
      self.Variance:int = obj["Variance"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocVariance:int = obj["DocVariance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.APInterfaced:bool = obj["APInterfaced"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrName:str = obj["BaseCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseDocumentDesc:str = obj["BaseDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Specifies the identifier for the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.Bankslip:int = obj["Bankslip"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.Description:str = obj["Description"]
      """  Indicates a description of the statement.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  Specifies opening balance for the statement.  """  
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      """  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  Specifies the opening date for transactions for the bank account.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  Specifies the closing amount for the statement.  """  
      self.DocClosingBalance:int = obj["DocClosingBalance"]
      """  The Closing Balance of the Bank Account.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  Specifies the closing date for transactions for the bank account.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year of the transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period of the transaction.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  The currency of the Bank Account  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Rpt1ClosingBalance:int = obj["Rpt1ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClosingBalance:int = obj["Rpt2ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClosingBalance:int = obj["Rpt3ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Specifies the date for which the statement applies.  """  
      self.FilterToDate:str = obj["FilterToDate"]
      """  Filter To Date  """  
      self.FilterToDateToken:str = obj["FilterToDateToken"]
      """  Filter To Date Token  """  
      self.RetrieveStatus:int = obj["RetrieveStatus"]
      """  Retrieve Status  """  
      self.IncludePIPastClose:bool = obj["IncludePIPastClose"]
      """  Include PI Past Close  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.GrpCashReceipt:str = obj["GrpCashReceipt"]
      """  CashReceipt Group  """  
      self.GrpAPPay:str = obj["GrpAPPay"]
      """  AP Payment Group  """  
      self.GrpBankAdj:str = obj["GrpBankAdj"]
      """  Bank Adjustment Group  """  
      self.GrpBankTrans:str = obj["GrpBankTrans"]
      """  BankTransfer Group  """  
      self.RefNum:str = obj["RefNum"]
      """  RefNum  """  
      self.Info:str = obj["Info"]
      """  Info  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilterByLineType:bool = obj["FilterByLineType"]
      """  FilterByLineType  """  
      self.StatementDate:str = obj["StatementDate"]
      """  StatementDate  """  
      self.UseClosingDateCutoff:bool = obj["UseClosingDateCutoff"]
      """  UseClosingDateCutoff  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Select the transaction document type for the bank statement, if necessary.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  When the application assigns a legal number to the statement, it is displayed in this field. Refer to the Actions - Legal Numbers commands.  """  
      self.UnconvertedStatement:bool = obj["UnconvertedStatement"]
      """  UnconvertedStatement  """  
      self.StatementVersion:int = obj["StatementVersion"]
      """  StatementVersion  """  
      self.GrpARPI:str = obj["GrpARPI"]
      """  AR Payment Instrument Group  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.ThresholdDate:str = obj["ThresholdDate"]
      """  ThresholdDate  """  
      self.ClearDate:str = obj["ClearDate"]
      """  ClearDate  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.BankTranCodeList:str = obj["BankTranCodeList"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrName:str = obj["BaseCurrName"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseDocumentDesc:str = obj["BaseDocumentDesc"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentBalance:int = obj["CurrentBalance"]
      self.DefaultLineType:int = obj["DefaultLineType"]
      self.DocCurrentBalance:int = obj["DocCurrentBalance"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocNetChange:int = obj["DocNetChange"]
      self.DocNonReconciled:int = obj["DocNonReconciled"]
      self.DocReconciledBalance:int = obj["DocReconciledBalance"]
      self.DocVariance:int = obj["DocVariance"]
      self.DspDocRunningBal:int = obj["DspDocRunningBal"]
      self.DspDocVariance:int = obj["DspDocVariance"]
      self.DspRunningBal:int = obj["DspRunningBal"]
      self.DspVariance:int = obj["DspVariance"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock  """  
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.LineTotal:int = obj["LineTotal"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.NonReconciled:int = obj["NonReconciled"]
      self.ReconciledBalance:int = obj["ReconciledBalance"]
      self.Rpt1CurrentBalance:int = obj["Rpt1CurrentBalance"]
      self.Rpt1DspRunningBal:int = obj["Rpt1DspRunningBal"]
      self.Rpt1DspVariance:int = obj["Rpt1DspVariance"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1NonReconciled:int = obj["Rpt1NonReconciled"]
      self.Rpt1ReconciledBalance:int = obj["Rpt1ReconciledBalance"]
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2CurrentBalance:int = obj["Rpt2CurrentBalance"]
      self.Rpt2DspRunningBal:int = obj["Rpt2DspRunningBal"]
      self.Rpt2DspVariance:int = obj["Rpt2DspVariance"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2NonReconciled:int = obj["Rpt2NonReconciled"]
      self.Rpt2ReconciledBalance:int = obj["Rpt2ReconciledBalance"]
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3CurrentBalance:int = obj["Rpt3CurrentBalance"]
      self.Rpt3DspRunningBal:int = obj["Rpt3DspRunningBal"]
      self.Rpt3DspVariance:int = obj["Rpt3DspVariance"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3NonReconciled:int = obj["Rpt3NonReconciled"]
      self.Rpt3ReconciledBalance:int = obj["Rpt3ReconciledBalance"]
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranDocTypeDesc:str = obj["TranDocTypeDesc"]
      self.UpdateDates:int = obj["UpdateDates"]
      self.Variance:int = obj["Variance"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.BalanceStatus:str = obj["BalanceStatus"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      """  Standar Legal Number message when a new legal number is created.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MatchedDocumentsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.CashBookLine:int = obj["CashBookLine"]
      """  Cash Book Line Number.  """  
      self.MatchLineNum:int = obj["MatchLineNum"]
      """  Match Line Num  """  
      self.DocumentType:int = obj["DocumentType"]
      """  Indicates the type of the document matched to the line. The application uses  """  
      self.DocumentTypeMode:int = obj["DocumentTypeMode"]
      """  Document Type Mode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.Partner:str = obj["Partner"]
      """  Partner  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the name of the partner in the matched document.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Indicates the legal number of the matched document.  """  
      self.InternalNumber:str = obj["InternalNumber"]
      """  Indicates the internal number of the matched document.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Indicates the matched document amount in the document currency.  """  
      self.DocCurrency:str = obj["DocCurrency"]
      """  Indicates the matched document currency.  """  
      self.DocDate:str = obj["DocDate"]
      """  Indicates the matched document date.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Doc Discount Amount  """  
      self.TranAmount:int = obj["TranAmount"]
      """  Indicates the matched document amount in the bank currency.  """  
      self.TranCurrency:str = obj["TranCurrency"]
      """  Indicates the document currency  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Indicates the matched document amount in the bank currency.  """  
      self.BankCurrency:str = obj["BankCurrency"]
      """  Bank Currency  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankBatchRef:str = obj["BankBatchRef"]
      """  If the line was matched to a batch or a batch payment, this field indicates the number of the batch reference.  """  
      self.NewDoc:int = obj["NewDoc"]
      """  If this document was created either manually or automatically, this field indicates the document type.  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  SysRowID of matched document  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  If the line was matched to a batch or a batch payment, this field indicates the SysRowID of the batch.  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.Key1:str = obj["Key1"]
      """  Matched document reference key 1  """  
      self.Key2:str = obj["Key2"]
      """  Matched document reference key 2  """  
      self.Key3:str = obj["Key3"]
      """  Matched document reference key 3  """  
      self.MasterTypeMode:int = obj["MasterTypeMode"]
      self.Selected:bool = obj["Selected"]
      self.BankBatchID:str = obj["BankBatchID"]
      self.CreateMode:bool = obj["CreateMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SubLedgerDocsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.DocumentType:int = obj["DocumentType"]
      """  Document Type  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.CashBookLine:int = obj["CashBookLine"]
      """  Cash Book Line Number.  """  
      self.DocumentTypeMode:int = obj["DocumentTypeMode"]
      """  Document Type Mode  """  
      self.Partner:str = obj["Partner"]
      """  Indicates the partner ID.  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the partner name.  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  Partner Number  """  
      self.DocumentStatus:bool = obj["DocumentStatus"]
      """  Document Status  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Indicates the legal number of the unmatched document.  """  
      self.InternalNumber:str = obj["InternalNumber"]
      """  Internal Number  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Indicates the unmatched document amount in the document currency.  """  
      self.DocCurrency:str = obj["DocCurrency"]
      """  Indicates the unmatched document currency.  """  
      self.DocDate:str = obj["DocDate"]
      """  Indicates the unmatched document date.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Indicates the document amount in bank currency.  """  
      self.BankCurrency:str = obj["BankCurrency"]
      """  Indicates a bank currency code.  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SuggestedForLines:str = obj["SuggestedForLines"]
      """  Suggested For Lines  """  
      self.BankBatchRef:str = obj["BankBatchRef"]
      """  Indicates the refrence number of the batch.  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  SysRowID of the unmatched document  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  Indicates the SysRowID of the batch.  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.Key2:str = obj["Key2"]
      """  SubLedger document reference key 2  """  
      self.Key3:str = obj["Key3"]
      """  SubLedger document reference key 3  """  
      self.QSInternalNumber:str = obj["QSInternalNumber"]
      self.Ranged:bool = obj["Ranged"]
      self.Selected:bool = obj["Selected"]
      self.ShouldBeHidden:bool = obj["ShouldBeHidden"]
      self.Suggested:bool = obj["Suggested"]
      self.BankBatchID:str = obj["BankBatchID"]
      self.Key1:str = obj["Key1"]
      """  SubLedger document reference key 1  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddMissingBankBatchSubLedgerDoc_input:
   """ Required : 
   cashBookNum
   bankAcctID
   bankBatchRef
   """  
   def __init__(self, obj):
      self.cashBookNum:int = obj["cashBookNum"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.bankBatchRef:str = obj["bankBatchRef"]
      pass

class AddMissingBankBatchSubLedgerDoc_output:
   def __init__(self, obj):
      pass

class AddMissingBatchedSubLedgerDocs_input:
   """ Required : 
   cashBookNum
   bankAcctID
   bankBatchRef
   """  
   def __init__(self, obj):
      self.cashBookNum:int = obj["cashBookNum"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.bankBatchRef:str = obj["bankBatchRef"]
      pass

class AddMissingBatchedSubLedgerDocs_output:
   def __init__(self, obj):
      pass

class AddNewStatement_input:
   """ Required : 
   ipBankAcctID
   ipFiscalYear
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank Account ID of the statement.  """  
      self.ipFiscalYear      #schema had no properties on an object.
      """  Fiscal Year.  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class AddNewStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddStatement_input:
   """ Required : 
   pcBankAcctID
   ds
   statementDate
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Bank Account ID of the statement.  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.statementDate:str = obj["statementDate"]
      """  Opening date of statement (Default null).  """  
      pass

class AddStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AllowPostStatement_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class AssignLegalNumber_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank account identifier.  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash Book number.  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLegalNumMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AutoMatchStatement_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class AutoMatchStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BankStGetLegalNumGenOpts_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash Book number  """  
      pass

class BankStGetLegalNumGenOpts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class BankStmtGetLegalNumGenOpts_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash Book number  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class BankStmtGetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
      pass

      """  output parameters  """  

class CheckBankSlip_input:
   """ Required : 
   ipBankAcctID
   ipFiscalYear
   ipBankSlip
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account ID  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipBankSlip:int = obj["ipBankSlip"]
      """  Bank slip  """  
      pass

class CheckBankSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCashBookNum:int = obj["parameters"]
      self.opUnconverted:bool = obj["opUnconverted"]
      self.opLegalNumber:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   iBankAcctID
   iFiscalYear
   iFiscalYearSuffix
   iBankSlip
   iFiscalCalendarID
   """  
   def __init__(self, obj):
      self.iBankAcctID:str = obj["iBankAcctID"]
      """  BankAcctID  """  
      self.iFiscalYear:int = obj["iFiscalYear"]
      """  FiscalYear  """  
      self.iFiscalYearSuffix:str = obj["iFiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.iBankSlip:int = obj["iBankSlip"]
      """  BankSlip  """  
      self.iFiscalCalendarID:str = obj["iFiscalCalendarID"]
      """  FiscalCalendarID  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckSubLedgerDocs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class CheckSubLedgerDocs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTolerance_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipLineNum
   ipMode
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Book  """  
      self.ipLineNum:int = obj["ipLineNum"]
      """  Line No  """  
      self.ipMode:int = obj["ipMode"]
      """  Mode  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class CheckTolerance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ClearSuggestion_input:
   """ Required : 
   ipBankAcctID
   ipCashBookNum
   ipCashBookLine
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      self.ipCashBookLine:int = obj["ipCashBookLine"]
      pass

class ClearSuggestion_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ConcatenateKeywords_input:
   """ Required : 
   keys
   """  
   def __init__(self, obj):
      self.keys:str = obj["keys"]
      """  Keys array  """  
      pass

class ConcatenateKeywords_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Concatenated string  """  
      pass

class CreateLine_input:
   """ Required : 
   pcLineType
   pdCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.pcLineType:str = obj["pcLineType"]
      """  Line Type.  For example, Manual, MisPay, PayInv, Deposit, APPay, PRPay, CRPay, BankTran, APPIPay and ARPIPay  """  
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  Cash book number  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class CreateLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.piCashBookLine:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateManualLine_input:
   """ Required : 
   ipLineType
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipLineType:str = obj["ipLineType"]
      """  Line Type  """  
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash book number  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class CreateManualLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCashBookLine:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateNewDocuments_input:
   """ Required : 
   ipLineType
   ipCashBook
   ipLinesList
   ds
   """  
   def __init__(self, obj):
      self.ipLineType:int = obj["ipLineType"]
      """  Line Type  """  
      self.ipCashBook:int = obj["ipCashBook"]
      """  Cash book number  """  
      self.ipLinesList:str = obj["ipLinesList"]
      """  Lines for which documents should be created  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class CreateNewDocuments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLastNewDocNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   cashBookNum
   """  
   def __init__(self, obj):
      self.cashBookNum:int = obj["cashBookNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BankRecBankAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BankAcctID:str = obj["BankAcctID"]
      self.Description:str = obj["Description"]
      self.CheckingAccount:str = obj["CheckingAccount"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.AutoStatementImport:bool = obj["AutoStatementImport"]
      self.AutoRetrieve:bool = obj["AutoRetrieve"]
      self.FilterByLine:bool = obj["FilterByLine"]
      self.AutoMatch:bool = obj["AutoMatch"]
      self.BankClosed:bool = obj["BankClosed"]
      self.IBANCode:str = obj["IBANCode"]
      self.Tolerance:int = obj["Tolerance"]
      self.TranTemplateID:str = obj["TranTemplateID"]
      self.PayrollCheckingAccount:bool = obj["PayrollCheckingAccount"]
      self.EnableAddNewStatement:bool = obj["EnableAddNewStatement"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankRecBankAcctTableset:
   def __init__(self, obj):
      self.BankRecBankAcct:list[Erp_Tablesets_BankRecBankAcctRow] = obj["BankRecBankAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankRecExchangeRatesRow:
   def __init__(self, obj):
      self.CashBookLine:int = obj["CashBookLine"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankRecMessagesRow:
   def __init__(self, obj):
      self.MessageType:int = obj["MessageType"]
      self.MessageText:str = obj["MessageText"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankRecRemittanceInfoTableset:
   def __init__(self, obj):
      self.RemittanceInfo:list[Erp_Tablesets_RemittanceInfoRow] = obj["RemittanceInfo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankRecTableset:
   def __init__(self, obj):
      self.CashBHed:list[Erp_Tablesets_CashBHedRow] = obj["CashBHed"]
      self.CashBHedAttch:list[Erp_Tablesets_CashBHedAttchRow] = obj["CashBHedAttch"]
      self.CashBFilterOptions:list[Erp_Tablesets_CashBFilterOptionsRow] = obj["CashBFilterOptions"]
      self.SubLedgerDocs:list[Erp_Tablesets_SubLedgerDocsRow] = obj["SubLedgerDocs"]
      self.CashBDtl:list[Erp_Tablesets_CashBDtlRow] = obj["CashBDtl"]
      self.CashBDtlAttch:list[Erp_Tablesets_CashBDtlAttchRow] = obj["CashBDtlAttch"]
      self.MatchedDocuments:list[Erp_Tablesets_MatchedDocumentsRow] = obj["MatchedDocuments"]
      self.BankRecExchangeRates:list[Erp_Tablesets_BankRecExchangeRatesRow] = obj["BankRecExchangeRates"]
      self.BankRecMessages:list[Erp_Tablesets_BankRecMessagesRow] = obj["BankRecMessages"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashBDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashBookNum:int = obj["CashBookNum"]
      self.CashbookLine:int = obj["CashbookLine"]
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

class Erp_Tablesets_CashBDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LineNum:int = obj["LineNum"]
      """  Indicates the line number.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TranType:str = obj["TranType"]
      """  Identifies the type of transaction. Possible values are 'Banktran' for bank adjustments, 'manual' for manual A/P payments, 'appay' for A/P payments, 'prpay' for P/R payments, 'crpay' for cashreceipts which are entered in the Cash Receipt Entry program, 'payinv' for invoice cash receipts, 'deposit' for deposit cash receipts and 'mispay' for miscellaneous cash receipts.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user.  """  
      self.TranDate:str = obj["TranDate"]
      """  Indicates the transaction date in the statement line.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Amount of transaction that is being applied.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Amount of transaction that is being applied.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix. This is not entered by the user on each record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.LinkedTranType:str = obj["LinkedTranType"]
      """  Used on Bank Fees created from Bank Reconciliation, Identifies the type of transaction from was created. Possible values are 'Manual' for Manual A/P payments and ?PayInv? for Invoice Cash Receipt.  """  
      self.LinkedHeadNum:int = obj["LinkedHeadNum"]
      """  Used on Bank Fees, this field will be used to link Checks or AR Payments created from Bank Reconciliation.  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Partner:str = obj["Partner"]
      """  Indicates the name of the partner in the statement line.  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the ID of the partner. The bank uses this ID to specify the partner in the statement line.  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  Partner Number  """  
      self.PartnerType:int = obj["PartnerType"]
      """  Partner Type  """  
      self.DebitCreditMark:str = obj["DebitCreditMark"]
      """  Debit Credit Mark  """  
      self.ImportTranAmount:int = obj["ImportTranAmount"]
      """  Indicates the statement line amount in line currency.  """  
      self.ImportTranUnclearedAmount:int = obj["ImportTranUnclearedAmount"]
      """  Indicates the part of statement line amount that is not matched with an existing document in transaction currency.  """  
      self.ImportUnclearedAmount:int = obj["ImportUnclearedAmount"]
      """  Indicates the part of statement line amount that is not matched with an existing document.  """  
      self.ImportRpt1UnclearedAmount:int = obj["ImportRpt1UnclearedAmount"]
      """  Import Report 1 Uncleared Amount  """  
      self.ImportRpt2UnclearedAmount:int = obj["ImportRpt2UnclearedAmount"]
      """  Import Report 2 Uncleared Amount  """  
      self.ImportRpt3UnclearedAmount:int = obj["ImportRpt3UnclearedAmount"]
      """  Import Report 3 Uncleared Amount  """  
      self.ImportTranCurrency:str = obj["ImportTranCurrency"]
      """  Indicates the currency code for the transaction amount.  """  
      self.ImportBankAmount:int = obj["ImportBankAmount"]
      """  Indicates the statement line amount in bank currency.  """  
      self.ImportBankVariance:int = obj["ImportBankVariance"]
      """  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  """  
      self.ImportAmount:int = obj["ImportAmount"]
      """  Import Amount  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Indicates the exchange rate between the line currency and the bank currency.  """  
      self.LineStatus:int = obj["LineStatus"]
      """  Indicates the statement line's status.  """  
      self.LineType:int = obj["LineType"]
      """  Indicates the type of the statement line.  """  
      self.LineDescription:str = obj["LineDescription"]
      """  Indicates the statement line transaction text.  """  
      self.DocumentList:str = obj["DocumentList"]
      """  Document List  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.ImportError:str = obj["ImportError"]
      """  The application displays here the information explaining why it did not perform correctly automatic line recognition, document creation or matching.  """  
      self.FilterByPartner:bool = obj["FilterByPartner"]
      """  Filter By Partner  """  
      self.ImportBankGainLoss:int = obj["ImportBankGainLoss"]
      """  Import Bank Gain Loss  """  
      self.ImportGainLoss:int = obj["ImportGainLoss"]
      """  Gain/Loss  """  
      self.ImportRpt1GainLoss:int = obj["ImportRpt1GainLoss"]
      """  Import Report 1 Gain Loss  """  
      self.ImportRpt2GainLoss:int = obj["ImportRpt2GainLoss"]
      """  Import Report 2 Gain Loss  """  
      self.ImportRpt3GainLoss:int = obj["ImportRpt3GainLoss"]
      """  Import Report 3 Gain Loss  """  
      self.BankTranType:str = obj["BankTranType"]
      """  BankTranType  """  
      self.ImportBankUnclearedAmount:int = obj["ImportBankUnclearedAmount"]
      """  Indicates the difference between the total line amount in bank currency and the applied transactions amount  """  
      self.ImportTranType:str = obj["ImportTranType"]
      """  Indicates the type of the transaction.  """  
      self.ImportTranCode:str = obj["ImportTranCode"]
      """  Indicates the code of the transaction.  """  
      self.TranRef:str = obj["TranRef"]
      """  Indicates the number of the business document related to the line which is known to the bank.  """  
      self.PartnerBank:str = obj["PartnerBank"]
      """  Indicates the code of the partner bank.  """  
      self.PartnerBankAcct:str = obj["PartnerBankAcct"]
      """  Indicates the account of the partner bank.  """  
      self.ReverseFlag:bool = obj["ReverseFlag"]
      """  This check box is selected if the line is of the Reverse Cash Receipt or Voided AP Payment type.  """  
      self.TotalChrgAmt:int = obj["TotalChrgAmt"]
      """  Indicates the total charges amount.  """  
      self.ChrgCurrCode:str = obj["ChrgCurrCode"]
      """  Indicates the currency code for the total charges.  """  
      self.RawData:str = obj["RawData"]
      """  RawData  """  
      self.MatchingInfo:str = obj["MatchingInfo"]
      """  Indicates the reference details of the invoice.  """  
      self.RemitData:str = obj["RemitData"]
      """  RemitData  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      """  Bank Fee ID  """  
      self.TransferBankID:str = obj["TransferBankID"]
      """  Transfer Bank ID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.CreateMode:int = obj["CreateMode"]
      """  CreateMode  """  
      self.UserComment:str = obj["UserComment"]
      """  Add any comments in this field if required.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableMXRecDate:bool = obj["DisableMXRecDate"]
      """  Disable MXRecDate  """  
      self.DocTotalCandAmt:int = obj["DocTotalCandAmt"]
      self.DocTotalRemAmt:int = obj["DocTotalRemAmt"]
      self.DocTotalSelAmt:int = obj["DocTotalSelAmt"]
      self.DocumentsRefData:str = obj["DocumentsRefData"]
      """  Contains description of imported line with potential Invoices numbers list.  """  
      self.DspLineNum:str = obj["DspLineNum"]
      self.ExchangeRates:str = obj["ExchangeRates"]
      self.HeadNum:int = obj["HeadNum"]
      """  Stores HeadNum or TranNum value.  Used to call BankAdjEntry, PaymentEntry or CashRec - GetByID method.  """  
      self.ImportBankVarianceDsp:int = obj["ImportBankVarianceDsp"]
      """  Indicates the difference between the amount of the currently selected statement line and the total amount of transactions currently selected for  """  
      self.ImportCreditAmount:int = obj["ImportCreditAmount"]
      self.ImportDebitAmount:int = obj["ImportDebitAmount"]
      self.ImportDspBankAmount:int = obj["ImportDspBankAmount"]
      self.ImportTranCodeDesc:str = obj["ImportTranCodeDesc"]
      """  Transaction Code Description  """  
      self.isCleared:bool = obj["isCleared"]
      self.NewDoc:bool = obj["NewDoc"]
      self.Reference:str = obj["Reference"]
      """  Reference field.  """  
      self.Rounding:int = obj["Rounding"]
      self.Rpt1TotalCandAmt:int = obj["Rpt1TotalCandAmt"]
      self.Rpt1TotalRemAmt:int = obj["Rpt1TotalRemAmt"]
      self.Rpt1TotalSelAmt:int = obj["Rpt1TotalSelAmt"]
      self.Rpt2TotalCandAmt:int = obj["Rpt2TotalCandAmt"]
      self.Rpt2TotalRemAmt:int = obj["Rpt2TotalRemAmt"]
      self.Rpt2TotalSelAmt:int = obj["Rpt2TotalSelAmt"]
      self.Rpt3TotalCandAmt:int = obj["Rpt3TotalCandAmt"]
      self.Rpt3TotalRemAmt:int = obj["Rpt3TotalRemAmt"]
      self.Rpt3TotalSelAmt:int = obj["Rpt3TotalSelAmt"]
      self.TotalCandAmt:int = obj["TotalCandAmt"]
      """  AP Clearing Total Candidates  """  
      self.TotalRemAmt:int = obj["TotalRemAmt"]
      """  AP Clearing Total Remaining  """  
      self.TotalSelAmt:int = obj["TotalSelAmt"]
      """  AP Clearing Total Selected  """  
      self.TranRef1:str = obj["TranRef1"]
      """  Transaction Reference 1  """  
      self.TranRef2:str = obj["TranRef2"]
      """  Transaction Reference 2  """  
      self.TranRef3:str = obj["TranRef3"]
      """  Transaction Reference 3  """  
      self.TranTemplateID:str = obj["TranTemplateID"]
      self.TranTypeDescription:str = obj["TranTypeDescription"]
      """  Tran Type description  """  
      self.DspUnallocatedAmount:int = obj["DspUnallocatedAmount"]
      self.DspUnallocatedCurrency:str = obj["DspUnallocatedCurrency"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBFilterOptionsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.LineType:int = obj["LineType"]
      """  Line Type  """  
      self.FilterAPInvoices:bool = obj["FilterAPInvoices"]
      """  Filter AP Invoices  """  
      self.FilterAPPay:bool = obj["FilterAPPay"]
      """  Filter AP Pay  """  
      self.FilterAPPI:bool = obj["FilterAPPI"]
      """  Filter AP Payment Instruments  """  
      self.FilterARPI:bool = obj["FilterARPI"]
      """  Filter AR Payment Instruments  """  
      self.FilterARInvoices:bool = obj["FilterARInvoices"]
      """  Filter AR Invoices  """  
      self.FilterBankAdj:bool = obj["FilterBankAdj"]
      """  Filter Bank Adjustments  """  
      self.FilterBankTran:bool = obj["FilterBankTran"]
      """  Filter Bank Transactions  """  
      self.FilterCRPay:bool = obj["FilterCRPay"]
      """  Filter Cash Receipts Payments  """  
      self.FilterRevAPPay:bool = obj["FilterRevAPPay"]
      """  Filter Reversed AP Payments  """  
      self.FilterRevCRPay:bool = obj["FilterRevCRPay"]
      """  Filter Reversed Cash Receipts Payments  """  
      self.FilterAll:bool = obj["FilterAll"]
      """  Filter All  """  
      self.FilterPayments:bool = obj["FilterPayments"]
      """  Filter Payments  """  
      self.FilterReceipts:bool = obj["FilterReceipts"]
      """  Filter Receipts  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilterPRPay:bool = obj["FilterPRPay"]
      """  Filter PR Pay  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashBookNum:int = obj["CashBookNum"]
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

class Erp_Tablesets_CashBHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Specifies the identifier for the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.Bankslip:int = obj["Bankslip"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.Description:str = obj["Description"]
      """  Indicates a description of the statement.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  Specifies opening balance for the statement.  """  
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      """  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  Specifies the opening date for transactions for the bank account.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  Specifies the closing amount for the statement.  """  
      self.DocClosingBalance:int = obj["DocClosingBalance"]
      """  The Closing Balance of the Bank Account.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  Specifies the closing date for transactions for the bank account.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year of the transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period of the transaction.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  The currency of the Bank Account  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Rpt1ClosingBalance:int = obj["Rpt1ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClosingBalance:int = obj["Rpt2ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClosingBalance:int = obj["Rpt3ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Specifies the date for which the statement applies.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocNetChange:int = obj["DocNetChange"]
      self.LineTotal:int = obj["LineTotal"]
      self.Variance:int = obj["Variance"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocVariance:int = obj["DocVariance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.APInterfaced:bool = obj["APInterfaced"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrName:str = obj["BaseCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseDocumentDesc:str = obj["BaseDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashBHedListTableset:
   def __init__(self, obj):
      self.CashBHedList:list[Erp_Tablesets_CashBHedListRow] = obj["CashBHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashBHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Specifies the identifier for the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed and uses its CashBookNum + 1. Not directly entered by the user.  """  
      self.Bankslip:int = obj["Bankslip"]
      """  When creating a new CashBHed, the next available # is assigned by the system.  The system generates a number by finding the last CashBHed of a Bank Account and a Fiscal Year and uses its Bankslip + 1. The user can override this number when no cashbook lines are available for this bankslip.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.Description:str = obj["Description"]
      """  Indicates a description of the statement.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  Specifies opening balance for the statement.  """  
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      """  The Opening Balance of the Bank Account.  When a Reconciliation is posted this field is set to the Closing Balance.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  Specifies the opening date for transactions for the bank account.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  Specifies the closing amount for the statement.  """  
      self.DocClosingBalance:int = obj["DocClosingBalance"]
      """  The Closing Balance of the Bank Account.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  Specifies the closing date for transactions for the bank account.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year of the transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period of the transaction.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  The currency of the Bank Account  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Check.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Rpt1ClosingBalance:int = obj["Rpt1ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClosingBalance:int = obj["Rpt2ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClosingBalance:int = obj["Rpt3ClosingBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Specifies the fiscal year suffix of the fiscal year during which the transactions occurred.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Specifies the date for which the statement applies.  """  
      self.FilterToDate:str = obj["FilterToDate"]
      """  Filter To Date  """  
      self.FilterToDateToken:str = obj["FilterToDateToken"]
      """  Filter To Date Token  """  
      self.RetrieveStatus:int = obj["RetrieveStatus"]
      """  Retrieve Status  """  
      self.IncludePIPastClose:bool = obj["IncludePIPastClose"]
      """  Include PI Past Close  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.GrpCashReceipt:str = obj["GrpCashReceipt"]
      """  CashReceipt Group  """  
      self.GrpAPPay:str = obj["GrpAPPay"]
      """  AP Payment Group  """  
      self.GrpBankAdj:str = obj["GrpBankAdj"]
      """  Bank Adjustment Group  """  
      self.GrpBankTrans:str = obj["GrpBankTrans"]
      """  BankTransfer Group  """  
      self.RefNum:str = obj["RefNum"]
      """  RefNum  """  
      self.Info:str = obj["Info"]
      """  Info  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FilterByLineType:bool = obj["FilterByLineType"]
      """  FilterByLineType  """  
      self.StatementDate:str = obj["StatementDate"]
      """  StatementDate  """  
      self.UseClosingDateCutoff:bool = obj["UseClosingDateCutoff"]
      """  UseClosingDateCutoff  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Select the transaction document type for the bank statement, if necessary.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  When the application assigns a legal number to the statement, it is displayed in this field. Refer to the Actions - Legal Numbers commands.  """  
      self.UnconvertedStatement:bool = obj["UnconvertedStatement"]
      """  UnconvertedStatement  """  
      self.StatementVersion:int = obj["StatementVersion"]
      """  StatementVersion  """  
      self.GrpARPI:str = obj["GrpARPI"]
      """  AR Payment Instrument Group  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.ThresholdDate:str = obj["ThresholdDate"]
      """  ThresholdDate  """  
      self.ClearDate:str = obj["ClearDate"]
      """  ClearDate  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.BankTranCodeList:str = obj["BankTranCodeList"]
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrName:str = obj["BaseCurrName"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseDocumentDesc:str = obj["BaseDocumentDesc"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentBalance:int = obj["CurrentBalance"]
      self.DefaultLineType:int = obj["DefaultLineType"]
      self.DocCurrentBalance:int = obj["DocCurrentBalance"]
      self.DocLineTotal:int = obj["DocLineTotal"]
      self.DocNetChange:int = obj["DocNetChange"]
      self.DocNonReconciled:int = obj["DocNonReconciled"]
      self.DocReconciledBalance:int = obj["DocReconciledBalance"]
      self.DocVariance:int = obj["DocVariance"]
      self.DspDocRunningBal:int = obj["DspDocRunningBal"]
      self.DspDocVariance:int = obj["DspDocVariance"]
      self.DspRunningBal:int = obj["DspRunningBal"]
      self.DspVariance:int = obj["DspVariance"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock  """  
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.LineTotal:int = obj["LineTotal"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: an invoice is already in review journal or in posting process  """  
      self.NonReconciled:int = obj["NonReconciled"]
      self.ReconciledBalance:int = obj["ReconciledBalance"]
      self.Rpt1CurrentBalance:int = obj["Rpt1CurrentBalance"]
      self.Rpt1DspRunningBal:int = obj["Rpt1DspRunningBal"]
      self.Rpt1DspVariance:int = obj["Rpt1DspVariance"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1NonReconciled:int = obj["Rpt1NonReconciled"]
      self.Rpt1ReconciledBalance:int = obj["Rpt1ReconciledBalance"]
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      self.Rpt2CurrentBalance:int = obj["Rpt2CurrentBalance"]
      self.Rpt2DspRunningBal:int = obj["Rpt2DspRunningBal"]
      self.Rpt2DspVariance:int = obj["Rpt2DspVariance"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2NonReconciled:int = obj["Rpt2NonReconciled"]
      self.Rpt2ReconciledBalance:int = obj["Rpt2ReconciledBalance"]
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      self.Rpt3CurrentBalance:int = obj["Rpt3CurrentBalance"]
      self.Rpt3DspRunningBal:int = obj["Rpt3DspRunningBal"]
      self.Rpt3DspVariance:int = obj["Rpt3DspVariance"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3NonReconciled:int = obj["Rpt3NonReconciled"]
      self.Rpt3ReconciledBalance:int = obj["Rpt3ReconciledBalance"]
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranDocTypeDesc:str = obj["TranDocTypeDesc"]
      self.UpdateDates:int = obj["UpdateDates"]
      self.Variance:int = obj["Variance"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.BalanceStatus:str = obj["BalanceStatus"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      """  Standar Legal Number message when a new legal number is created.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MatchedDocumentsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.CashBookLine:int = obj["CashBookLine"]
      """  Cash Book Line Number.  """  
      self.MatchLineNum:int = obj["MatchLineNum"]
      """  Match Line Num  """  
      self.DocumentType:int = obj["DocumentType"]
      """  Indicates the type of the document matched to the line. The application uses  """  
      self.DocumentTypeMode:int = obj["DocumentTypeMode"]
      """  Document Type Mode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.Partner:str = obj["Partner"]
      """  Partner  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the name of the partner in the matched document.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Indicates the legal number of the matched document.  """  
      self.InternalNumber:str = obj["InternalNumber"]
      """  Indicates the internal number of the matched document.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Indicates the matched document amount in the document currency.  """  
      self.DocCurrency:str = obj["DocCurrency"]
      """  Indicates the matched document currency.  """  
      self.DocDate:str = obj["DocDate"]
      """  Indicates the matched document date.  """  
      self.DocDiscountAmount:int = obj["DocDiscountAmount"]
      """  Doc Discount Amount  """  
      self.TranAmount:int = obj["TranAmount"]
      """  Indicates the matched document amount in the bank currency.  """  
      self.TranCurrency:str = obj["TranCurrency"]
      """  Indicates the document currency  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Indicates the matched document amount in the bank currency.  """  
      self.BankCurrency:str = obj["BankCurrency"]
      """  Bank Currency  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankBatchRef:str = obj["BankBatchRef"]
      """  If the line was matched to a batch or a batch payment, this field indicates the number of the batch reference.  """  
      self.NewDoc:int = obj["NewDoc"]
      """  If this document was created either manually or automatically, this field indicates the document type.  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  SysRowID of matched document  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  If the line was matched to a batch or a batch payment, this field indicates the SysRowID of the batch.  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.Key1:str = obj["Key1"]
      """  Matched document reference key 1  """  
      self.Key2:str = obj["Key2"]
      """  Matched document reference key 2  """  
      self.Key3:str = obj["Key3"]
      """  Matched document reference key 3  """  
      self.MasterTypeMode:int = obj["MasterTypeMode"]
      self.Selected:bool = obj["Selected"]
      self.BankBatchID:str = obj["BankBatchID"]
      self.CreateMode:bool = obj["CreateMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RemittanceInfoRow:
   def __init__(self, obj):
      self.TagCode:str = obj["TagCode"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SubLedgerDocsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash Book Number.  """  
      self.DocumentType:int = obj["DocumentType"]
      """  Document Type  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.CashBookLine:int = obj["CashBookLine"]
      """  Cash Book Line Number.  """  
      self.DocumentTypeMode:int = obj["DocumentTypeMode"]
      """  Document Type Mode  """  
      self.Partner:str = obj["Partner"]
      """  Indicates the partner ID.  """  
      self.PartnerName:str = obj["PartnerName"]
      """  Indicates the partner name.  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  Partner Number  """  
      self.DocumentStatus:bool = obj["DocumentStatus"]
      """  Document Status  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Indicates the legal number of the unmatched document.  """  
      self.InternalNumber:str = obj["InternalNumber"]
      """  Internal Number  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Indicates the unmatched document amount in the document currency.  """  
      self.DocCurrency:str = obj["DocCurrency"]
      """  Indicates the unmatched document currency.  """  
      self.DocDate:str = obj["DocDate"]
      """  Indicates the unmatched document date.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Indicates the document amount in bank currency.  """  
      self.BankCurrency:str = obj["BankCurrency"]
      """  Indicates a bank currency code.  """  
      self.GroupID:str = obj["GroupID"]
      """  Group ID  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SuggestedForLines:str = obj["SuggestedForLines"]
      """  Suggested For Lines  """  
      self.BankBatchRef:str = obj["BankBatchRef"]
      """  Indicates the refrence number of the batch.  """  
      self.ExternalSysRowID:str = obj["ExternalSysRowID"]
      """  SysRowID of the unmatched document  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  Indicates the SysRowID of the batch.  """  
      self.UserReference:str = obj["UserReference"]
      """  UserReference  """  
      self.Key2:str = obj["Key2"]
      """  SubLedger document reference key 2  """  
      self.Key3:str = obj["Key3"]
      """  SubLedger document reference key 3  """  
      self.QSInternalNumber:str = obj["QSInternalNumber"]
      self.Ranged:bool = obj["Ranged"]
      self.Selected:bool = obj["Selected"]
      self.ShouldBeHidden:bool = obj["ShouldBeHidden"]
      self.Suggested:bool = obj["Suggested"]
      self.BankBatchID:str = obj["BankBatchID"]
      self.Key1:str = obj["Key1"]
      """  SubLedger document reference key 1  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtBankRecTableset:
   def __init__(self, obj):
      self.CashBHed:list[Erp_Tablesets_CashBHedRow] = obj["CashBHed"]
      self.CashBHedAttch:list[Erp_Tablesets_CashBHedAttchRow] = obj["CashBHedAttch"]
      self.CashBFilterOptions:list[Erp_Tablesets_CashBFilterOptionsRow] = obj["CashBFilterOptions"]
      self.SubLedgerDocs:list[Erp_Tablesets_SubLedgerDocsRow] = obj["SubLedgerDocs"]
      self.CashBDtl:list[Erp_Tablesets_CashBDtlRow] = obj["CashBDtl"]
      self.CashBDtlAttch:list[Erp_Tablesets_CashBDtlAttchRow] = obj["CashBDtlAttch"]
      self.MatchedDocuments:list[Erp_Tablesets_MatchedDocumentsRow] = obj["MatchedDocuments"]
      self.BankRecExchangeRates:list[Erp_Tablesets_BankRecExchangeRatesRow] = obj["BankRecExchangeRates"]
      self.BankRecMessages:list[Erp_Tablesets_BankRecMessagesRow] = obj["BankRecMessages"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsUnverifiedTransfers_input:
   """ Required : 
   bankAcctID
   transferBankAcctID
   toDate
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  BankAcctID of bank to check to.  """  
      self.transferBankAcctID:str = obj["transferBankAcctID"]
      """  BankAcctID of second bank. Could be empty.  """  
      self.toDate:str = obj["toDate"]
      """  Maximum transaction date value  """  
      pass

class ExistsUnverifiedTransfers_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if any transfers found, otherwise false.  """  
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ExtractInvoices_input:
   """ Required : 
   textData
   paramCode
   """  
   def __init__(self, obj):
      self.textData:str = obj["textData"]
      """  Source text data  """  
      self.paramCode:str = obj["paramCode"]
      """  Code of parameters set  """  
      pass

class ExtractInvoices_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of found Invoices with a comma as separator  """  
      pass

class FindObsoleteReceiptsPayments_input:
   """ Required : 
   ipBankAcctID
   ipCashBookNum
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Current not posted cashbook  """  
      pass

class FindObsoleteReceiptsPayments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateNewCashMove_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class GenerateNewCashMove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBankInfo_input:
   """ Required : 
   ipBankAcctID
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account ID  """  
      pass

class GetBankInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecBankAcctTableset] = obj["returnObj"]
      pass

class GetBankStatement_input:
   """ Required : 
   ipBankAcctID
   ipFiscalYear
   ipBankSlip
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipBankSlip:int = obj["ipBankSlip"]
      """  Bank slip  """  
      pass

class GetBankStatement_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   cashBookNum
   """  
   def __init__(self, obj):
      self.cashBookNum:int = obj["cashBookNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDocumentList_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipLineNum
   ipTrandate
   ipLineType
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ipLineNum:int = obj["ipLineNum"]
      """  Line #  """  
      self.ipTrandate:str = obj["ipTrandate"]
      """  Line Date  """  
      self.ipLineType:int = obj["ipLineType"]
      """  Line Date  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class GetDocumentList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDocumentList:str = obj["parameters"]
      self.opTranDocTypeiD:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetExtendedProperties_input:
   """ Required : 
   ipTableList
   """  
   def __init__(self, obj):
      self.ipTableList:str = obj["ipTableList"]
      """  Tables list  """  
      pass

class GetExtendedProperties_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opExtProperties:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLegNumDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class GetLegNumDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
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
      self.returnObj:list[Erp_Tablesets_CashBHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCashBDtlAttch_input:
   """ Required : 
   ds
   cashBookNum
   cashbookLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashbookLine:int = obj["cashbookLine"]
      pass

class GetNewCashBDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashBDtl_input:
   """ Required : 
   ds
   cashBookNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.cashBookNum:int = obj["cashBookNum"]
      pass

class GetNewCashBDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashBFilterOptions_input:
   """ Required : 
   ds
   bankAcctID
   cashBookNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      pass

class GetNewCashBFilterOptions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashBHedAttch_input:
   """ Required : 
   ds
   cashBookNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.cashBookNum:int = obj["cashBookNum"]
      pass

class GetNewCashBHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashBHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class GetNewCashBHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFiscalPer_input:
   """ Required : 
   p_newdate
   """  
   def __init__(self, obj):
      self.p_newdate:str = obj["p_newdate"]
      pass

class GetNewFiscalPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.n_FiscalCalendarID:str = obj["parameters"]
      self.n_FiscalYear:int = obj["parameters"]
      self.n_FiscalYearSuffix:str = obj["parameters"]
      self.n_FiscalPeriod:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewMatchedDocuments_input:
   """ Required : 
   ds
   bankAcctID
   cashBookNum
   cashBookLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      pass

class GetNewMatchedDocuments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSubLedgerDocs_input:
   """ Required : 
   ds
   bankAcctID
   cashBookNum
   documentType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.documentType:int = obj["documentType"]
      pass

class GetNewSubLedgerDocs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNextCashBookNum_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  decimal  """  
      pass

class GetPeriodThresholdDate_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      pass

class GetPeriodThresholdDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opThresholdDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetProcessStatus_input:
   """ Required : 
   ipBankAcct
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      pass

class GetProcessStatus_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRemittanceInfo_input:
   """ Required : 
   pdCashBookNum
   ipCashBookLine
   """  
   def __init__(self, obj):
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  Cash book number  """  
      self.ipCashBookLine:int = obj["ipCashBookLine"]
      """  CashBookLine from CashbDtl datatable  """  
      pass

class GetRemittanceInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecRemittanceInfoTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseCashBHed
   whereClauseCashBHedAttch
   whereClauseCashBFilterOptions
   whereClauseSubLedgerDocs
   whereClauseCashBDtl
   whereClauseCashBDtlAttch
   whereClauseMatchedDocuments
   whereClauseBankRecExchangeRates
   whereClauseBankRecMessages
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashBHed:str = obj["whereClauseCashBHed"]
      self.whereClauseCashBHedAttch:str = obj["whereClauseCashBHedAttch"]
      self.whereClauseCashBFilterOptions:str = obj["whereClauseCashBFilterOptions"]
      self.whereClauseSubLedgerDocs:str = obj["whereClauseSubLedgerDocs"]
      self.whereClauseCashBDtl:str = obj["whereClauseCashBDtl"]
      self.whereClauseCashBDtlAttch:str = obj["whereClauseCashBDtlAttch"]
      self.whereClauseMatchedDocuments:str = obj["whereClauseMatchedDocuments"]
      self.whereClauseBankRecExchangeRates:str = obj["whereClauseBankRecExchangeRates"]
      self.whereClauseBankRecMessages:str = obj["whereClauseBankRecMessages"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetStatement_input:
   """ Required : 
   pcBankAcctID
   piFiscalYear
   piBankSlip
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Bank Account ID of the statement.  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year of the statement  """  
      self.piBankSlip:int = obj["piBankSlip"]
      """  Bank slip#  """  
      pass

class GetStatement_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class GetTransactionCodes_input:
   """ Required : 
   tranTemplateID
   """  
   def __init__(self, obj):
      self.tranTemplateID:str = obj["tranTemplateID"]
      """  Template ID  """  
      pass

class GetTransactionCodes_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class HasLinkedReverseLines_input:
   """ Required : 
   bankAcctID
   cashBookNum
   cashBookLine
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  BankAcctID  """  
      self.cashBookNum:int = obj["cashBookNum"]
      """  CashBookNum  """  
      self.cashBookLine:int = obj["cashBookLine"]
      """  CashBookLine  """  
      pass

class HasLinkedReverseLines_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  0 - no revese lines, 1 - exists reverse lines, 2 - new document with reverse lines  """  
      pass

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

class ImporMultiStatement_input:
   """ Required : 
   EFTHeadUID
   importFile
   instanceTaskNum
   logFile
   """  
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface ID  """  
      self.importFile:str = obj["importFile"]
      """  Import file name (Server path)  """  
      self.instanceTaskNum:int = obj["instanceTaskNum"]
      """  Task Number  """  
      self.logFile:str = obj["logFile"]
      """  Log file path  """  
      pass

class ImporMultiStatement_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ImportStatementContinue_input:
   """ Required : 
   bankAcct
   importFile
   ds
   """  
   def __init__(self, obj):
      self.bankAcct:str = obj["bankAcct"]
      """  Bank Account  """  
      self.importFile:str = obj["importFile"]
      """  Import file name  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class ImportStatementContinue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.msgList:str = obj["parameters"]
      self.opCashBookNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class ImportStatementDelete_input:
   """ Required : 
   importFile
   """  
   def __init__(self, obj):
      self.importFile:str = obj["importFile"]
      """  Server Import file path  """  
      pass

class ImportStatementDelete_output:
   def __init__(self, obj):
      pass

class ImportStatementSlipContinue_input:
   """ Required : 
   bankAcct
   importFile
   ds
   """  
   def __init__(self, obj):
      self.bankAcct:str = obj["bankAcct"]
      """  Bank Account  """  
      self.importFile:str = obj["importFile"]
      """  Import file name  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class ImportStatementSlipContinue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.msgList:str = obj["parameters"]
      self.opFiscalYear:int = obj["parameters"]
      self.opBankslip:int = obj["parameters"]
      pass

      """  output parameters  """  

class ImportStatementSlip_input:
   """ Required : 
   bankAcct
   importFile
   ds
   """  
   def __init__(self, obj):
      self.bankAcct:str = obj["bankAcct"]
      """  Bank Account  """  
      self.importFile:str = obj["importFile"]
      """  Import file name  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class ImportStatementSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.msgList:str = obj["parameters"]
      self.opFiscalYear:int = obj["parameters"]
      self.opBankslip:int = obj["parameters"]
      pass

      """  output parameters  """  

class ImportStatement_input:
   """ Required : 
   bankAcct
   importFile
   ds
   """  
   def __init__(self, obj):
      self.bankAcct:str = obj["bankAcct"]
      """  Bank Account  """  
      self.importFile:str = obj["importFile"]
      """  Import file name  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class ImportStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.msgList:str = obj["parameters"]
      self.opCashBookNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class IsAutomaticVoiding_input:
   """ Required : 
   tranDocTypeID
   date
   """  
   def __init__(self, obj):
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      """  Transaction document type identifier.  """  
      self.date:str = obj["date"]
      """  Date to get legal number configuration.  """  
      pass

class IsAutomaticVoiding_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if legal number configuration exists and s automatic voiding for the specified date; otherwise, `false`.  """  
      pass

class IsExistingSearchIDForPartner_input:
   """ Required : 
   searchID
   partnerNum
   partnerID
   partnerType
   """  
   def __init__(self, obj):
      self.searchID:str = obj["searchID"]
      self.partnerNum:int = obj["partnerNum"]
      self.partnerID:str = obj["partnerID"]
      self.partnerType:int = obj["partnerType"]
      pass

class IsExistingSearchIDForPartner_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsUnconvertedStatement_input:
   """ Required : 
   bankAcctID
   fiscalYear
   bankslip
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      self.fiscalYear:int = obj["fiscalYear"]
      """  FiscalYear  """  
      self.bankslip:int = obj["bankslip"]
      """  Bankslip  """  
      pass

class IsUnconvertedStatement_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class LockGroup_input:
   """ Required : 
   bankAcctID
   fiscalYear
   bankSlip
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.bankSlip:int = obj["bankSlip"]
      pass

class LockGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool  """  
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class LockStatement_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class LockStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MatchDocument2Line_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipLineNum
   ipMatchMode
   ipDocument
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ipLineNum:int = obj["ipLineNum"]
      """  Line #  """  
      self.ipMatchMode:int = obj["ipMatchMode"]
      """  Manual match  """  
      self.ipDocument:str = obj["ipDocument"]
      """  TranDocTypeID  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class MatchDocument2Line_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class NewDocumentWithUpdateStatement_input:
   """ Required : 
   lineType
   cashBookNum
   cashBookLine
   ds
   """  
   def __init__(self, obj):
      self.lineType:int = obj["lineType"]
      """  Line Type  """  
      self.cashBookNum:int = obj["cashBookNum"]
      """  Cash book number  """  
      self.cashBookLine:int = obj["cashBookLine"]
      """  Line for which document should be created  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class NewDocumentWithUpdateStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLastNewDocNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeClearDate_input:
   """ Required : 
   ipCashBookNum
   ipClearDate
   ds
   """  
   def __init__(self, obj):
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  CashBookNum from CashBHed datatable  """  
      self.ipClearDate:str = obj["ipClearDate"]
      """  Clear Date  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangeClearDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeClosingDate_input:
   """ Required : 
   ipCashBookNum
   ipClosingDate
   ds
   """  
   def __init__(self, obj):
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  CashBookNum from CashBHed datatable  """  
      self.ipClosingDate:str = obj["ipClosingDate"]
      """  Closing Date  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangeClosingDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDocDiscount_input:
   """ Required : 
   ipDiscAmount
   ipTranCurrency
   ipTranRateGroup
   ipTranDate
   ipDocCurrency
   ipBankCurrency
   """  
   def __init__(self, obj):
      self.ipDiscAmount:int = obj["ipDiscAmount"]
      """  Doc Currency amount  """  
      self.ipTranCurrency:str = obj["ipTranCurrency"]
      """  Operation Currency  """  
      self.ipTranRateGroup:str = obj["ipTranRateGroup"]
      """  Operation Rate group  """  
      self.ipTranDate:str = obj["ipTranDate"]
      """  Operation Date  """  
      self.ipDocCurrency:str = obj["ipDocCurrency"]
      """  Doc Currency  """  
      self.ipBankCurrency:str = obj["ipBankCurrency"]
      """  Doc Currency  """  
      pass

class OnChangeDocDiscount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTranAmount:int = obj["parameters"]
      self.opBankAmount:int = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeOpeningDate_input:
   """ Required : 
   ipCashBookNum
   ipOpeningDate
   ds
   """  
   def __init__(self, obj):
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  CashBookNum from CashBHed datatable  """  
      self.ipOpeningDate:str = obj["ipOpeningDate"]
      """  Opening Date  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangeOpeningDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranDocTypeId_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangeTranDocTypeId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofApplyDate_input:
   """ Required : 
   pdCashBookNum
   newApplyDate
   ds
   """  
   def __init__(self, obj):
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  CashBookNum from CashBHed datatable  """  
      self.newApplyDate:str = obj["newApplyDate"]
      """  Proposed Apply Date.  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangeofApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDocClosingBalance_input:
   """ Required : 
   proposedDocClosingBalance
   ds
   """  
   def __init__(self, obj):
      self.proposedDocClosingBalance:int = obj["proposedDocClosingBalance"]
      """  Proposed Closing Balance  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnChangingDocClosingBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMXRecDate_input:
   """ Required : 
   plMXRecDate
   pdCashBookNum
   piCashBookLine
   """  
   def __init__(self, obj):
      self.plMXRecDate:str = obj["plMXRecDate"]
      """  New Reconciled Date  """  
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  CashBookNum from CashbDtl datatable  """  
      self.piCashBookLine:int = obj["piCashBookLine"]
      """  CashBookLine from CashbDtl datatable  """  
      pass

class OnChangingMXRecDate_output:
   def __init__(self, obj):
      pass

class OnPartnerInfoChanged_input:
   """ Required : 
   bankAcctID
   cashBookNum
   cashBookLine
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnPartnerInfoChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnPartnerNameChanged_input:
   """ Required : 
   bankAcctID
   cashBookNum
   cashBookLine
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class OnPartnerNameChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OpenDocument_input:
   """ Required : 
   ipLineType
   ipCashBook
   ipLineNum
   """  
   def __init__(self, obj):
      self.ipLineType:int = obj["ipLineType"]
      """  Line Type  """  
      self.ipCashBook:int = obj["ipCashBook"]
      """  Cash book number  """  
      self.ipLineNum:int = obj["ipLineNum"]
      """  Line for which document should be opened  """  
      pass

class OpenDocument_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opGroupID:str = obj["parameters"]
      self.opDocNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class ParseText_input:
   """ Required : 
   pattern
   textData
   """  
   def __init__(self, obj):
      self.pattern:str = obj["pattern"]
      """  Pattern  """  
      self.textData:str = obj["textData"]
      """  Text data  """  
      pass

class ParseText_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of found blocks with a comma as separator  """  
      pass

class PartnerExists_input:
   """ Required : 
   partnerType
   partnerName
   """  
   def __init__(self, obj):
      self.partnerType:int = obj["partnerType"]
      self.partnerName:str = obj["partnerName"]
      pass

class PartnerExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class PrePostStatement_input:
   """ Required : 
   ipBankAcctID
   ipCashBookNum
   ipDocVariance
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account ID  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash book  """  
      self.ipDocVariance:int = obj["ipDocVariance"]
      """  Variance  """  
      pass

class PrePostStatement_output:
   def __init__(self, obj):
      pass

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class ReCalcAmount_input:
   """ Required : 
   ipAmount
   ipRateGroup
   ipFromCurrency
   ipToCurrency
   ipExchangeDate
   ipFromDoc
   """  
   def __init__(self, obj):
      self.ipAmount:int = obj["ipAmount"]
      """  Amount to convert  """  
      self.ipRateGroup:str = obj["ipRateGroup"]
      """  Rate Group  """  
      self.ipFromCurrency:str = obj["ipFromCurrency"]
      """  From Currency  """  
      self.ipToCurrency:str = obj["ipToCurrency"]
      """  To Currency  """  
      self.ipExchangeDate:str = obj["ipExchangeDate"]
      """  Exchange Date  """  
      self.ipFromDoc:bool = obj["ipFromDoc"]
      """  Document Currency  """  
      pass

class ReCalcAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opAmount:int = obj["parameters"]
      pass

      """  output parameters  """  

class ReLoadBatchSubLedgerDocs_input:
   """ Required : 
   BankAcctID
   CashBookNum
   ds
   """  
   def __init__(self, obj):
      self.BankAcctID:str = obj["BankAcctID"]
      self.CashBookNum:int = obj["CashBookNum"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class ReLoadBatchSubLedgerDocs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecognizePartners_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class RecognizePartners_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshCashBDtlAuto_input:
   """ Required : 
   pdCashBookNum
   piCashBookLine
   piDocNum
   """  
   def __init__(self, obj):
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  Cash book number  """  
      self.piCashBookLine:int = obj["piCashBookLine"]
      """  CashBookLine from CashbDtl datatable  """  
      self.piDocNum:int = obj["piDocNum"]
      """  Document number  """  
      pass

class RefreshCashBDtlAuto_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class RefreshCashBDtl_input:
   """ Required : 
   pdCashBookNum
   piCashBookLine
   """  
   def __init__(self, obj):
      self.pdCashBookNum:int = obj["pdCashBookNum"]
      """  Cash book number  """  
      self.piCashBookLine:int = obj["piCashBookLine"]
      """  CashBookLine from CashbDtl datatable  """  
      pass

class RefreshCashBDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class RefreshLineRatesList_input:
   """ Required : 
   ipCashBookLine
   ipDate
   ipRateGrpCode
   ipTranCurrency
   ds
   """  
   def __init__(self, obj):
      self.ipCashBookLine:int = obj["ipCashBookLine"]
      """  Line  """  
      self.ipDate:str = obj["ipDate"]
      """  Date  """  
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Group Code  """  
      self.ipTranCurrency:str = obj["ipTranCurrency"]
      """  Currency  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class RefreshLineRatesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshRatesList_input:
   """ Required : 
   ipDate
   ipRateGrpCode
   ipTranCurrency
   """  
   def __init__(self, obj):
      self.ipDate:str = obj["ipDate"]
      """  Date  """  
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Group Code  """  
      self.ipTranCurrency:str = obj["ipTranCurrency"]
      """  Currency  """  
      pass

class RefreshRatesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRatesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class RefreshTranCodeList_input:
   """ Required : 
   ipBankAcctId
   ipCashBookNum
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctId:str = obj["ipBankAcctId"]
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class RefreshTranCodeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrieveDocuments_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipCashBookLine
   ipDocType
   ipToDate
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ipCashBookLine:int = obj["ipCashBookLine"]
      """  Line  """  
      self.ipDocType:int = obj["ipDocType"]
      """  Document Type  """  
      self.ipToDate:str = obj["ipToDate"]
      """  To Date  """  
      pass

class RetrieveDocuments_output:
   def __init__(self, obj):
      pass

class SearchPartner_input:
   """ Required : 
   ipLineType
   ipPartner
   ipPartnerName
   """  
   def __init__(self, obj):
      self.ipLineType:int = obj["ipLineType"]
      """  Statement Line Type  """  
      self.ipPartner:str = obj["ipPartner"]
      """  Partner  """  
      self.ipPartnerName:str = obj["ipPartnerName"]
      """  Partner Name  """  
      pass

class SearchPartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartnerType:int = obj["parameters"]
      self.opPartnerNum:int = obj["parameters"]
      self.opPartnerID:str = obj["parameters"]
      self.opPartnerBank:str = obj["parameters"]
      self.opPartnerBankAcct:str = obj["parameters"]
      self.opStorePartner:bool = obj["opStorePartner"]
      self.opImportError:str = obj["parameters"]
      pass

      """  output parameters  """  

class SelectBankLockGroups_input:
   """ Required : 
   ipBankAcctID
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      """  Bank account ID  """  
      pass

class SelectBankLockGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFiscalYear:int = obj["parameters"]
      self.opBankslip:int = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      self.opAutoStatementImport:bool = obj["opAutoStatementImport"]
      self.opEnableAddNewStatement:bool = obj["opEnableAddNewStatement"]
      pass

      """  output parameters  """  

class SelectBank_input:
   """ Required : 
   pcBankAcctID
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Bank account ID  """  
      pass

class SelectBank_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecBankAcctTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pdCashBookNum:int = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetBalances_input:
   """ Required : 
   ipDocClosingBalance
   ipClosingDate
   cashBHedRow
   """  
   def __init__(self, obj):
      self.ipDocClosingBalance:int = obj["ipDocClosingBalance"]
      """  DocClosingBalance  """  
      self.ipClosingDate:str = obj["ipClosingDate"]
      """  Closing Date  """  
      self.cashBHedRow:list[Erp_Tablesets_CashBHedRow] = obj["cashBHedRow"]
      pass

class SetBalances_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cashBHedRow:list[Erp_Tablesets_CashBHedRow] = obj["cashBHedRow"]
      pass

      """  output parameters  """  

class SplitKeywords_input:
   """ Required : 
   keys
   """  
   def __init__(self, obj):
      self.keys:str = obj["keys"]
      """  String contained keys with separators  """  
      pass

class SplitKeywords_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.listKeys:str = obj["parameters"]
      pass

      """  output parameters  """  

class StorePartner_input:
   """ Required : 
   ipPartnerNum
   ipPartnerID
   partnerType
   ipSearchID
   """  
   def __init__(self, obj):
      self.ipPartnerNum:int = obj["ipPartnerNum"]
      self.ipPartnerID:str = obj["ipPartnerID"]
      self.partnerType:int = obj["partnerType"]
      self.ipSearchID:str = obj["ipSearchID"]
      pass

class StorePartner_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UnSelectBank_input:
   """ Required : 
   pcBankAcctID
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Unlock the groups for Bank account ID  """  
      pass

class UnSelectBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plSuccess:bool = obj["plSuccess"]
      pass

      """  output parameters  """  

class UnlockStatement_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class UnlockStatement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnmatchDocument_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipLineNum
   ipDocRef
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank Account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cashbook num  """  
      self.ipLineNum:int = obj["ipLineNum"]
      """  Line #  """  
      self.ipDocRef:str = obj["ipDocRef"]
      """  Line #  """  
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class UnmatchDocument_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnmatchDocuments_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipLineNum
   unmatchLinkedReverseLines
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      self.ipLineNum:int = obj["ipLineNum"]
      self.unmatchLinkedReverseLines:bool = obj["unmatchLinkedReverseLines"]
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class UnmatchDocuments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnmatchLinkedReverseLines_input:
   """ Required : 
   bankAcctID
   cashBookNum
   cashBookLine
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      pass

class UnmatchLinkedReverseLines_output:
   def __init__(self, obj):
      pass

class UpdateAPPay_input:
   """ Required : 
   ipCashBookNum
   ipCashBookLine
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash book number  """  
      self.ipCashBookLine:int = obj["ipCashBookLine"]
      """  CashBookLine from CashbDtl datatable  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Document number  """  
      pass

class UpdateAPPay_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankRecTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankRecTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMatchedLink_input:
   """ Required : 
   company
   cashBookNum
   cashbookLine
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  CompanyID  """  
      self.cashBookNum:int = obj["cashBookNum"]
      """  CashBookNum  """  
      self.cashbookLine:int = obj["cashbookLine"]
      """  CashbookLine  """  
      pass

class UpdateMatchedLink_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankRecTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipBankAcct
   ipCashBookNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipBankAcct:str = obj["ipBankAcct"]
      """  Bank account  """  
      self.ipCashBookNum:int = obj["ipCashBookNum"]
      """  Cash Book number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankRecTableset] = obj["returnObj"]
      pass

class enableAddNewStatement_input:
   """ Required : 
   keyBankAcctID
   """  
   def __init__(self, obj):
      self.keyBankAcctID:str = obj["keyBankAcctID"]
      pass

class enableAddNewStatement_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

