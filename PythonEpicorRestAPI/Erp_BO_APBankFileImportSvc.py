import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APBankFileImportSvc
# Description: none
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APBankFileImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APBankFileImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports",headers=creds) as resp:
           return await resp.json()

async def post_APBankFileImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APBankFileImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APBankFileImport item
   Description: Calls GetByID to retrieve the APBankFileImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APBankFileImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APBankFileImports_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APBankFileImport for the service
   Description: Calls UpdateExt to update APBankFileImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APBankFileImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APBankFileImports_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APBankFileImport item
   Description: Call UpdateExt to delete APBankFileImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APBankFileImport
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports_Company_GroupID_CheckHedImports(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CheckHedImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CheckHedImports1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/CheckHedImports",headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports_Company_GroupID_CheckHedImports_Company_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckHedImport item
   Description: Calls GetByID to retrieve the CheckHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/CheckHedImports(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports_Company_GroupID_APChkGrpImportAttches(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APChkGrpImportAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APChkGrpImportAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/APChkGrpImportAttches",headers=creds) as resp:
           return await resp.json()

async def get_APBankFileImports_Company_GroupID_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APChkGrpImportAttch item
   Description: Calls GetByID to retrieve the APChkGrpImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpImportAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APBankFileImports(" + Company + "," + GroupID + ")/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CheckHedImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CheckHedImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports",headers=creds) as resp:
           return await resp.json()

async def post_CheckHedImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CheckHedImports_Company_HeadNum(Company, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckHedImport item
   Description: Calls GetByID to retrieve the CheckHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CheckHedImports_Company_HeadNum(Company, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CheckHedImport for the service
   Description: Calls UpdateExt to update CheckHedImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CheckHedImports_Company_HeadNum(Company, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CheckHedImport item
   Description: Call UpdateExt to delete CheckHedImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CheckHedImports_Company_HeadNum_APTranImports(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APTranImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTranImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")/APTranImports",headers=creds) as resp:
           return await resp.json()

async def get_CheckHedImports_Company_HeadNum_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company, HeadNum, APTranImportNo, InvoiceNum, Voided, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTranImport item
   Description: Calls GetByID to retrieve the APTranImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranImportNo: Desc: APTranImportNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedImports(" + Company + "," + HeadNum + ")/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APTranImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APTranImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports",headers=creds) as resp:
           return await resp.json()

async def post_APTranImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company, HeadNum, APTranImportNo, InvoiceNum, Voided, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTranImport item
   Description: Calls GetByID to retrieve the APTranImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranImportNo: Desc: APTranImportNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company, HeadNum, APTranImportNo, InvoiceNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APTranImport for the service
   Description: Calls UpdateExt to update APTranImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranImportNo: Desc: APTranImportNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APTranImports_Company_HeadNum_APTranImportNo_InvoiceNum_Voided(Company, HeadNum, APTranImportNo, InvoiceNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APTranImport item
   Description: Call UpdateExt to delete APTranImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranImportNo: Desc: APTranImportNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APTranImports(" + Company + "," + HeadNum + "," + APTranImportNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APChkGrpImportAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APChkGrpImportAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APChkGrpImportAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches",headers=creds) as resp:
           return await resp.json()

async def post_APChkGrpImportAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APChkGrpImportAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APChkGrpImportAttch item
   Description: Calls GetByID to retrieve the APChkGrpImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APChkGrpImportAttch for the service
   Description: Calls UpdateExt to update APChkGrpImportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APChkGrpImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpImportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APChkGrpImportAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APChkGrpImportAttch item
   Description: Call UpdateExt to delete APChkGrpImportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APChkGrpImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APChkGrpImportAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPmtMatches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPmtMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPmtMatches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPmtMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches",headers=creds) as resp:
           return await resp.json()

async def post_APPmtMatches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPmtMatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPmtMatches_Company_HeadNum_APTRanNo(Company, HeadNum, APTRanNo, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPmtMatch item
   Description: Calls GetByID to retrieve the APPmtMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPmtMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTRanNo: Desc: APTRanNo   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPmtMatches_Company_HeadNum_APTRanNo(Company, HeadNum, APTRanNo, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPmtMatch for the service
   Description: Calls UpdateExt to update APPmtMatch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPmtMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTRanNo: Desc: APTRanNo   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPmtMatchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPmtMatches_Company_HeadNum_APTRanNo(Company, HeadNum, APTRanNo, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPmtMatch item
   Description: Call UpdateExt to delete APPmtMatch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPmtMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTRanNo: Desc: APTRanNo   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/APPmtMatches(" + Company + "," + HeadNum + "," + APTRanNo + ")",headers=creds) as resp:
           return await resp.json()

async def get_CheckHedMatcheds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CheckHedMatcheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CheckHedMatcheds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedMatchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds",headers=creds) as resp:
           return await resp.json()

async def post_CheckHedMatcheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CheckHedMatcheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CheckHedMatcheds_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CheckHedMatched item
   Description: Calls GetByID to retrieve the CheckHedMatched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CheckHedMatched
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CheckHedMatcheds_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CheckHedMatched for the service
   Description: Calls UpdateExt to update CheckHedMatched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CheckHedMatched
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedMatchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CheckHedMatcheds_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CheckHedMatched item
   Description: Call UpdateExt to delete CheckHedMatched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CheckHedMatched
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/CheckHedMatcheds(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPChkGrpImport, whereClauseAPChkGrpImportAttch, whereClauseCheckHedImport, whereClauseAPTranImport, whereClauseAPPmtMatch, whereClauseCheckHedMatched, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPChkGrpImport=" + whereClauseAPChkGrpImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPChkGrpImportAttch=" + whereClauseAPChkGrpImportAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCheckHedImport=" + whereClauseCheckHedImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPTranImport=" + whereClauseAPTranImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPmtMatch=" + whereClauseAPPmtMatch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCheckHedMatched=" + whereClauseCheckHedMatched
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGrpBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGrpBankAcctID
   Description: Method to call when changing the bank account.
   OperationID: ChangeGrpBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGrpBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGrpBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMatchFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMatchFlag
   Description: Validate entered record number - user matches payments
   OperationID: ChangeMatchFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMatchFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMatchFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRecordNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRecordNum
   Description: none
   OperationID: ChangeRecordNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRecordNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRecordNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportBankFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportBankFile
   Description: none
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchPayments
   Description: none
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchTelepayPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchTelepayPayments
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: MatchTelepayPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchTelepayPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchTelepayPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnEnterGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnEnterGroupID
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: OnEnterGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnEnterGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnEnterGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPayments
   Description: Method Match imported file records to unmatched payments of Proposed Payment Groups
   OperationID: ProcessPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRejectedPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRejectedPayments
   Description: Delete Rejected Payments from the system
   OperationID: DeleteRejectedPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRejectedPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRejectedPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetStatement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetStatement
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPChkGrpImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPChkGrpImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPChkGrpImportAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPChkGrpImportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpImportAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpImportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpImportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCheckHedImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCheckHedImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHedImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTranImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTranImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTranImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APBankFileImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpImportAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPmtMatchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPmtMatchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckHedImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedMatchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckHedMatchedRow] = obj["value"]
      pass

class Erp_Tablesets_APChkGrpImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
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

class Erp_Tablesets_APChkGrpImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  PostErrorLog  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  PostInProcess  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """  GrpCreationVia  """  
      self.CompletelyMatched:bool = obj["CompletelyMatched"]
      """  CompletelyMatched  """  
      self.MatchFlag:bool = obj["MatchFlag"]
      """  MatchFlag  """  
      self.ImportedFlag:bool = obj["ImportedFlag"]
      """  ImportedFlag  """  
      self.ProcessedFlag:bool = obj["ProcessedFlag"]
      """  ProcessedFlag  """  
      self.TotalStatementAmt:int = obj["TotalStatementAmt"]
      """  TotalStatementAmt  """  
      self.MatchedAmt:int = obj["MatchedAmt"]
      """  MatchedAmt  """  
      self.UnMatchedAmt:int = obj["UnMatchedAmt"]
      """  UnMatchedAmt  """  
      self.ImportBankCode:str = obj["ImportBankCode"]
      """  ImportBankCode  """  
      self.ImportStmtNbr:str = obj["ImportStmtNbr"]
      """  ImportStmtNbr  """  
      self.ImportBankDate:str = obj["ImportBankDate"]
      """  ImportBankDate  """  
      self.PaymentType:int = obj["PaymentType"]
      """  PaymentType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
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
      self.OkToImport:bool = obj["OkToImport"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToMatch:bool = obj["OkToMatch"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  The availability of Process Group menu item is based on this flag  """  
      self.OkToReport:bool = obj["OkToReport"]
      """  The availability of Report menu item is based on this flag  """  
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
      self.ReadyToMatch:bool = obj["ReadyToMatch"]
      """  the flag to show if imported records are ready for matching  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  the flag to show if imported records are ready for processing  """  
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      """  Bank Branch Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APChkGrpImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  PostErrorLog  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  PostInProcess  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """  GrpCreationVia  """  
      self.CompletelyMatched:bool = obj["CompletelyMatched"]
      """  CompletelyMatched  """  
      self.MatchFlag:bool = obj["MatchFlag"]
      """  MatchFlag  """  
      self.ImportedFlag:bool = obj["ImportedFlag"]
      """  ImportedFlag  """  
      self.ProcessedFlag:bool = obj["ProcessedFlag"]
      """  ProcessedFlag  """  
      self.TotalStatementAmt:int = obj["TotalStatementAmt"]
      """  TotalStatementAmt  """  
      self.MatchedAmt:int = obj["MatchedAmt"]
      """  MatchedAmt  """  
      self.UnMatchedAmt:int = obj["UnMatchedAmt"]
      """  UnMatchedAmt  """  
      self.ImportBankCode:str = obj["ImportBankCode"]
      """  ImportBankCode  """  
      self.ImportStmtNbr:str = obj["ImportStmtNbr"]
      """  ImportStmtNbr  """  
      self.ImportBankDate:str = obj["ImportBankDate"]
      """  ImportBankDate  """  
      self.PaymentType:int = obj["PaymentType"]
      """  PaymentType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReadyToMatch:bool = obj["ReadyToMatch"]
      """  the flag to show if imported records are ready for matching  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  the flag to show if imported records are ready for processing  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.OkToImport:bool = obj["OkToImport"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToMatch:bool = obj["OkToMatch"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  The availability of Process Group menu item is based on this flag  """  
      self.OkToReport:bool = obj["OkToReport"]
      """  The availability of Report menu item is based on this flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      self.PayMethodOutputFile:str = obj["PayMethodOutputFile"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPmtMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      self.CheckAmt:int = obj["CheckAmt"]
      self.VendorID:str = obj["VendorID"]
      self.RecordNumber:int = obj["RecordNumber"]
      """  The record number of imported file - used for manual match  """  
      self.CheckDate:str = obj["CheckDate"]
      self.APTRanNo:int = obj["APTRanNo"]
      self.CheckNum:int = obj["CheckNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranImportNo:int = obj["APTranImportNo"]
      """  APTranImportNo  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  DiscAmt  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  DocDiscAmt  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckNum:int = obj["CheckNum"]
      """  CheckNum  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  EntryPerson  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.RefType:str = obj["RefType"]
      """  RefType  """  
      self.RefCode:str = obj["RefCode"]
      """  RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  RefCodeDesc  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  RoundDiff  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Rpt1DiscAmt  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Rpt2DiscAmt  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Rpt3DiscAmt  """  
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
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
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
      self.RedStorno:bool = obj["RedStorno"]
      """  RedStorno  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  PrePayment  """  
      self.ContractRef:str = obj["ContractRef"]
      """  ContractRef  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  ContractRefDate  """  
      self.RefPONum:int = obj["RefPONum"]
      """  RefPONum  """  
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
      self.BankID:str = obj["BankID"]
      """  BankID  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  BankPaidAmt  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  DocBankPaidAmt  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Rpt1BankPaidAmt  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Rpt2BankPaidAmt  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Rpt3BankPaidAmt  """  
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  AdjLegalNumber  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  AdjTranDocTypeID  """  
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
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  CardID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  CardHolderTaxID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  CardMemberName  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
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
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckHedImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckNum:int = obj["CheckNum"]
      """  CheckNum  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  CheckSrc  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  ClearedCheck  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  ClearedPending  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  ClearedAmt  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  DocClearedAmt  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  ClearedPerson  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  ClearedDate  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  ClearedTime  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  ClearedStmtEndDate  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  CheckAmt  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  DocCheckAmt  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  ManualPrint  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  EntryPerson  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State  """  
      self.ZIP:str = obj["ZIP"]
      """  ZIP  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.CountryNum:int = obj["CountryNum"]
      """  CountryNum  """  
      self.BankSlip:str = obj["BankSlip"]
      """  BankSlip  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  ElecPayment  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  VendorBankID  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  VendorBankName  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  VendorBankNameOnAccount  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  VendorBankAddress1  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  VendorBankAddress2  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  VendorBankAddress3  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  VendorBankCity  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  VendorBankState  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  VendorBankPostalCode  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  VendorBankCountryNum  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  VendorBankAcctNumber  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  VendorBankSwiftNum  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  CashBookNum  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  CashbookLine  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  XRefCheckNum  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Rpt1CheckAmt  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Rpt2CheckAmt  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Rpt3CheckAmt  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Rpt1ClearedAmt  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Rpt2ClearedAmt  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Rpt3ClearedAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  PaymentTotal  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  DocPaymentTotal  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Rpt1PaymentTotal  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Rpt2PaymentTotal  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Rpt3PaymentTotal  """  
      self.Variance:int = obj["Variance"]
      """  Variance  """  
      self.DocVariance:int = obj["DocVariance"]
      """  DocVariance  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Rpt1Variance  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Rpt2Variance  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Rpt3Variance  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  PaymentBankRate  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  BankTotalAmt  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  IsEnterTotal  """  
      self.LockRate:int = obj["LockRate"]
      """  LockRate  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  ReadyToCalc  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  RecalcBeforePost  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  UsePendAcct  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  ForceDiscount  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  FirstHeadNum  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  ApplyingPayment  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.BankTranID:str = obj["BankTranID"]
      """  BankTranID  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  BankPaidAmt  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  DocBankPaidAmt  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Rpt1BankPaidAmt  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Rpt2BankPaidAmt  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Rpt3BankPaidAmt  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  BankTransDate  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusDesc  """  
      self.TransText:str = obj["TransText"]
      """  TransText  """  
      self.TransDetail:str = obj["TransDetail"]
      """  TransDetail  """  
      self.OrigInvoiceNum:str = obj["OrigInvoiceNum"]
      """  OrigInvoiceNum  """  
      self.OrigName:str = obj["OrigName"]
      """  OrigName  """  
      self.OrigVendorID:str = obj["OrigVendorID"]
      """  OrigVendorID  """  
      self.PropGroupID:str = obj["PropGroupID"]
      """  PropGroupID  """  
      self.NumPayment:int = obj["NumPayment"]
      """  NumPayment  """  
      self.CheckHeadNum:int = obj["CheckHeadNum"]
      """  CheckHeadNum  """  
      self.OrigVendorNum:int = obj["OrigVendorNum"]
      """  OrigVendorNum  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.OKToMatch:bool = obj["OKToMatch"]
      """  OKToMatch  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SavedInvoiceNum:str = obj["SavedInvoiceNum"]
      """  SavedInvoiceNum  """  
      self.SavedVendorName:str = obj["SavedVendorName"]
      """  SavedVendorName  """  
      self.SavedVendorID:str = obj["SavedVendorID"]
      """  SavedVendorID  """  
      self.SavedVendorNum:int = obj["SavedVendorNum"]
      """  SavedVendorNum  """  
      self.CheckStatus:int = obj["CheckStatus"]
      """  CheckStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.NOPaymentDirection:str = obj["NOPaymentDirection"]
      """  NOPaymentDirection  """  
      self.NOPaymentType:str = obj["NOPaymentType"]
      """  NOPaymentType  """  
      self.NOTransferFileName:str = obj["NOTransferFileName"]
      """  NOTransferFileName  """  
      self.NOBankTransRef:str = obj["NOBankTransRef"]
      """  NOBankTransRef  """  
      self.BalanceUpdate:int = obj["BalanceUpdate"]
      """  BalanceUpdate  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  BOEInvoiceNum  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MsgId:str = obj["MsgId"]
      """  MsgId  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.PayTranDocTypeID:str = obj["PayTranDocTypeID"]
      """  PayTranDocTypeID  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.TaxPaymInfo:str = obj["TaxPaymInfo"]
      """  TaxPaymInfo  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  VoidLegalNumber  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  VoidTranDocTypeID  """  
      self.SEGrpNum:int = obj["SEGrpNum"]
      """  SEGrpNum  """  
      self.SEReference:str = obj["SEReference"]
      """  SEReference  """  
      self.SEISGroupedPO3:bool = obj["SEISGroupedPO3"]
      """  SEISGroupedPO3  """  
      self.SEISExported:bool = obj["SEISExported"]
      """  SEISExported  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MXBankAcctNumber:str = obj["MXBankAcctNumber"]
      """  MXBankAcctNumber  """  
      self.MXBankIdentifier:str = obj["MXBankIdentifier"]
      """  MXBankIdentifier  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  BankBatchExcluded  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.SEPAPaymentDescription:str = obj["SEPAPaymentDescription"]
      """  SEPAPaymentDescription  """  
      self.NOImportErrors:str = obj["NOImportErrors"]
      """  NOImportErrors  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  THRefInvoiceNum  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  THRefVendorNum  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  VoidedReason  """  
      self.RegulatoryReportingCode:str = obj["RegulatoryReportingCode"]
      """  RegulatoryReportingCode  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  TaxPointDate  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACHTranCode  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  US1099KMerchCatCode  """  
      self.US1099KGen:bool = obj["US1099KGen"]
      """  US1099KGen  """  
      self.VendorBankBranchCode:str = obj["VendorBankBranchCode"]
      """  VendorBankBranchCode  """  
      self.NettingID:int = obj["NettingID"]
      """  NettingID  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  GL Description for the Payment Voiding process  """  
      self.DMDescription:str = obj["DMDescription"]
      """  GL Description for AP - Apply Debit Memo/Prepayment  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  MXDIOTTranType  """  
      self.TransDetail1:str = obj["TransDetail1"]
      """  Transaction Detail, part 1  """  
      self.TransDetail3:str = obj["TransDetail3"]
      """  Transactoin Detail part 3  """  
      self.TransDetail4:str = obj["TransDetail4"]
      """  Transaction Detail part 4  """  
      self.UnderpayFlag:bool = obj["UnderpayFlag"]
      """  Indicates if the amount of payment from the imported file is less than amount of  proposed  payment  """  
      self.OverpayFlag:bool = obj["OverpayFlag"]
      """  Indicates if the amount of payment from the imported file is more than amount of  proposed  payment  """  
      self.TransDetail2:str = obj["TransDetail2"]
      """  Transaction Detail, Part2  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckHedMatchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.Name:str = obj["Name"]
      """  Supplier Name  """  
      self.GroupID:str = obj["GroupID"]
      """  Payment Group ID  """  
      self.PrpGroupID:str = obj["PrpGroupID"]
      """  Group ID of the proposed Payment  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of the CheckHed matched  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number for the payment matched  """  
      self.APTranNo:int = obj["APTranNo"]
      self.CheckDate:str = obj["CheckDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the payment  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Payment amount  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount in Document currency  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      self.RecordNumber:int = obj["RecordNumber"]
      """  Record number of the imported table matched  """  
      self.Matched:str = obj["Matched"]
      self.CheckNum:int = obj["CheckNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeGrpBankAcctID_input:
   """ Required : 
   ProposedBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ProposedBankAcctID:str = obj["ProposedBankAcctID"]
      """  The proposed bank account id  """  
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class ChangeGrpBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMatchFlag_input:
   """ Required : 
   matchFlag
   pcGroupID
   ds
   """  
   def __init__(self, obj):
      self.matchFlag:bool = obj["matchFlag"]
      """  Record number entered/proposed  """  
      self.pcGroupID:str = obj["pcGroupID"]
      """  Group ID of the payment  """  
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class ChangeMatchFlag_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRecordNum_input:
   """ Required : 
   ds
   recordNumber
   pcGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      self.recordNumber:int = obj["recordNumber"]
      self.pcGroupID:str = obj["pcGroupID"]
      pass

class ChangeRecordNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
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

class DeleteRejectedPayments_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  Group ID of the paymnet  """  
      pass

class DeleteRejectedPayments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_APBankFileImportTableset:
   def __init__(self, obj):
      self.APChkGrpImport:list[Erp_Tablesets_APChkGrpImportRow] = obj["APChkGrpImport"]
      self.APChkGrpImportAttch:list[Erp_Tablesets_APChkGrpImportAttchRow] = obj["APChkGrpImportAttch"]
      self.CheckHedImport:list[Erp_Tablesets_CheckHedImportRow] = obj["CheckHedImport"]
      self.APTranImport:list[Erp_Tablesets_APTranImportRow] = obj["APTranImport"]
      self.APPmtMatch:list[Erp_Tablesets_APPmtMatchRow] = obj["APPmtMatch"]
      self.CheckHedMatched:list[Erp_Tablesets_CheckHedMatchedRow] = obj["CheckHedMatched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APChkGrpImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
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

class Erp_Tablesets_APChkGrpImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  PostErrorLog  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  PostInProcess  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """  GrpCreationVia  """  
      self.CompletelyMatched:bool = obj["CompletelyMatched"]
      """  CompletelyMatched  """  
      self.MatchFlag:bool = obj["MatchFlag"]
      """  MatchFlag  """  
      self.ImportedFlag:bool = obj["ImportedFlag"]
      """  ImportedFlag  """  
      self.ProcessedFlag:bool = obj["ProcessedFlag"]
      """  ProcessedFlag  """  
      self.TotalStatementAmt:int = obj["TotalStatementAmt"]
      """  TotalStatementAmt  """  
      self.MatchedAmt:int = obj["MatchedAmt"]
      """  MatchedAmt  """  
      self.UnMatchedAmt:int = obj["UnMatchedAmt"]
      """  UnMatchedAmt  """  
      self.ImportBankCode:str = obj["ImportBankCode"]
      """  ImportBankCode  """  
      self.ImportStmtNbr:str = obj["ImportStmtNbr"]
      """  ImportStmtNbr  """  
      self.ImportBankDate:str = obj["ImportBankDate"]
      """  ImportBankDate  """  
      self.PaymentType:int = obj["PaymentType"]
      """  PaymentType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
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
      self.OkToImport:bool = obj["OkToImport"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToMatch:bool = obj["OkToMatch"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  The availability of Process Group menu item is based on this flag  """  
      self.OkToReport:bool = obj["OkToReport"]
      """  The availability of Report menu item is based on this flag  """  
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
      self.ReadyToMatch:bool = obj["ReadyToMatch"]
      """  the flag to show if imported records are ready for matching  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  the flag to show if imported records are ready for processing  """  
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      """  Bank Branch Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APChkGrpImportListTableset:
   def __init__(self, obj):
      self.APChkGrpImportList:list[Erp_Tablesets_APChkGrpImportListRow] = obj["APChkGrpImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APChkGrpImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  ActiveUserID  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  Cashbook  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  PostErrorLog  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  PostInProcess  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  PromissoryNote  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  EIPaymSent  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """  GrpCreationVia  """  
      self.CompletelyMatched:bool = obj["CompletelyMatched"]
      """  CompletelyMatched  """  
      self.MatchFlag:bool = obj["MatchFlag"]
      """  MatchFlag  """  
      self.ImportedFlag:bool = obj["ImportedFlag"]
      """  ImportedFlag  """  
      self.ProcessedFlag:bool = obj["ProcessedFlag"]
      """  ProcessedFlag  """  
      self.TotalStatementAmt:int = obj["TotalStatementAmt"]
      """  TotalStatementAmt  """  
      self.MatchedAmt:int = obj["MatchedAmt"]
      """  MatchedAmt  """  
      self.UnMatchedAmt:int = obj["UnMatchedAmt"]
      """  UnMatchedAmt  """  
      self.ImportBankCode:str = obj["ImportBankCode"]
      """  ImportBankCode  """  
      self.ImportStmtNbr:str = obj["ImportStmtNbr"]
      """  ImportStmtNbr  """  
      self.ImportBankDate:str = obj["ImportBankDate"]
      """  ImportBankDate  """  
      self.PaymentType:int = obj["PaymentType"]
      """  PaymentType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReadyToMatch:bool = obj["ReadyToMatch"]
      """  the flag to show if imported records are ready for matching  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  the flag to show if imported records are ready for processing  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.OkToImport:bool = obj["OkToImport"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToMatch:bool = obj["OkToMatch"]
      """  The availability of Import File menu item is based on this flag  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  The availability of Process Group menu item is based on this flag  """  
      self.OkToReport:bool = obj["OkToReport"]
      """  The availability of Report menu item is based on this flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIBANCode:str = obj["BankAcctIBANCode"]
      self.BankAcctCurrencyCode:str = obj["BankAcctCurrencyCode"]
      self.BankAcctBankIdentifier:str = obj["BankAcctBankIdentifier"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankBranchCode:str = obj["BankAcctBankBranchCode"]
      self.BankAcctCheckingAccount:str = obj["BankAcctCheckingAccount"]
      self.PayMethodOutputFile:str = obj["PayMethodOutputFile"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPmtMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      self.CheckAmt:int = obj["CheckAmt"]
      self.VendorID:str = obj["VendorID"]
      self.RecordNumber:int = obj["RecordNumber"]
      """  The record number of imported file - used for manual match  """  
      self.CheckDate:str = obj["CheckDate"]
      self.APTRanNo:int = obj["APTRanNo"]
      self.CheckNum:int = obj["CheckNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.APTranImportNo:int = obj["APTranImportNo"]
      """  APTranImportNo  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.TranAmt:int = obj["TranAmt"]
      """  TranAmt  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  DocTranAmt  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  DiscAmt  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  DocDiscAmt  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckNum:int = obj["CheckNum"]
      """  CheckNum  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  GLPosted  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  EntryPerson  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  DocTaxAmt  """  
      self.RefType:str = obj["RefType"]
      """  RefType  """  
      self.RefCode:str = obj["RefCode"]
      """  RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  RefCodeDesc  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  RoundDiff  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Rpt1DiscAmt  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Rpt2DiscAmt  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Rpt3DiscAmt  """  
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
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  GetDfltTaxIds  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
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
      self.RedStorno:bool = obj["RedStorno"]
      """  RedStorno  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  PrePayment  """  
      self.ContractRef:str = obj["ContractRef"]
      """  ContractRef  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  ContractRefDate  """  
      self.RefPONum:int = obj["RefPONum"]
      """  RefPONum  """  
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
      self.BankID:str = obj["BankID"]
      """  BankID  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  BankPaidAmt  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  DocBankPaidAmt  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Rpt1BankPaidAmt  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Rpt2BankPaidAmt  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Rpt3BankPaidAmt  """  
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  AdjLegalNumber  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  AdjTranDocTypeID  """  
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
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  AssetTypeCode  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  CreditCard  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  CardID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  CardHolderTaxID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  CardMemberName  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
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
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class Erp_Tablesets_CheckHedImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.CheckNum:int = obj["CheckNum"]
      """  CheckNum  """  
      self.CheckDate:str = obj["CheckDate"]
      """  CheckDate  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.Voided:bool = obj["Voided"]
      """  Voided  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  CheckSrc  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  ClearedCheck  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  ClearedPending  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  ClearedAmt  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  DocClearedAmt  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  ClearedPerson  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  ClearedDate  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  ClearedTime  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  ClearedStmtEndDate  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  CheckAmt  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  DocCheckAmt  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  ManualPrint  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  EntryPerson  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State  """  
      self.ZIP:str = obj["ZIP"]
      """  ZIP  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  ExchangeRate  """  
      self.CountryNum:int = obj["CountryNum"]
      """  CountryNum  """  
      self.BankSlip:str = obj["BankSlip"]
      """  BankSlip  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  ElecPayment  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  VendorBankID  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  VendorBankName  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  VendorBankNameOnAccount  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  VendorBankAddress1  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  VendorBankAddress2  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  VendorBankAddress3  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  VendorBankCity  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  VendorBankState  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  VendorBankPostalCode  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  VendorBankCountryNum  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  VendorBankAcctNumber  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  VendorBankSwiftNum  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  CashBookNum  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  CashbookLine  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  XRefCheckNum  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Rpt1CheckAmt  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Rpt2CheckAmt  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Rpt3CheckAmt  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Rpt1ClearedAmt  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Rpt2ClearedAmt  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Rpt3ClearedAmt  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  RateGrpCode  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  PaymentTotal  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  DocPaymentTotal  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Rpt1PaymentTotal  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Rpt2PaymentTotal  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Rpt3PaymentTotal  """  
      self.Variance:int = obj["Variance"]
      """  Variance  """  
      self.DocVariance:int = obj["DocVariance"]
      """  DocVariance  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Rpt1Variance  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Rpt2Variance  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Rpt3Variance  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  PaymentBankRate  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  BankTotalAmt  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  IsEnterTotal  """  
      self.LockRate:int = obj["LockRate"]
      """  LockRate  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  ReadyToCalc  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  RecalcBeforePost  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  UsePendAcct  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  ForceDiscount  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  FirstHeadNum  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  ApplyingPayment  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  PCashDeskID  """  
      self.BankTranID:str = obj["BankTranID"]
      """  BankTranID  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  PCashRefNum  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  BankPaidAmt  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  DocBankPaidAmt  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Rpt1BankPaidAmt  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Rpt2BankPaidAmt  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Rpt3BankPaidAmt  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  BankTransDate  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusDesc  """  
      self.TransText:str = obj["TransText"]
      """  TransText  """  
      self.TransDetail:str = obj["TransDetail"]
      """  TransDetail  """  
      self.OrigInvoiceNum:str = obj["OrigInvoiceNum"]
      """  OrigInvoiceNum  """  
      self.OrigName:str = obj["OrigName"]
      """  OrigName  """  
      self.OrigVendorID:str = obj["OrigVendorID"]
      """  OrigVendorID  """  
      self.PropGroupID:str = obj["PropGroupID"]
      """  PropGroupID  """  
      self.NumPayment:int = obj["NumPayment"]
      """  NumPayment  """  
      self.CheckHeadNum:int = obj["CheckHeadNum"]
      """  CheckHeadNum  """  
      self.OrigVendorNum:int = obj["OrigVendorNum"]
      """  OrigVendorNum  """  
      self.Matched:bool = obj["Matched"]
      """  Matched  """  
      self.OKToMatch:bool = obj["OKToMatch"]
      """  OKToMatch  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SavedInvoiceNum:str = obj["SavedInvoiceNum"]
      """  SavedInvoiceNum  """  
      self.SavedVendorName:str = obj["SavedVendorName"]
      """  SavedVendorName  """  
      self.SavedVendorID:str = obj["SavedVendorID"]
      """  SavedVendorID  """  
      self.SavedVendorNum:int = obj["SavedVendorNum"]
      """  SavedVendorNum  """  
      self.CheckStatus:int = obj["CheckStatus"]
      """  CheckStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.NOPaymentDirection:str = obj["NOPaymentDirection"]
      """  NOPaymentDirection  """  
      self.NOPaymentType:str = obj["NOPaymentType"]
      """  NOPaymentType  """  
      self.NOTransferFileName:str = obj["NOTransferFileName"]
      """  NOTransferFileName  """  
      self.NOBankTransRef:str = obj["NOBankTransRef"]
      """  NOBankTransRef  """  
      self.BalanceUpdate:int = obj["BalanceUpdate"]
      """  BalanceUpdate  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  BOEInvoiceNum  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MsgId:str = obj["MsgId"]
      """  MsgId  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.PayTranDocTypeID:str = obj["PayTranDocTypeID"]
      """  PayTranDocTypeID  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.TaxPaymInfo:str = obj["TaxPaymInfo"]
      """  TaxPaymInfo  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  VoidLegalNumber  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  VoidTranDocTypeID  """  
      self.SEGrpNum:int = obj["SEGrpNum"]
      """  SEGrpNum  """  
      self.SEReference:str = obj["SEReference"]
      """  SEReference  """  
      self.SEISGroupedPO3:bool = obj["SEISGroupedPO3"]
      """  SEISGroupedPO3  """  
      self.SEISExported:bool = obj["SEISExported"]
      """  SEISExported  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MXBankAcctNumber:str = obj["MXBankAcctNumber"]
      """  MXBankAcctNumber  """  
      self.MXBankIdentifier:str = obj["MXBankIdentifier"]
      """  MXBankIdentifier  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  BankBatchExcluded  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.SEPAPaymentDescription:str = obj["SEPAPaymentDescription"]
      """  SEPAPaymentDescription  """  
      self.NOImportErrors:str = obj["NOImportErrors"]
      """  NOImportErrors  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  THRefInvoiceNum  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  THRefVendorNum  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  VoidedReason  """  
      self.RegulatoryReportingCode:str = obj["RegulatoryReportingCode"]
      """  RegulatoryReportingCode  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  TaxPointDate  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACHTranCode  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  US1099KMerchCatCode  """  
      self.US1099KGen:bool = obj["US1099KGen"]
      """  US1099KGen  """  
      self.VendorBankBranchCode:str = obj["VendorBankBranchCode"]
      """  VendorBankBranchCode  """  
      self.NettingID:int = obj["NettingID"]
      """  NettingID  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  GL Description for the Payment Voiding process  """  
      self.DMDescription:str = obj["DMDescription"]
      """  GL Description for AP - Apply Debit Memo/Prepayment  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  MXDIOTTranType  """  
      self.TransDetail1:str = obj["TransDetail1"]
      """  Transaction Detail, part 1  """  
      self.TransDetail3:str = obj["TransDetail3"]
      """  Transactoin Detail part 3  """  
      self.TransDetail4:str = obj["TransDetail4"]
      """  Transaction Detail part 4  """  
      self.UnderpayFlag:bool = obj["UnderpayFlag"]
      """  Indicates if the amount of payment from the imported file is less than amount of  proposed  payment  """  
      self.OverpayFlag:bool = obj["OverpayFlag"]
      """  Indicates if the amount of payment from the imported file is more than amount of  proposed  payment  """  
      self.TransDetail2:str = obj["TransDetail2"]
      """  Transaction Detail, Part2  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckHedMatchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.Name:str = obj["Name"]
      """  Supplier Name  """  
      self.GroupID:str = obj["GroupID"]
      """  Payment Group ID  """  
      self.PrpGroupID:str = obj["PrpGroupID"]
      """  Group ID of the proposed Payment  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum of the CheckHed matched  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number for the payment matched  """  
      self.APTranNo:int = obj["APTranNo"]
      self.CheckDate:str = obj["CheckDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the payment  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Payment amount  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount in Document currency  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      self.RecordNumber:int = obj["RecordNumber"]
      """  Record number of the imported table matched  """  
      self.Matched:str = obj["Matched"]
      self.CheckNum:int = obj["CheckNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPBankFileImportTableset:
   def __init__(self, obj):
      self.APChkGrpImport:list[Erp_Tablesets_APChkGrpImportRow] = obj["APChkGrpImport"]
      self.APChkGrpImportAttch:list[Erp_Tablesets_APChkGrpImportAttchRow] = obj["APChkGrpImportAttch"]
      self.CheckHedImport:list[Erp_Tablesets_CheckHedImportRow] = obj["CheckHedImport"]
      self.APTranImport:list[Erp_Tablesets_APTranImportRow] = obj["APTranImport"]
      self.APPmtMatch:list[Erp_Tablesets_APPmtMatchRow] = obj["APPmtMatch"]
      self.CheckHedMatched:list[Erp_Tablesets_CheckHedMatchedRow] = obj["CheckHedMatched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBankFileImportParam_input:
   """ Required : 
   cGroupID
   """  
   def __init__(self, obj):
      self.cGroupID:str = obj["cGroupID"]
      """  The Payment Group ID  """  
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
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_APChkGrpImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPChkGrpImportAttch_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewAPChkGrpImportAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPChkGrpImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class GetNewAPChkGrpImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPTranImport_input:
   """ Required : 
   ds
   headNum
   apTranImportNo
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.apTranImportNo:int = obj["apTranImportNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPTranImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCheckHedImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class GetNewCheckHedImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPChkGrpImport
   whereClauseAPChkGrpImportAttch
   whereClauseCheckHedImport
   whereClauseAPTranImport
   whereClauseAPPmtMatch
   whereClauseCheckHedMatched
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPChkGrpImport:str = obj["whereClauseAPChkGrpImport"]
      self.whereClauseAPChkGrpImportAttch:str = obj["whereClauseAPChkGrpImportAttch"]
      self.whereClauseCheckHedImport:str = obj["whereClauseCheckHedImport"]
      self.whereClauseAPTranImport:str = obj["whereClauseAPTranImport"]
      self.whereClauseAPPmtMatch:str = obj["whereClauseAPPmtMatch"]
      self.whereClauseCheckHedMatched:str = obj["whereClauseCheckHedMatched"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetStatement_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID  """  
      pass

class GetStatement_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
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

class ImportBankFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankFileImportParamTableset] = obj["ds"]
      pass

class ImportBankFile_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
      pass

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

class MatchPayments_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      pass

class MatchPayments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
      pass

class MatchTelepayPayments_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  Group ID of the payment  """  
      pass

class MatchTelepayPayments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APBankFileImportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnEnterGroupID_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID of the paymnet  """  
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class OnEnterGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessPayments_input:
   """ Required : 
   pcGroupID
   ds
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  Group ID of the paymnet  """  
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class ProcessPayments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.ds:list[Erp_Tablesets_UpdExtAPBankFileImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPBankFileImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APBankFileImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

