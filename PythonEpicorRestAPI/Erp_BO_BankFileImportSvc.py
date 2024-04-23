import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BankFileImportSvc
# Description: BankFile class
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BankFileImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankFileImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankFileImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports",headers=creds) as resp:
           return await resp.json()

async def post_BankFileImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankFileImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankFileImports_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankFileImport item
   Description: Calls GetByID to retrieve the BankFileImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankFileImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankFileImports_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankFileImport for the service
   Description: Calls UpdateExt to update BankFileImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankFileImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashGrpImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankFileImports_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankFileImport item
   Description: Call UpdateExt to delete BankFileImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankFileImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankFileImports_Company_GroupID_CashHeadImports(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashHeadImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashHeadImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")/CashHeadImports",headers=creds) as resp:
           return await resp.json()

async def get_BankFileImports_Company_GroupID_CashHeadImports_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashHeadImport item
   Description: Calls GetByID to retrieve the CashHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/BankFileImports(" + Company + "," + GroupID + ")/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashHeadImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashHeadImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashHeadImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports",headers=creds) as resp:
           return await resp.json()

async def post_CashHeadImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashHeadImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashHeadImports_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashHeadImport item
   Description: Calls GetByID to retrieve the CashHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashHeadImports_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashHeadImport for the service
   Description: Calls UpdateExt to update CashHeadImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashHeadImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashHeadImports_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashHeadImport item
   Description: Call UpdateExt to delete CashHeadImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashHeadImports_Company_GroupID_HeadNum_CashDtlImports(Company, GroupID, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CashDtlImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CashDtlImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtlImports",headers=creds) as resp:
           return await resp.json()

async def get_CashHeadImports_Company_GroupID_HeadNum_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashDtlImport item
   Description: Calls GetByID to retrieve the CashDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashHeadImports(" + Company + "," + GroupID + "," + HeadNum + ")/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def get_CashDtlImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CashDtlImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CashDtlImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports",headers=creds) as resp:
           return await resp.json()

async def post_CashDtlImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CashDtlImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CashDtlImport item
   Description: Calls GetByID to retrieve the CashDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CashDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CashDtlImport for the service
   Description: Calls UpdateExt to update CashDtlImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CashDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CashDtlImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CashDtlImports_Company_GroupID_HeadNum_InvoiceNum_InvoiceRef(Company, GroupID, HeadNum, InvoiceNum, InvoiceRef, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CashDtlImport item
   Description: Call UpdateExt to delete CashDtlImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CashDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceRef: Desc: InvoiceRef   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/CashDtlImports(" + Company + "," + GroupID + "," + HeadNum + "," + InvoiceNum + "," + InvoiceRef + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CashGrpImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCashGrpImport, whereClauseCashHeadImport, whereClauseCashDtlImport, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseCashGrpImport=" + whereClauseCashGrpImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashHeadImport=" + whereClauseCashHeadImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCashDtlImport=" + whereClauseCashDtlImport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeARInvSelApplyAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeARInvSelApplyAmt
   Description: Method to call when changing the apply amount on the invoice to match.
   OperationID: ChangeARInvSelApplyAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelApplyAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelApplyAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeARInvSelDocDiscAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeARInvSelDocDiscAmt
   Description: Method to call when changing the discount amount for the invoice to match.
   OperationID: ChangeARInvSelDocDiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelDocDiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelDocDiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeARInvSelSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeARInvSelSelected
   Description: Method to call when selecting or deselecting an invoice to match.
   OperationID: ChangeARInvSelSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeARInvSelSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeARInvSelSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashDtlImportDocDiscount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashDtlImportDocDiscount
   Description: Method to call when changing the discount on the payment detail.
   OperationID: ChangeCashDtlImportDocDiscount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportDocDiscount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportDocDiscount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashDtlImportDocTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashDtlImportDocTranAmt
   Description: Method to call when changing the tran amount on the payment detail.
   OperationID: ChangeCashDtlImportDocTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportDocTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportDocTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashDtlImportInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashDtlImportInvoiceNum
   Description: Method to call when changing the invoice number.
   OperationID: ChangeCashDtlImportInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashDtlImportInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashDtlImportInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashGrpImportBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashGrpImportBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeCashGrpImportBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashGrpImportBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashGrpImportBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashHeadImportCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashHeadImportCustID
   Description: Method to call when changing the customer.
   OperationID: ChangeCashHeadImportCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashHeadImportCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashHeadImportCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCashHeadSettlementExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCashHeadSettlementExRate
   Description: Method to call when changing the Settlement Exchange rate.
   OperationID: ChangeCashHeadSettlementExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCashHeadSettlementExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCashHeadSettlementExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePymtForInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePymtForInvoices
   Description: Create payments for selected invoices.
   OperationID: CreatePymtForInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePymtForInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePymtForInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCreditMemos(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCreditMemos
   Description: Delete Credit Memos
   OperationID: DeleteCreditMemos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCreditMemos_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeletePaymantsWithErrors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePaymantsWithErrors
   Description: Delete Paymants with errors
   OperationID: DeletePaymantsWithErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePaymantsWithErrors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePaymantsWithErrors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankFileImportParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankFileImportParam
   Description: Returns record in BankFileImportParam dataset
   OperationID: GetBankFileImportParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankFileImportParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankFileImportParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportBankFileExpress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportBankFileExpress
   OperationID: ImportBankFileExpress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBankFileExpress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBankFileExpress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetBankFileImportExpressGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetBankFileImportExpressGroup
   Description: Reset status of group in case payments are hanged in Generation of Posting status.
   OperationID: ResetBankFileImportExpressGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetBankFileImportExpressGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetBankFileImportExpressGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupInfo
   Description: Returns current status of Group
   OperationID: GetGroupInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTranTypeActiveRevision(epicorHeaders = None):
   """  
   Summary: Invoke method CheckTranTypeActiveRevision
   Description: Check AR Payment transaction Type: Active Revision, Send To RJ flag and PE Log
   OperationID: CheckTranTypeActiveRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTranTypeActiveRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportBankFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportBankFile
   Description: Imports a bank file
   OperationID: ImportBankFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportBankFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportBankFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchCHCashHeadImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchCHCashHeadImport
   Description: Method to call to match CashHeadImport record with invalid ISR Reference Number to invoices (for Switzerland).
   OperationID: MatchCHCashHeadImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchCHCashHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchCHCashHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchPayments
   Description: Method to call to automatically match the invoices, called after import
   OperationID: MatchPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessReceipts
   Description: Method to call to automatically process receipts
   OperationID: ProcessReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectInvoices
   Description: Read InvcHead records and create ARInvSel records if they meet the selection criteria.
   OperationID: SelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockGroup
   Description: Should be call before GetByID to lock the Group.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockGroup
   Description: Unlock the group.  Only user who locked the group can unlock it.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpImportNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpImportNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewCashGrpImportNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpImportNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpImportNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashGrpImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashGrpImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashGrpImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashGrpImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashGrpImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashHeadImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashHeadImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashHeadImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCashDtlImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCashDtlImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCashDtlImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCashDtlImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCashDtlImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashDtlImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashDtlImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashGrpImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashGrpImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashGrpImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CashHeadImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CashHeadImportRow] = obj["value"]
      pass

class Erp_Tablesets_CashDtlImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CheckRef:str = obj["CheckRef"]
      """  CheckRef  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  DocDiscount  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GLRefType:str = obj["GLRefType"]
      """  GLRefType  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  GLRefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  DebitNote  """  
      self.DNComments:str = obj["DNComments"]
      """  DNComments  """  
      self.DNAmount:int = obj["DNAmount"]
      """  DNAmount  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  DocDnAmount  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  DNCustNbr  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  RoundDiff  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Rpt1Discount  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Rpt2Discount  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Rpt3Discount  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Rpt1DnAmount  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Rpt2DnAmount  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Rpt3DnAmount  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Rpt1TranAmt  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Rpt2TranAmt  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Rpt3TranAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  WithholdAmt  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  DocWithholdAmt  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Rpt1WithholdAmt  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Rpt2WithholdAmt  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Rpt3WithholdAmt  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  SelfAssessAmt  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  DocSelfAssessAmt  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Rpt1SelfAssessAmt  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Rpt2SelfAssessAmt  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Rpt3SelfAssessAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Rpt1TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Rpt2TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Rpt3TaxAmt  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  RedStorno  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  TaxReceiptDate  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  TaxReceiptNo  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  WHTCertificateDate  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  WHTCertificateNo  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.GainLossType:str = obj["GainLossType"]
      """  GainLossType  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  ReverseGL  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  RevalueDate  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  RevalueBal  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  DocRevalueBal  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Rpt1RevalueBal  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Rpt2RevalueBal  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Rpt3RevalueBal  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MainSite:bool = obj["MainSite"]
      """  MainSite  """  
      self.SiteCode:str = obj["SiteCode"]
      """  SiteCode  """  
      self.BranchID:str = obj["BranchID"]
      """  BranchID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  TaxRemarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  NonDeductCode  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  NonDeductAmt  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  NonDeductDocAmt  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  NonDeductRpt1Amt  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  NonDeductRpt2Amt  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  NonDeductRpt3Amt  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.InvDueDate:str = obj["InvDueDate"]
      """  InvDueDate  """  
      self.ManualMatch:bool = obj["ManualMatch"]
      """  ManualMatch  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  WriteOffHeadNumRef  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  TaxableAdjustment  """  
      self.BankNetPay:int = obj["BankNetPay"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      self.DocNetPay:int = obj["DocNetPay"]
      self.InvPayStatus:str = obj["InvPayStatus"]
      self.DocRemainInvBal:int = obj["DocRemainInvBal"]
      self.InvOpenBalance:int = obj["InvOpenBalance"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.PIStatus:str = obj["PIStatus"]
      """  PIStatus  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  PIStatusGrp  """  
      self.PIType:str = obj["PIType"]
      """  PIType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      """  Currency.CurrencyCode of the currency that the bank account is denominated in.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      """  IBAN Code  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.PIStatus:str = obj["PIStatus"]
      """  PIStatus  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  PIStatusGrp  """  
      self.PIType:str = obj["PIType"]
      """  PIType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BankBatchID:str = obj["BankBatchID"]
      """  BankBatchID  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  ImportFileName  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.LockForChanges:bool = obj["LockForChanges"]
      self.ProcessButtonEnabled:bool = obj["ProcessButtonEnabled"]
      self.ProcessStatusDisplay:str = obj["ProcessStatusDisplay"]
      self.EnableMatchCMemoWithInv:bool = obj["EnableMatchCMemoWithInv"]
      """  Enable matching Credit Memo with Invoice  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.CheckRef:str = obj["CheckRef"]
      """  CheckRef  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  UnAppliedAmt  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  DocUnAppliedAmt  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  AppliedAmt  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  DocAppliedAmt  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  CreditMemoNum  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  CashBookNum  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  CashbookLine  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.ExternalID:str = obj["ExternalID"]
      """  ExternalID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  GLRefType  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  GLRefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  CardMemberName  """  
      self.CardNumber:str = obj["CardNumber"]
      """  CardNumber  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  ExpirationMonth  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  ExpirationYear  """  
      self.CardID:str = obj["CardID"]
      """  CardID  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  CardmemberReference  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  ProcessCard  """  
      self.CCAmount:int = obj["CCAmount"]
      """  CCAmount  """  
      self.CCFreight:int = obj["CCFreight"]
      """  CCFreight  """  
      self.CCTax:int = obj["CCTax"]
      """  CCTax  """  
      self.CCTotal:int = obj["CCTotal"]
      """  CCTotal  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  CCDocAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  CCDocFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  CCDocTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  CCDocTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  CCStreetAddr  """  
      self.CCZip:str = obj["CCZip"]
      """  CCZip  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Rpt1AppliedAmt  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Rpt2AppliedAmt  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Rpt3AppliedAmt  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Rpt1TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Rpt2TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Rpt3TaxAmt  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Rpt1TranAmt  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Rpt2TranAmt  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Rpt3TranAmt  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Rpt1UnAppliedAmt  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Rpt2UnAppliedAmt  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Rpt3UnAppliedAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  DocDepApplied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  Rpt1CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  Rpt2CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  Rpt3CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  Rpt1CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  Rpt2CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  Rpt3CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  Rpt1CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  Rpt2CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  Rpt3CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  Rpt1CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  Rpt2CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  Rpt3CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  ReadyToCalc  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  RecalcBeforePost  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  WithholdAmt  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  DocWithholdAmt  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Rpt1WithholdAmt  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Rpt2WithholdAmt  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Rpt3WithholdAmt  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  SelfAssessAmt  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  DocSelfAssessAmt  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Rpt1SelfAssessAmt  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Rpt2SelfAssessAmt  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Rpt3SelfAssessAmt  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  ReceiptCurrencyCode  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  ReceiptAmt  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  BankRcptExchangeRate  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  SettlementExchangeRate  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  CMCurrencyCode  """  
      self.CMAmount:int = obj["CMAmount"]
      """  CMAmount  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  ReverseRef  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  ReverseDate  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  TaxWhld  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  DiscountDate  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  TaxWhldCalc  """  
      self.ContractDate:str = obj["ContractDate"]
      """  ContractDate  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  UnallocatedAmt  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  DocUnallocatedAmt  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Rpt1UnallocatedAmt  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Rpt2UnallocatedAmt  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Rpt3UnallocatedAmt  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  ApplyHeadNum  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  AllocatedAmt  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  DocAllocatedAmt  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Rpt1AllocatedAmt  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Rpt2AllocatedAmt  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Rpt3AllocatedAmt  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.BankTranID:str = obj["BankTranID"]
      """  BankTranID  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MainSite:bool = obj["MainSite"]
      """  MainSite  """  
      self.SiteCode:str = obj["SiteCode"]
      """  SiteCode  """  
      self.BranchID:str = obj["BranchID"]
      """  BranchID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  TaxRemarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  NonDeductCode  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  NonDeductAmt  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  NonDeductDocAmt  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  NonDeductRpt1Amt  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  NonDeductRpt2Amt  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  NonDeductRpt3Amt  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  BankTransDate  """  
      self.CustNameFromFile:str = obj["CustNameFromFile"]
      """  CustNameFromFile  """  
      self.OCRNumber:str = obj["OCRNumber"]
      """  OCRNumber  """  
      self.ImportLineStatus:str = obj["ImportLineStatus"]
      """  ImportLineStatus  """  
      self.ImportLineError:str = obj["ImportLineError"]
      """  ImportLineError  """  
      self.DescFromImport:str = obj["DescFromImport"]
      """  DescFromImport  """  
      self.InvNumList:str = obj["InvNumList"]
      """  InvNumList  """  
      self.InvAmtList:str = obj["InvAmtList"]
      """  InvAmtList  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.ManualMatch:bool = obj["ManualMatch"]
      """  ManualMatch  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  CreditMemo  """  
      self.CMNum:int = obj["CMNum"]
      """  CMNum  """  
      self.CMDocAmount:int = obj["CMDocAmount"]
      """  CMDocAmount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.CHISRRefNumAvailableToChange:bool = obj["CHISRRefNumAvailableToChange"]
      """  CHISRRefNumAvailableToChange  """  
      self.BankBatchID:str = obj["BankBatchID"]
      """  BankBatchID  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  RcptCurAppliedAmt  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  RcptCurUnAppliedAmt  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  MXPaySupplementFlag  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MXOriginalCheckRef  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MXBankID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  ReversedReason  """  
      self.CCCity:str = obj["CCCity"]
      """  CCCity  """  
      self.CCState:str = obj["CCState"]
      """  CCState  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Adjustment  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  AdjustmentRef  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  AdjustmentReason  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  WriteOffAmount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACHTranCode  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  CustomerBankID  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  CustomerBankAcctNumber  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  CustomerBankIBANCode  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  CustomerBankNameOnAccount  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  CustomerBankAddress1  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  CustomerBankAddress2  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  CustomerBankAddress3  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  CustomerBankCity  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  CustomerBankState  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  CustomerBankPostalCode  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  CustomerBankCountryNum  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  CustomerBankName  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.CashRecGroupID:str = obj["CashRecGroupID"]
      """  Cash Rec Group ID  """  
      self.CashRecHeadNum:int = obj["CashRecHeadNum"]
      """  Cash Rec Head Num  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  RvJrnUID  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.NettingID:int = obj["NettingID"]
      """  NettingID  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  BankReceiptAmt  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.CHImportStatus:bool = obj["CHImportStatus"]
      """  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  """  
      self.EnableCust:bool = obj["EnableCust"]
      """  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  """  
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.LockForChanges:bool = obj["LockForChanges"]
      self.ProcessStatusDisplay:str = obj["ProcessStatusDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RcptCurrencyCurrSymbol:str = obj["RcptCurrencyCurrSymbol"]
      self.SettlementCurrencyCurrSymbol:str = obj["SettlementCurrencyCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeARInvSelApplyAmt_input:
   """ Required : 
   ProposedApplyAmt
   inInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedApplyAmt:int = obj["ProposedApplyAmt"]
      """  The proposed apply amount  """  
      self.inInvoiceNum:int = obj["inInvoiceNum"]
      """  The invoice number  """  
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

class ChangeARInvSelApplyAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeARInvSelDocDiscAmt_input:
   """ Required : 
   ProposedDocDiscAmt
   inInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedDocDiscAmt:int = obj["ProposedDocDiscAmt"]
      """  The proposed doc discount amount  """  
      self.inInvoiceNum:int = obj["inInvoiceNum"]
      """  The invoice number  """  
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

class ChangeARInvSelDocDiscAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeARInvSelSelected_input:
   """ Required : 
   ProposedSelected
   inInvoiceNum
   inTranDate
   inCreditMemo
   ds
   """  
   def __init__(self, obj):
      self.ProposedSelected:bool = obj["ProposedSelected"]
      """  The proposed selected value  """  
      self.inInvoiceNum:int = obj["inInvoiceNum"]
      """  The invoice number  """  
      self.inTranDate:str = obj["inTranDate"]
      """  The tran date  """  
      self.inCreditMemo:bool = obj["inCreditMemo"]
      """  Credit Memo  """  
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

class ChangeARInvSelSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashDtlImportDocDiscount_input:
   """ Required : 
   ProposedDocDiscount
   ds
   """  
   def __init__(self, obj):
      self.ProposedDocDiscount:int = obj["ProposedDocDiscount"]
      """  The proposed discount  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashDtlImportDocDiscount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashDtlImportDocTranAmt_input:
   """ Required : 
   ProposedDocTranAmt
   ds
   """  
   def __init__(self, obj):
      self.ProposedDocTranAmt:int = obj["ProposedDocTranAmt"]
      """  The proposed tran amt  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashDtlImportDocTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashDtlImportInvoiceNum_input:
   """ Required : 
   ProposedInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ProposedInvoiceNum:int = obj["ProposedInvoiceNum"]
      """  The proposed invoice number  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashDtlImportInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashGrpImportBankAcctID_input:
   """ Required : 
   ProposedBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ProposedBankAcctID:str = obj["ProposedBankAcctID"]
      """  The proposed bank account id  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashGrpImportBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashHeadImportCustID_input:
   """ Required : 
   ProposedCustID
   ds
   """  
   def __init__(self, obj):
      self.ProposedCustID:str = obj["ProposedCustID"]
      """  The proposed bank account id  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashHeadImportCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCashHeadSettlementExRate_input:
   """ Required : 
   proposedExRate
   ds
   """  
   def __init__(self, obj):
      self.proposedExRate:int = obj["proposedExRate"]
      """  The proposed settlement exchange rate  """  
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class ChangeCashHeadSettlementExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTranTypeActiveRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NoActiveRevision:bool = obj["NoActiveRevision"]
      self.SendToReviewJournal:bool = obj["SendToReviewJournal"]
      self.PELogEnabled:bool = obj["PELogEnabled"]
      pass

      """  output parameters  """  

class CreatePymtForInvoices_input:
   """ Required : 
   pcGroupID
   pcHeadNum
   ds
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  Cash Receipt Group ID  """  
      self.pcHeadNum:int = obj["pcHeadNum"]
      """  Imported payment to create the line for  """  
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

class CreatePymtForInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFileImportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvSelTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteCreditMemos_output:
   def __init__(self, obj):
      pass

class DeletePaymantsWithErrors_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      pass

class DeletePaymantsWithErrors_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARInvSelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  """  
      self.UnappliedCash:bool = obj["UnappliedCash"]
      """  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  """  
      self.DeferredRevenue:bool = obj["DeferredRevenue"]
      """  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.FOB:str = obj["FOB"]
      """  Defaults from sales order ORderHed.FOB  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Once posted, maintenance is not allowed.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DepositCredit:int = obj["DepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.DocDepositCredit:int = obj["DocDepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.RefCancelled:int = obj["RefCancelled"]
      """  Value of this field is reference to invoice which has been cancelled by current invoice.  """  
      self.RefCancelledBy:int = obj["RefCancelledBy"]
      """  Value of this field is reference to invoice that cancelled this invoice.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.PayDiscDate:str = obj["PayDiscDate"]
      """  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  """  
      self.PayDiscAmt:int = obj["PayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.DocPayDiscAmt:int = obj["DocPayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  """  
      self.RMANum:int = obj["RMANum"]
      """   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that the invoice is relate to.  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.DNComments:str = obj["DNComments"]
      """  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  """  
      self.DebitNote:bool = obj["DebitNote"]
      """   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  This is populated from ShipHead.CustNum representing the Sold To customer.  """  
      self.Consolidated:bool = obj["Consolidated"]
      """  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  """  
      self.BillToInvoiceAddress:bool = obj["BillToInvoiceAddress"]
      """  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  """  
      self.SoldToInvoiceAddress:bool = obj["SoldToInvoiceAddress"]
      """  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.RepComm1:int = obj["RepComm1"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm2:int = obj["RepComm2"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm3:int = obj["RepComm3"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm4:int = obj["RepComm4"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm5:int = obj["RepComm5"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepSales1:int = obj["RepSales1"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales2:int = obj["RepSales2"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales3:int = obj["RepSales3"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales4:int = obj["RepSales4"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales5:int = obj["RepSales5"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.CMType:str = obj["CMType"]
      """  Indicates if the Credit Memo is for a Rebate  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding in Customer currency  """  
      self.Rpt1DepositCredit:int = obj["Rpt1DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2DepositCredit:int = obj["Rpt2DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3DepositCredit:int = obj["Rpt3DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayDiscAmt:int = obj["Rpt1PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayDiscAmt:int = obj["Rpt2PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayDiscAmt:int = obj["Rpt3PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1DepGainLoss:int = obj["Rpt1DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2DepGainLoss:int = obj["Rpt2DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3DepGainLoss:int = obj["Rpt3DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.LastChrgCalcDate:str = obj["LastChrgCalcDate"]
      """  The last date finance/late charges have been calculated for this invoice.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.TotFinChrg:int = obj["TotFinChrg"]
      """  Total Finance Charge amount.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.BlockedFinChrg:bool = obj["BlockedFinChrg"]
      """  Blocks certain invoice from generating finance/later charge.  """  
      self.BlockedFinChrgReason:str = obj["BlockedFinChrgReason"]
      """  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.BlockedRemLetters:bool = obj["BlockedRemLetters"]
      """  Blocks certain invoice from being printed on reminder letters.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.BlockedRemLettersReason:str = obj["BlockedRemLettersReason"]
      """  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.CurrRateDate:str = obj["CurrRateDate"]
      """  Currency Rate Date  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.UseAltBillTo:bool = obj["UseAltBillTo"]
      """  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden Finland Localization field - Banking Reference  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.ReversalDocAmount:int = obj["ReversalDocAmount"]
      """  Reversal Doucment Amount  """  
      self.OrigDueDate:str = obj["OrigDueDate"]
      """  Original Due Date at posting time  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The reference to CashHead.HeadNum.Used in deposit invoices  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  The free text field which can contain reference (such as Contract)  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.PBProjectID:str = obj["PBProjectID"]
      """  If the invoice was generated in Project Billing then it is reference to the project.  """  
      self.DepositAmt:int = obj["DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment  """  
      self.GUIExportBillNumber:str = obj["GUIExportBillNumber"]
      """   Taiwan Localization
Export Bill Number  """  
      self.DocDepositAmt:int = obj["DocDepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in document currency  """  
      self.GUIDateOfExport:str = obj["GUIDateOfExport"]
      """   Taiwan Localization
Date of Export  """  
      self.Rpt1DepositAmt:int = obj["Rpt1DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt1 currency  """  
      self.GUIExportType:str = obj["GUIExportType"]
      """   Taiwan Localization
Export Type  """  
      self.Rpt2DepositAmt:int = obj["Rpt2DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt2 currency  """  
      self.GUIExportMark:str = obj["GUIExportMark"]
      """   Taiwan Localization
Export Mark  """  
      self.Rpt3DepositAmt:int = obj["Rpt3DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt23currency  """  
      self.GUIExportBillType:str = obj["GUIExportBillType"]
      """   Taiwan Localization
Export Bill Type  """  
      self.DepUnallocatedAmt:int = obj["DepUnallocatedAmt"]
      """  Deposit unallocated amount in base currency  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DocDepUnallocatedAmt:int = obj["DocDepUnallocatedAmt"]
      """  Deposit unallocated amount in document currency  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.Rpt1DepUnallocatedAmt:int = obj["Rpt1DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt1 currency  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.Rpt2DepUnallocatedAmt:int = obj["Rpt2DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt2 currency  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Only records ready to bill will be printed in the Billing Statement  """  
      self.Rpt3DepUnallocatedAmt:int = obj["Rpt3DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.CustAgentName:str = obj["CustAgentName"]
      """  Customer Agent Name  """  
      self.CustAgentTaxRegNo:str = obj["CustAgentTaxRegNo"]
      """  Customer Agent Tax Region Number  """  
      self.ExportType:str = obj["ExportType"]
      """  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  """  
      self.ExportReportNo:str = obj["ExportReportNo"]
      """  Export Report Number  """  
      self.RealEstateNo:str = obj["RealEstateNo"]
      """  Real Estate Number  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.RecurringState:str = obj["RecurringState"]
      """  RecurringState  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsAddedToGTI:bool = obj["IsAddedToGTI"]
      """  IsAddedToGTI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CMReason:str = obj["CMReason"]
      """  CMReason  """  
      self.THIsImmatAdjustment:bool = obj["THIsImmatAdjustment"]
      """  THIsImmatAdjustment  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.RevisionDate:str = obj["RevisionDate"]
      """  RevisionDate  """  
      self.RevisionNum:int = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  TWGUIGroup  """  
      self.TWPeriodPrefix:str = obj["TWPeriodPrefix"]
      """  TWPeriodPrefix  """  
      self.InvInCollections:bool = obj["InvInCollections"]
      """  Indicates if the Invoice is in Collections status  """  
      self.CollectionsCust:bool = obj["CollectionsCust"]
      """   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  """  
      self.CounterARForm:int = obj["CounterARForm"]
      """  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  """  
      self.PostedRecog:bool = obj["PostedRecog"]
      """  flag indicates if Revenue of the invoice has been already posted  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Confirmation Date  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  MXApprovalYear  """  
      self.MXCBB:str = obj["MXCBB"]
      """  MXCBB  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  MXApprovalNum  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.MXOriginalAmount:int = obj["MXOriginalAmount"]
      """  MXOriginalAmount  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXOriginalDate:str = obj["MXOriginalDate"]
      """  MXOriginalDate  """  
      self.MXOriginalSeries:str = obj["MXOriginalSeries"]
      """  MXOriginalSeries  """  
      self.MXOriginalFolio:str = obj["MXOriginalFolio"]
      """  MXOriginalFolio  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  MXOriginalString  """  
      self.MXPaymentName:str = obj["MXPaymentName"]
      """  MXPaymentName  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EInvStatus:int = obj["EInvStatus"]
      """  EInvStatus  """  
      self.EInvTimestamp:str = obj["EInvTimestamp"]
      """  EInvTimestamp  """  
      self.EInvUpdatedBy:str = obj["EInvUpdatedBy"]
      """  EInvUpdatedBy  """  
      self.EInvException:str = obj["EInvException"]
      """  EInvException  """  
      self.WithTaxConfirm:bool = obj["WithTaxConfirm"]
      """  Flagged that this invoice has taxes which were necessary or is necessary now.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.MXCancelledDate:str = obj["MXCancelledDate"]
      """  MXCancelledDate  """  
      self.Overpaid:bool = obj["Overpaid"]
      """  Overpaid  """  
      self.OrdExchangeRate:int = obj["OrdExchangeRate"]
      """  OrdExchangeRate  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  PEAPPayNum  """  
      self.PEBankNumber:str = obj["PEBankNumber"]
      """  PEBankNumber  """  
      self.PECharges:int = obj["PECharges"]
      """  PECharges  """  
      self.PECommissions:int = obj["PECommissions"]
      """  PECommissions  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  PEDetTaxAmt  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  PEDetTaxCurrencyCode  """  
      self.PEDischargeAmt:int = obj["PEDischargeAmt"]
      """  PEDischargeAmt  """  
      self.PEDischargeDate:str = obj["PEDischargeDate"]
      """  PEDischargeDate  """  
      self.PEInterest:int = obj["PEInterest"]
      """  PEInterest  """  
      self.PENoPayPenalty:int = obj["PENoPayPenalty"]
      """  PENoPayPenalty  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PEBOEPosted:bool = obj["PEBOEPosted"]
      """  PEBOEPosted  """  
      self.DocPEInterest:int = obj["DocPEInterest"]
      """  DocPEInterest  """  
      self.DocPECommissions:int = obj["DocPECommissions"]
      """  DocPECommissions  """  
      self.DocPECharges:int = obj["DocPECharges"]
      """  DocPECharges  """  
      self.DocPENoPayPenalty:int = obj["DocPENoPayPenalty"]
      """  DocPENoPayPenalty  """  
      self.DocPEDischargeAmt:int = obj["DocPEDischargeAmt"]
      """  DocPEDischargeAmt  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  DocPEDetTaxAmt  """  
      self.Rpt1PEInterest:int = obj["Rpt1PEInterest"]
      """  Rpt1PEInterest  """  
      self.Rpt1PECommissions:int = obj["Rpt1PECommissions"]
      """  Rpt1PECommissions  """  
      self.Rpt1PECharges:int = obj["Rpt1PECharges"]
      """  Rpt1PECharges  """  
      self.Rpt1PENoPayPenalty:int = obj["Rpt1PENoPayPenalty"]
      """  Rpt1PENoPayPenalty  """  
      self.Rpt1PEDischargeAmt:int = obj["Rpt1PEDischargeAmt"]
      """  Rpt1PEDischargeAmt  """  
      self.Rpt2PEInterest:int = obj["Rpt2PEInterest"]
      """  Rpt2PEInterest  """  
      self.Rpt2PECommissions:int = obj["Rpt2PECommissions"]
      """  Rpt2PECommissions  """  
      self.Rpt2PECharges:int = obj["Rpt2PECharges"]
      """  Rpt2PECharges  """  
      self.Rpt2PENoPayPenalty:int = obj["Rpt2PENoPayPenalty"]
      """  Rpt2PENoPayPenalty  """  
      self.Rpt2PEDischargeAmt:int = obj["Rpt2PEDischargeAmt"]
      """  Rpt2PEDischargeAmt  """  
      self.Rpt3PEInterest:int = obj["Rpt3PEInterest"]
      """  Rpt3PEInterest  """  
      self.Rpt3PECommissions:int = obj["Rpt3PECommissions"]
      """  Rpt3PECommissions  """  
      self.Rpt3PECharges:int = obj["Rpt3PECharges"]
      """  Rpt3PECharges  """  
      self.Rpt3PENoPayPenalty:int = obj["Rpt3PENoPayPenalty"]
      """  Rpt3PENoPayPenalty  """  
      self.Rpt3PEDischargeAmt:int = obj["Rpt3PEDischargeAmt"]
      """  Rpt3PEDischargeAmt  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEBOEStatus:str = obj["PEBOEStatus"]
      """  PEBOEStatus  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.TWGUIExportDocumentName:str = obj["TWGUIExportDocumentName"]
      """  Document Name  """  
      self.TWGUIExportRemarks:str = obj["TWGUIExportRemarks"]
      """  Remarks  """  
      self.TWGUIExportVerification:str = obj["TWGUIExportVerification"]
      """  Verification  """  
      self.PEDebitNoteReasonCode:str = obj["PEDebitNoteReasonCode"]
      """  PEDebitNoteReasonCode  """  
      self.PEDebitNote:bool = obj["PEDebitNote"]
      """  PEDebitNote  """  
      self.MXPartPmt:bool = obj["MXPartPmt"]
      """  MXPartPmt  """  
      self.CNTaxInvoiceType:int = obj["CNTaxInvoiceType"]
      """  Tax Invoice Type  """  
      self.MXExportOperationType:str = obj["MXExportOperationType"]
      """  MXExportOperationType  """  
      self.MXExportCustDocCode:str = obj["MXExportCustDocCode"]
      """  MXExportCustDocCode  """  
      self.MXExportCertOriginNum:str = obj["MXExportCertOriginNum"]
      """  MXExportCertOriginNum  """  
      self.MXExportConfNum:str = obj["MXExportConfNum"]
      """  MXExportConfNum  """  
      self.MXExportCertOrigin:bool = obj["MXExportCertOrigin"]
      """  MXExportCertOrigin  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.AGDocConcept:int = obj["AGDocConcept"]
      """  AGDocConcept  """  
      self.EInvRefNum:str = obj["EInvRefNum"]
      """  Electronic Invoice reference number  """  
      self.ExportDocRefNum:str = obj["ExportDocRefNum"]
      """  Export document reference number  """  
      self.ExportDocDate:str = obj["ExportDocDate"]
      """  Export document date  """  
      self.INTaxTransactionID:str = obj["INTaxTransactionID"]
      """  Tax Transaction ID  """  
      self.MXMovingReasonFlag:bool = obj["MXMovingReasonFlag"]
      """  MXMovingReasonFlag  """  
      self.MXMovingReason:str = obj["MXMovingReason"]
      """  MXMovingReason  """  
      self.MXNumRegIdTrib:str = obj["MXNumRegIdTrib"]
      """  MXNumRegIdTrib  """  
      self.MXResidenCountryNum:int = obj["MXResidenCountryNum"]
      """  MXResidenCountryNum  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXExternalCode:str = obj["MXExternalCode"]
      """  MXExternalCode  """  
      self.ServiceInvoice:bool = obj["ServiceInvoice"]
      """  This invoice was created via an integration with a third-party field service.  """  
      self.MXDomesticTransfer:bool = obj["MXDomesticTransfer"]
      """  MXDomesticTransfer  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      """  Shipping Port Code  """  
      self.INExportProcedure:str = obj["INExportProcedure"]
      """  Export Procedure  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this invoice record is associated with.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case related to this invoice.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this invoice.  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The user id that override the invoice credit hold.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  """  
      self.PEXMLType:int = obj["PEXMLType"]
      """  Peru Electronic Invoice XML Type  """  
      self.COCreditMemoReasonCode:str = obj["COCreditMemoReasonCode"]
      """  COCreditMemoReasonCode  """  
      self.CODebitMemoReasonCode:str = obj["CODebitMemoReasonCode"]
      """  CODebitMemoReasonCode  """  
      self.COReasonDesc:str = obj["COReasonDesc"]
      """  COReasonDesc  """  
      self.CODebitNote:bool = obj["CODebitNote"]
      """  CODebitNote  """  
      self.PEDetractionTranNum:int = obj["PEDetractionTranNum"]
      """  PEDetractionTranNum  """  
      self.PEProductCode:str = obj["PEProductCode"]
      """  PEProductCode  """  
      self.PECollectionGroupID:str = obj["PECollectionGroupID"]
      """  PECollectionGroupID  """  
      self.PECaptionCode:str = obj["PECaptionCode"]
      """  PE Caption Code  """  
      self.PECaption:str = obj["PECaption"]
      """  PE Caption Code Description  """  
      self.PERefDocumentType:str = obj["PERefDocumentType"]
      """  PE Reference DocumentType 1  """  
      self.PERefDocumentNumber:str = obj["PERefDocumentNumber"]
      """  PE Reference Document Number 1  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PERefDocumentType2:str = obj["PERefDocumentType2"]
      """  PE Reference DocumentType 2  """  
      self.PERefDocumentType3:str = obj["PERefDocumentType3"]
      """  PE Reference DocumentType 3  """  
      self.PERefDocumentType4:str = obj["PERefDocumentType4"]
      """  PE Reference DocumentType 4  """  
      self.PERefDocumentType5:str = obj["PERefDocumentType5"]
      """  PE Reference DocumentType 5  """  
      self.PERefDocumentNumber2:str = obj["PERefDocumentNumber2"]
      """  PE Reference Document Number 2  """  
      self.PERefDocumentNumber3:str = obj["PERefDocumentNumber3"]
      """  PE Reference Document Number 3  """  
      self.PERefDocumentNumber4:str = obj["PERefDocumentNumber4"]
      """  PE Reference Document Number 4  """  
      self.PERefDocumentNumber5:str = obj["PERefDocumentNumber5"]
      """  PE Reference Document Number 5  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  Date and Time of E-invoice generation.  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Flag that indicates if the Invoice is for Central Collection.  """  
      self.CColChildCompany:str = obj["CColChildCompany"]
      """  Company that created this invoice.  """  
      self.CColParentCompany:str = obj["CColParentCompany"]
      """  Central Collection company.  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the invoicing company.  """  
      self.CColChildInvoiceNum:int = obj["CColChildInvoiceNum"]
      """  Invoice number on the invoicing company.  """  
      self.CColInvoiceNum:int = obj["CColInvoiceNum"]
      """  Invoice number on central collection company  """  
      self.CColChildLegalNumber:str = obj["CColChildLegalNumber"]
      """  Legal number on the invoicing company invoice.  """  
      self.CColLegalNumber:str = obj["CColLegalNumber"]
      """  Legal number on central collection company.  """  
      self.CColInvoiceRef:int = obj["CColInvoiceRef"]
      """  Invoice reference on the Invoicing Company.  """  
      self.CColInvBal:int = obj["CColInvBal"]
      """  Invoice Balance in the Central Collection company.  """  
      self.DocCColInvBal:int = obj["DocCColInvBal"]
      """  Central Collection Doc Invoice Balance.  """  
      self.CColInvAmt:int = obj["CColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.DocCColInvAmt:int = obj["DocCColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.Rpt1CColInvBal:int = obj["Rpt1CColInvBal"]
      """  Rpt 1 Parent Invoice Balance  """  
      self.Rpt2CColInvBal:int = obj["Rpt2CColInvBal"]
      """  Rpt 2 Parent Invoice Balance  """  
      self.Rpt3CColInvBal:int = obj["Rpt3CColInvBal"]
      """  Rpt 3 Parent Invoice Balance  """  
      self.Rpt1CColInvAmt:int = obj["Rpt1CColInvAmt"]
      """  Rpt 1 Child Invoice Amount  """  
      self.Rpt2CColInvAmt:int = obj["Rpt2CColInvAmt"]
      """  Rpt 2 Child Invoice Amount  """  
      self.Rpt3CColInvAmt:int = obj["Rpt3CColInvAmt"]
      """  Rpt 3 Child Invoice Amount  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ELIEInvTerminalName:str = obj["ELIEInvTerminalName"]
      """  User terminal name  """  
      self.ELIEInvTerminalIP:str = obj["ELIEInvTerminalIP"]
      """  User terminal IP  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.CColOpenInvoice:bool = obj["CColOpenInvoice"]
      """  Indicates if the Central Collection parent invoice is open.  """  
      self.AGQRCodeData:str = obj["AGQRCodeData"]
      """  AGQRCodeData  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallLine:int = obj["CallLine"]
      """  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstInvoiceNum:int = obj["MXSubstInvoiceNum"]
      """  MXSubstInvoiceNum  """  
      self.MXExportType:str = obj["MXExportType"]
      """  MXExportType  """  
      self.MXGlobalInvoicePeriod:str = obj["MXGlobalInvoicePeriod"]
      """  MXGlobalInvoicePeriod  """  
      self.MXGlobalInvoiceMonth:str = obj["MXGlobalInvoiceMonth"]
      """  MXGlobalInvoiceMonth  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  ELIEInvServiceProviderStatus  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.AmountDue:int = obj["AmountDue"]
      """  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  """  
      self.ApplyAmt:int = obj["ApplyAmt"]
      """  The amount of the payment to apply to the invoice  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.BankNetPay:int = obj["BankNetPay"]
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.CashGroupID:str = obj["CashGroupID"]
      """  This external field captures the IMCashGrp.GroupID used in object BankFileImport.p  """  
      self.DiscAmt:int = obj["DiscAmt"]
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.Discount:int = obj["Discount"]
      """  This new column should display payment discount amounts for invoices that are still within discount terms  """  
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      self.DocAmountDue:int = obj["DocAmountDue"]
      """  Amount of the next schedule due. This amount is calculated based on the Cash Receipt Transaction Apply Date and the Due Dates of each payment of the Payment Schedule of the invoice.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      self.DocGrossPay:int = obj["DocGrossPay"]
      self.DocNetPay:int = obj["DocNetPay"]
      self.DueDateHighLighted:bool = obj["DueDateHighLighted"]
      """  Due Date should be higthlighted if number of business days between selection date and invoice due date is less that 2 (for subsequent recurrent payment type) or 5 (for one-off or first recurrent payment types) days  """  
      self.GrossPay:int = obj["GrossPay"]
      self.IsCreditMemo:bool = obj["IsCreditMemo"]
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  DueDate from Select Invoices dialog.  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      self.Rpt1GrossPay:int = obj["Rpt1GrossPay"]
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      self.Rpt2GrossPay:int = obj["Rpt2GrossPay"]
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      self.Rpt3GrossPay:int = obj["Rpt3GrossPay"]
      self.Selected:bool = obj["Selected"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      """  Taxable Write Off  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.AllocAmount:int = obj["AllocAmount"]
      """  This new column should enable the user to enter a draft payment amount ? a part of the check amount that is to be allocated to the invoice  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARInvSelTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum of ARInvcSel  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARInvSelTableset:
   def __init__(self, obj):
      self.ARInvSel:list[Erp_Tablesets_ARInvSelRow] = obj["ARInvSel"]
      self.ARInvSelTGLC:list[Erp_Tablesets_ARInvSelTGLCRow] = obj["ARInvSelTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankFileImportParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.ImportFile:str = obj["ImportFile"]
      self.ImportFormat:str = obj["ImportFormat"]
      self.ClientImportFileName:str = obj["ClientImportFileName"]
      self.ServerImportFileName:str = obj["ServerImportFileName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankFileImportParamTableset:
   def __init__(self, obj):
      self.BankFileImportParam:list[Erp_Tablesets_BankFileImportParamRow] = obj["BankFileImportParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankFileImportTableset:
   def __init__(self, obj):
      self.CashGrpImport:list[Erp_Tablesets_CashGrpImportRow] = obj["CashGrpImport"]
      self.CashHeadImport:list[Erp_Tablesets_CashHeadImportRow] = obj["CashHeadImport"]
      self.CashDtlImport:list[Erp_Tablesets_CashDtlImportRow] = obj["CashDtlImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashDtlImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CheckRef:str = obj["CheckRef"]
      """  CheckRef  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.Discount:int = obj["Discount"]
      """  Discount  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  DocDiscount  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.GLRefType:str = obj["GLRefType"]
      """  GLRefType  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  GLRefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  DebitNote  """  
      self.DNComments:str = obj["DNComments"]
      """  DNComments  """  
      self.DNAmount:int = obj["DNAmount"]
      """  DNAmount  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  DocDnAmount  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  DNCustNbr  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  RoundDiff  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Rpt1Discount  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Rpt2Discount  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Rpt3Discount  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Rpt1DnAmount  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Rpt2DnAmount  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Rpt3DnAmount  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Rpt1TranAmt  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Rpt2TranAmt  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Rpt3TranAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  WithholdAmt  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  DocWithholdAmt  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Rpt1WithholdAmt  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Rpt2WithholdAmt  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Rpt3WithholdAmt  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  SelfAssessAmt  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  DocSelfAssessAmt  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Rpt1SelfAssessAmt  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Rpt2SelfAssessAmt  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Rpt3SelfAssessAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Rpt1TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Rpt2TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Rpt3TaxAmt  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  RedStorno  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  TaxReceiptDate  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  TaxReceiptNo  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  WHTCertificateDate  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  WHTCertificateNo  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.GainLossType:str = obj["GainLossType"]
      """  GainLossType  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  ReverseGL  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  RevalueDate  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  RevalueBal  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  DocRevalueBal  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Rpt1RevalueBal  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Rpt2RevalueBal  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Rpt3RevalueBal  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MainSite:bool = obj["MainSite"]
      """  MainSite  """  
      self.SiteCode:str = obj["SiteCode"]
      """  SiteCode  """  
      self.BranchID:str = obj["BranchID"]
      """  BranchID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  TaxRemarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  NonDeductCode  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  NonDeductAmt  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  NonDeductDocAmt  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  NonDeductRpt1Amt  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  NonDeductRpt2Amt  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  NonDeductRpt3Amt  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.InvDueDate:str = obj["InvDueDate"]
      """  InvDueDate  """  
      self.ManualMatch:bool = obj["ManualMatch"]
      """  ManualMatch  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  BillingNumber  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  WriteOffHeadNumRef  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  TaxableAdjustment  """  
      self.BankNetPay:int = obj["BankNetPay"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      self.DocNetPay:int = obj["DocNetPay"]
      self.InvPayStatus:str = obj["InvPayStatus"]
      self.DocRemainInvBal:int = obj["DocRemainInvBal"]
      self.InvOpenBalance:int = obj["InvOpenBalance"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.PIStatus:str = obj["PIStatus"]
      """  PIStatus  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  PIStatusGrp  """  
      self.PIType:str = obj["PIType"]
      """  PIType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      """  Bank Branch Code  """  
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      """  Currency.CurrencyCode of the currency that the bank account is denominated in.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      """  IBAN Code  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashGrpImportListTableset:
   def __init__(self, obj):
      self.CashGrpImportList:list[Erp_Tablesets_CashGrpImportListRow] = obj["CashGrpImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashGrpImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.PIStatus:str = obj["PIStatus"]
      """  PIStatus  """  
      self.PIStatusGrp:bool = obj["PIStatusGrp"]
      """  PIStatusGrp  """  
      self.PIType:str = obj["PIType"]
      """  PIType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BankBatchID:str = obj["BankBatchID"]
      """  BankBatchID  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.ImportFileName:str = obj["ImportFileName"]
      """  ImportFileName  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.LockForChanges:bool = obj["LockForChanges"]
      self.ProcessButtonEnabled:bool = obj["ProcessButtonEnabled"]
      self.ProcessStatusDisplay:str = obj["ProcessStatusDisplay"]
      self.EnableMatchCMemoWithInv:bool = obj["EnableMatchCMemoWithInv"]
      """  Enable matching Credit Memo with Invoice  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.CheckRef:str = obj["CheckRef"]
      """  CheckRef  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  UnAppliedAmt  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  DocUnAppliedAmt  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  AppliedAmt  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  DocAppliedAmt  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  CreditMemoNum  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  CashBookNum  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  CashbookLine  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.ExternalID:str = obj["ExternalID"]
      """  ExternalID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  GLRefType  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  GLRefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  CardMemberName  """  
      self.CardNumber:str = obj["CardNumber"]
      """  CardNumber  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  ExpirationMonth  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  ExpirationYear  """  
      self.CardID:str = obj["CardID"]
      """  CardID  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  CardmemberReference  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  ProcessCard  """  
      self.CCAmount:int = obj["CCAmount"]
      """  CCAmount  """  
      self.CCFreight:int = obj["CCFreight"]
      """  CCFreight  """  
      self.CCTax:int = obj["CCTax"]
      """  CCTax  """  
      self.CCTotal:int = obj["CCTotal"]
      """  CCTotal  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  CCDocAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  CCDocFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  CCDocTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  CCDocTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  CCStreetAddr  """  
      self.CCZip:str = obj["CCZip"]
      """  CCZip  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  DebNoteOnly  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Rpt1AppliedAmt  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Rpt2AppliedAmt  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Rpt3AppliedAmt  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Rpt1TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Rpt2TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Rpt3TaxAmt  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Rpt1TranAmt  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Rpt2TranAmt  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Rpt3TranAmt  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Rpt1UnAppliedAmt  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Rpt2UnAppliedAmt  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Rpt3UnAppliedAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  DocDepApplied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  Rpt1CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  Rpt2CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  Rpt3CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  Rpt1CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  Rpt2CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  Rpt3CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  Rpt1CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  Rpt2CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  Rpt3CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  Rpt1CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  Rpt2CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  Rpt3CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  ReadyToCalc  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  RecalcBeforePost  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  WithholdAmt  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  DocWithholdAmt  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Rpt1WithholdAmt  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Rpt2WithholdAmt  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Rpt3WithholdAmt  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  SelfAssessAmt  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  DocSelfAssessAmt  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Rpt1SelfAssessAmt  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Rpt2SelfAssessAmt  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Rpt3SelfAssessAmt  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  ReceiptCurrencyCode  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  ReceiptAmt  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  BankRcptExchangeRate  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  SettlementExchangeRate  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  CMCurrencyCode  """  
      self.CMAmount:int = obj["CMAmount"]
      """  CMAmount  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  ReverseRef  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  ReverseDate  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  TaxWhld  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  DiscountDate  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  TaxWhldCalc  """  
      self.ContractDate:str = obj["ContractDate"]
      """  ContractDate  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  UnallocatedAmt  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  DocUnallocatedAmt  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Rpt1UnallocatedAmt  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Rpt2UnallocatedAmt  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Rpt3UnallocatedAmt  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  ApplyHeadNum  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  AllocatedAmt  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  DocAllocatedAmt  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Rpt1AllocatedAmt  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Rpt2AllocatedAmt  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Rpt3AllocatedAmt  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.BankTranID:str = obj["BankTranID"]
      """  BankTranID  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MainSite:bool = obj["MainSite"]
      """  MainSite  """  
      self.SiteCode:str = obj["SiteCode"]
      """  SiteCode  """  
      self.BranchID:str = obj["BranchID"]
      """  BranchID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  InvoiceDate  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  TaxRemarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  NonDeductCode  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  NonDeductAmt  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  NonDeductDocAmt  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  NonDeductRpt1Amt  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  NonDeductRpt2Amt  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  NonDeductRpt3Amt  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  BankTransDate  """  
      self.CustNameFromFile:str = obj["CustNameFromFile"]
      """  CustNameFromFile  """  
      self.OCRNumber:str = obj["OCRNumber"]
      """  OCRNumber  """  
      self.ImportLineStatus:str = obj["ImportLineStatus"]
      """  ImportLineStatus  """  
      self.ImportLineError:str = obj["ImportLineError"]
      """  ImportLineError  """  
      self.DescFromImport:str = obj["DescFromImport"]
      """  DescFromImport  """  
      self.InvNumList:str = obj["InvNumList"]
      """  InvNumList  """  
      self.InvAmtList:str = obj["InvAmtList"]
      """  InvAmtList  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.ManualMatch:bool = obj["ManualMatch"]
      """  ManualMatch  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  CreditMemo  """  
      self.CMNum:int = obj["CMNum"]
      """  CMNum  """  
      self.CMDocAmount:int = obj["CMDocAmount"]
      """  CMDocAmount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.CHISRRefNumAvailableToChange:bool = obj["CHISRRefNumAvailableToChange"]
      """  CHISRRefNumAvailableToChange  """  
      self.BankBatchID:str = obj["BankBatchID"]
      """  BankBatchID  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  RcptCurAppliedAmt  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  RcptCurUnAppliedAmt  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  MXPaySupplementFlag  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MXOriginalCheckRef  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MXBankID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  ReversedReason  """  
      self.CCCity:str = obj["CCCity"]
      """  CCCity  """  
      self.CCState:str = obj["CCState"]
      """  CCState  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Adjustment  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  AdjustmentRef  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  AdjustmentReason  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  WriteOffAmount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACHTranCode  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  CustomerBankID  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  CustomerBankAcctNumber  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  CustomerBankIBANCode  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  CustomerBankNameOnAccount  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  CustomerBankAddress1  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  CustomerBankAddress2  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  CustomerBankAddress3  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  CustomerBankCity  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  CustomerBankState  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  CustomerBankPostalCode  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  CustomerBankCountryNum  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  CustomerBankName  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.CashRecGroupID:str = obj["CashRecGroupID"]
      """  Cash Rec Group ID  """  
      self.CashRecHeadNum:int = obj["CashRecHeadNum"]
      """  Cash Rec Head Num  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  RvJrnUID  """  
      self.ProcessStatus:str = obj["ProcessStatus"]
      """  ProcessStatus  """  
      self.NettingID:int = obj["NettingID"]
      """  NettingID  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  BankReceiptAmt  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.CHImportStatus:bool = obj["CHImportStatus"]
      """  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  """  
      self.EnableCust:bool = obj["EnableCust"]
      """  Indicates if the customer id should be available for input.  Used in Bank File Import Workbench.  """  
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.LockForChanges:bool = obj["LockForChanges"]
      self.ProcessStatusDisplay:str = obj["ProcessStatusDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RcptCurrencyCurrSymbol:str = obj["RcptCurrencyCurrSymbol"]
      self.SettlementCurrencyCurrSymbol:str = obj["SettlementCurrencyCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtBankFileImportTableset:
   def __init__(self, obj):
      self.CashGrpImport:list[Erp_Tablesets_CashGrpImportRow] = obj["CashGrpImport"]
      self.CashHeadImport:list[Erp_Tablesets_CashHeadImportRow] = obj["CashHeadImport"]
      self.CashDtlImport:list[Erp_Tablesets_CashDtlImportRow] = obj["CashDtlImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBankFileImportParam_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Cash Group ID  """  
      pass

class GetBankFileImportParam_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFileImportParamTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFileImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankFileImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankFileImportTableset] = obj["returnObj"]
      pass

class GetGroupInfo_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID  """  
      pass

class GetGroupInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.processStatus:str = obj["parameters"]
      self.processStatusDisplay:str = obj["parameters"]
      self.processButtonEnabled:bool = obj["processButtonEnabled"]
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
      self.returnObj:list[Erp_Tablesets_CashGrpImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCashDtlImport_input:
   """ Required : 
   ds
   groupID
   headNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewCashDtlImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpImportNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class GetNewCashGrpImportNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashGrpImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class GetNewCashGrpImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCashHeadImport_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewCashHeadImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCashGrpImport
   whereClauseCashHeadImport
   whereClauseCashDtlImport
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCashGrpImport:str = obj["whereClauseCashGrpImport"]
      self.whereClauseCashHeadImport:str = obj["whereClauseCashHeadImport"]
      self.whereClauseCashDtlImport:str = obj["whereClauseCashDtlImport"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankFileImportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class ImportBankFileExpress_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportParamTableset] = obj["ds"]
      pass

class ImportBankFileExpress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportParamTableset] = obj["ds"]
      self.opPaymentsFoundWithErrorsMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ImportBankFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportParamTableset] = obj["ds"]
      pass

class ImportBankFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportParamTableset] = obj["ds"]
      self.opCMemoPaymentsNotFoundMessage:str = obj["parameters"]
      self.opPaymentsFoundWithErrorsMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class LockGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Selected Group ID  """  
      pass

class LockGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class MatchCHCashHeadImport_input:
   """ Required : 
   ipGroupID
   ipHeadNum
   ipISRRefNum
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  GroupID  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  Head Number  """  
      self.ipISRRefNum:str = obj["ipISRRefNum"]
      """  New ISR Reference number  """  
      pass

class MatchCHCashHeadImport_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Result of matching  """  
      pass

class MatchPayments_input:
   """ Required : 
   matchGroupID
   """  
   def __init__(self, obj):
      self.matchGroupID:str = obj["matchGroupID"]
      """  The Group to match  """  
      pass

class MatchPayments_output:
   def __init__(self, obj):
      pass

class ProcessReceipts_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Group to match  """  
      pass

class ProcessReceipts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cReturnMsg:str = obj["parameters"]
      self.lClearRcds:bool = obj["lClearRcds"]
      pass

      """  output parameters  """  

class ResetBankFileImportExpressGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  GroupID  """  
      pass

class ResetBankFileImportExpressGroup_output:
   def __init__(self, obj):
      pass

class SelectInvoices_input:
   """ Required : 
   pcGroupID
   piHeadNum
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AR Check Group ID  """  
      self.piHeadNum:int = obj["piHeadNum"]
      """  IMCashRec header number  """  
      pass

class SelectInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARInvSelTableset] = obj["returnObj"]
      pass

class UnlockGroup_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The Group ID selected by the user.  """  
      pass

class UnlockGroup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankFileImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankFileImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

