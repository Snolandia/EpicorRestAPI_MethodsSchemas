import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ImportMgmtSvc
# Description: ImportMgmtSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ImportMgmts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportMgmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportMgmts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts",headers=creds) as resp:
           return await resp.json()

async def post_ImportMgmts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportMgmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportMgmts_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportMgmt item
   Description: Calls GetByID to retrieve the ImportMgmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportMgmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportMgmts_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportMgmt for the service
   Description: Calls UpdateExt to update ImportMgmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportMgmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportMgmts_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportMgmt item
   Description: Call UpdateExt to delete ImportMgmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportMgmt
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportMgmts_Company_GroupID_ImportFiles(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportFiles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportFiles1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")/ImportFiles",headers=creds) as resp:
           return await resp.json()

async def get_ImportMgmts_Company_GroupID_ImportFiles_Company_GroupID_FileID(Company, GroupID, FileID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportFile item
   Description: Calls GetByID to retrieve the ImportFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportFile1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportMgmts(" + Company + "," + GroupID + ")/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportFiles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles",headers=creds) as resp:
           return await resp.json()

async def post_ImportFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles_Company_GroupID_FileID(Company, GroupID, FileID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportFile item
   Description: Calls GetByID to retrieve the ImportFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportFile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportFiles_Company_GroupID_FileID(Company, GroupID, FileID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportFile for the service
   Description: Calls UpdateExt to update ImportFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportFile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportFiles_Company_GroupID_FileID(Company, GroupID, FileID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportFile item
   Description: Call UpdateExt to delete ImportFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportFile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles_Company_GroupID_FileID_ImportDocuments(Company, GroupID, FileID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportDocuments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportDocuments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportDocumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportDocuments",headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles_Company_GroupID_FileID_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company, GroupID, FileID, DocumentNumber, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportDocument item
   Description: Calls GetByID to retrieve the ImportDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportDocument1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles_Company_GroupID_FileID_ImportExecutionPlans(Company, GroupID, FileID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportExecutionPlans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportExecutionPlans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportExecutionPlans",headers=creds) as resp:
           return await resp.json()

async def get_ImportFiles_Company_GroupID_FileID_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportExecutionPlan item
   Description: Calls GetByID to retrieve the ImportExecutionPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlan1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportFiles(" + Company + "," + GroupID + "," + FileID + ")/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportDocuments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportDocuments
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportDocumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments",headers=creds) as resp:
           return await resp.json()

async def post_ImportDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company, GroupID, FileID, DocumentNumber, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportDocument item
   Description: Calls GetByID to retrieve the ImportDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company, GroupID, FileID, DocumentNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportDocument for the service
   Description: Calls UpdateExt to update ImportDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportDocumentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportDocuments_Company_GroupID_FileID_DocumentNumber(Company, GroupID, FileID, DocumentNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportDocument item
   Description: Call UpdateExt to delete ImportDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportDocument
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportDocuments_Company_GroupID_FileID_DocumentNumber_ImportTasks(Company, GroupID, FileID, DocumentNumber, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportTasks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportTasks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")/ImportTasks",headers=creds) as resp:
           return await resp.json()

async def get_ImportDocuments_Company_GroupID_FileID_DocumentNumber_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportTask item
   Description: Calls GetByID to retrieve the ImportTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTask1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportDocuments(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + ")/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportTasks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportTasks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportTasks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks",headers=creds) as resp:
           return await resp.json()

async def post_ImportTasks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportTask item
   Description: Calls GetByID to retrieve the ImportTask item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportTask for the service
   Description: Calls UpdateExt to update ImportTask. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportTask item
   Description: Call UpdateExt to delete ImportTask item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportTask
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_ImportTaskLogs(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportTaskLogs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportTaskLogs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")/ImportTaskLogs",headers=creds) as resp:
           return await resp.json()

async def get_ImportTasks_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, LogID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportTaskLog item
   Description: Calls GetByID to retrieve the ImportTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTaskLog1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param LogID: Desc: LogID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTasks(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + ")/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportTaskLogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportTaskLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportTaskLogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs",headers=creds) as resp:
           return await resp.json()

async def post_ImportTaskLogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportTaskLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, LogID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportTaskLog item
   Description: Calls GetByID to retrieve the ImportTaskLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportTaskLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param LogID: Desc: LogID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, LogID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportTaskLog for the service
   Description: Calls UpdateExt to update ImportTaskLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportTaskLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param LogID: Desc: LogID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportTaskLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportTaskLogs_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_TaskID_LogID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, TaskID, LogID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportTaskLog item
   Description: Call UpdateExt to delete ImportTaskLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportTaskLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param TaskID: Desc: TaskID   Required: True   Allow empty value : True
      :param LogID: Desc: LogID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportTaskLogs(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + TaskID + "," + LogID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportExecutionPlans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportExecutionPlans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans",headers=creds) as resp:
           return await resp.json()

async def post_ImportExecutionPlans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportExecutionPlans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportExecutionPlan item
   Description: Calls GetByID to retrieve the ImportExecutionPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportExecutionPlan for the service
   Description: Calls UpdateExt to update ImportExecutionPlan. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportExecutionPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportExecutionPlan item
   Description: Call UpdateExt to delete ImportExecutionPlan item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportExecutionPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_ImportExecutionPlanDependencies(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ImportExecutionPlanDependencies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ImportExecutionPlanDependencies1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanDependencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")/ImportExecutionPlanDependencies",headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlans_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, DependsOn, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportExecutionPlanDependency item
   Description: Calls GetByID to retrieve the ImportExecutionPlanDependency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlanDependency1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param DependsOn: Desc: DependsOn   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlans(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + ")/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlanDependencies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportExecutionPlanDependencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportExecutionPlanDependencies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportExecutionPlanDependencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies",headers=creds) as resp:
           return await resp.json()

async def post_ImportExecutionPlanDependencies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportExecutionPlanDependencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, DependsOn, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportExecutionPlanDependency item
   Description: Calls GetByID to retrieve the ImportExecutionPlanDependency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportExecutionPlanDependency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param DependsOn: Desc: DependsOn   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, DependsOn, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportExecutionPlanDependency for the service
   Description: Calls UpdateExt to update ImportExecutionPlanDependency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportExecutionPlanDependency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param DependsOn: Desc: DependsOn   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ImportExecutionPlanDependencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportExecutionPlanDependencies_Company_GroupID_FileID_DocumentNumber_ExecutionPlanID_DependsOn(Company, GroupID, FileID, DocumentNumber, ExecutionPlanID, DependsOn, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportExecutionPlanDependency item
   Description: Call UpdateExt to delete ImportExecutionPlanDependency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportExecutionPlanDependency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param FileID: Desc: FileID   Required: True   Allow empty value : True
      :param DocumentNumber: Desc: DocumentNumber   Required: True   Allow empty value : True
      :param ExecutionPlanID: Desc: ExecutionPlanID   Required: True   Allow empty value : True
      :param DependsOn: Desc: DependsOn   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/ImportExecutionPlanDependencies(" + Company + "," + GroupID + "," + FileID + "," + DocumentNumber + "," + ExecutionPlanID + "," + DependsOn + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ImportGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseImportGroup, whereClauseImportFile, whereClauseImportDocument, whereClauseImportTask, whereClauseImportTaskLog, whereClauseImportExecutionPlan, whereClauseImportExecutionPlanDependency, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseImportGroup=" + whereClauseImportGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportFile=" + whereClauseImportFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportDocument=" + whereClauseImportDocument
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportTask=" + whereClauseImportTask
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportTaskLog=" + whereClauseImportTaskLog
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportExecutionPlan=" + whereClauseImportExecutionPlan
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseImportExecutionPlanDependency=" + whereClauseImportExecutionPlanDependency
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGroup
   Description: GetNewGroup - generates a new group
   OperationID: GetNewGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFile
   Description: creates a new file and a Group if needed
   OperationID: GetNewFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadFilesAndImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadFilesAndImport
   Description: Upload files And launches the import proces
   OperationID: UploadFilesAndImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFilesAndImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFilesAndImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIntQueID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIntQueID
   Description: get IntQueID for the Document we want to edit in Workbench
   OperationID: GetIntQueID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIntQueID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIntQueID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelImport
   Description: CancelImport method - this method calls cancel method from Import BO
   OperationID: CancelImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PauseImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PauseImport
   Description: PauseImport method - this method calls pause method from Import BO
   OperationID: PauseImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PauseImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PauseImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RestartImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RestartImport
   Description: RestartImport method - this method calls restart method from Import BO
   OperationID: RestartImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RestartImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestartImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportFile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportDocument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportDocument
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportTaskLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportTaskLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportTaskLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportTaskLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportTaskLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportExecutionPlan(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportExecutionPlan
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportExecutionPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportExecutionPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportExecutionPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportExecutionPlanDependency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportExecutionPlanDependency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportExecutionPlanDependency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportExecutionPlanDependency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportExecutionPlanDependency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ImportMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportDocumentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportDocumentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanDependencyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportExecutionPlanDependencyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportExecutionPlanRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportExecutionPlanRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportFileRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskLogRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportTaskLogRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ImportTaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ImportTaskRow] = obj["value"]
      pass

class Ice_Tablesets_ImportDocumentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Displays the Epicor system group used for the selected program. Epicor programs either belong to the application system (ERP) or the tools system (ICE).  """  
      self.ClassName:str = obj["ClassName"]
      """  Defines the class of the document, such Sales Order, Purchase Order, AR Invoice, etc.  """  
      self.DocumentType:str = obj["DocumentType"]
      """  Specifies the document type name that describes a particular shape of a document of the current class name, i.e. a Contract Sales Order from the class name Sales Order.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NumOfInputRows:int = obj["NumOfInputRows"]
      """  The number of rows contained in the document.  """  
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.Duration:int = obj["Duration"]
      """  Time spent on executing all document import calls.  """  
      self.PrimaryKey:str = obj["PrimaryKey"]
      """  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  """  
      self.NavDescription:str = obj["NavDescription"]
      """  column used only to be displayed on navigation controls.  """  
      self.NavFullDescription:str = obj["NavFullDescription"]
      """  column used only to be displayed on navigation controls.  """  
      self.ExistsIntQueIn:bool = obj["ExistsIntQueIn"]
      self.CancelledTasks:int = obj["CancelledTasks"]
      self.FailedTasks:int = obj["FailedTasks"]
      self.PausedTasks:int = obj["PausedTasks"]
      self.RowsPerMinute:int = obj["RowsPerMinute"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportExecutionPlanDependencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  ExecutionPlanID  """  
      self.DependsOn:int = obj["DependsOn"]
      """  Defines if the execution plan depends on other execution plans  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportExecutionPlanRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.ExecutionBlockID:int = obj["ExecutionBlockID"]
      """  Defines a block of execution plans that will run together in an isolated way, if multiple blocks exist per file they can potentially run in parallel  """  
      self.ExecutionAction:str = obj["ExecutionAction"]
      """  Defines the name of the method that would be executed on the current file and document combination  """  
      self.TaskSeq:int = obj["TaskSeq"]
      """  Defines the sequence on which the tasks of a block can potentially run as, ordered always in ascending order  """  
      self.Status:str = obj["Status"]
      """  defines the status of the current execution plan row, valid statuses are Pending, Processing, Completed, Paused, Cancelled and Error  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FileName:str = obj["FileName"]
      self.StartedEnded:str = obj["StartedEnded"]
      self.BitFlag:int = obj["BitFlag"]
      self.ImportTaskLinkStartedOn:str = obj["ImportTaskLinkStartedOn"]
      self.ImportTaskLinkDuration:int = obj["ImportTaskLinkDuration"]
      self.ImportTaskLinkEndedOn:str = obj["ImportTaskLinkEndedOn"]
      self.ImportTaskLinkNumOfInputRows:int = obj["ImportTaskLinkNumOfInputRows"]
      self.ImportTaskLinkPrimaryKey:str = obj["ImportTaskLinkPrimaryKey"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportFileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.Comments:str = obj["Comments"]
      """  Available if specified in the imported file, this field displays additional comments that defines importing needs about this file. These comments might include special file instructions, comments to the imported sales order sales order or other information that needs to be included.  """  
      self.FileName:str = obj["FileName"]
      """  Displays the directory path and filename for the imported file. By default, the file format is limited to JavaScript Object Notation (*.json) and Extensible Markup Language (*.xml).  """  
      self.Size:int = obj["Size"]
      """  Displays the size of the imported file in megabytes (MB).  """  
      self.UploadStatus:str = obj["UploadStatus"]
      """  Displays the current status of a file, valid statuses are PENDING,ERROR,COMPLETE.  """  
      self.NumberOfDocuments:int = obj["NumberOfDocuments"]
      """  Specifies the total number of documents in the imported file. A file may contain one or more documents. Each document must include a header (i.e. sales order header) and details (i.e. sales order lines).  """  
      self.ContinueProcessingOnError:bool = obj["ContinueProcessingOnError"]
      """  Determines how the process should proceed when an error is caught during the import process. Select this check box to skip the error entry and continue processing.  """  
      self.RollbackParentOnChildError:bool = obj["RollbackParentOnChildError"]
      """  Select this check box to roll back parent on child error.  """  
      self.RunSynchronously:bool = obj["RunSynchronously"]
      """  Select this check box to toggle between synchronous and asynchronous file execution. If you run the file synchronously, this file is processed immediately when the remaining files you have uploaded in the Upload sheet execute. Asynchronous execution means the call is executed immediately, but the action does not wait until the remaining files are finished and the results are processed.  """  
      self.OverrideCompany:str = obj["OverrideCompany"]
      """  Overrides the default company retrieved from the imported file that displays in the Company field in the Company Maintenance program.  """  
      self.OverridePlant:str = obj["OverridePlant"]
      """  Overrides the default plant retrieved from the imported file.  """  
      self.OverrideLanguage:str = obj["OverrideLanguage"]
      """  Overrides the default language retrieved from the imported file that displays in the Language ID field in the Language Maintenance program.  """  
      self.OverrideFormatCulture:str = obj["OverrideFormatCulture"]
      """  Overrides the default format culture retrieved from the imported file. Use the Format Culture drop-down list to select the culture code you want to define for this user. The culture code defines the interface and data format for a specific world culture. When you select a culture code for a user account, this specific user views and enters data in the method appropriate for the selected culture.  """  
      self.OverrideSchemaName:str = obj["OverrideSchemaName"]
      """  Override the default schema name of the imported file.  """  
      self.ImportSettings:str = obj["ImportSettings"]
      """  Contains a copy of the ImportSettings used by the current import file, describes the alternate settings that a user can override.  """  
      self.Formatter:str = obj["Formatter"]
      """  Describes the current specialized formatter used to parse the current file contents, by default GenericJSON and GenericXML are the valid values, customized formatters will be described in this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FormatName:str = obj["FormatName"]
      """  FormatName  """  
      self.FilePath:str = obj["FilePath"]
      self.FileExtension:str = obj["FileExtension"]
      self.ImportedDocuments:int = obj["ImportedDocuments"]
      """  the number of imported doucments  """  
      self.FailedDocuments:int = obj["FailedDocuments"]
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.StartedEnded:str = obj["StartedEnded"]
      self.TimeLeft:int = obj["TimeLeft"]
      self.ProgressPercent:int = obj["ProgressPercent"]
      self.RowsPerMinute:int = obj["RowsPerMinute"]
      self.Duration:int = obj["Duration"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  identification number of the group of the imported files  """  
      self.Description:str = obj["Description"]
      """  Further identifies each group.  """  
      self.Status:str = obj["Status"]
      """  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  identification number of the group of the imported files  """  
      self.Description:str = obj["Description"]
      """  Further identifies each group.  """  
      self.Status:str = obj["Status"]
      """  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportTaskLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.TaskID:int = obj["TaskID"]
      """  Displays the sequence number of the task.  """  
      self.LogID:int = obj["LogID"]
      """  Displays the sequence number of the log  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  Displays the date and time on which the task was started.  """  
      self.Error:bool = obj["Error"]
      """  When selected, specifies an error occurred during document import processing. Click the Message field to display additional information about the error.  """  
      self.ErrorTableName:str = obj["ErrorTableName"]
      """  Displays the name of the system table where the error occurred.  """  
      self.ErrorRowNum:int = obj["ErrorRowNum"]
      """  Displays the row number where the import failed  """  
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      """  this identifier should match with RowGuid field from  ice.ImportKeyValueStore, it is used to display the rows on Integration Workbench  """  
      self.Message:str = obj["Message"]
      """  An import process passes through different statuses during its lifecycle. Message information displays as the document is processing.  """  
      self.MessageType:str = obj["MessageType"]
      """  Displays the type of the message. The following types are available are Informational and Error  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FileName:str = obj["FileName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ImportExecutionPlanLinkExecutionAction:str = obj["ImportExecutionPlanLinkExecutionAction"]
      self.PrimaryKeyPrimaryKey:str = obj["PrimaryKeyPrimaryKey"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportTaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.TaskID:int = obj["TaskID"]
      """  Displays the sequence number of the task.  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Displays the date and time on which the task was started.  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Displays the date and time on which the task finished.  """  
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.NumOfInputRows:int = obj["NumOfInputRows"]
      """  The number of rows contained in the document.  """  
      self.UserID:str = obj["UserID"]
      """  Identifies the user who submitted, or launched the import task.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Displays the identification number of the process.  """  
      self.ThreadID:int = obj["ThreadID"]
      """  Indicates which thread from the application server was used to run the call.  """  
      self.ServerName:str = obj["ServerName"]
      """  Defines the specific name for the server from which you capture the logs.  """  
      self.PrimaryKey:str = obj["PrimaryKey"]
      """  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  """  
      self.Duration:int = obj["Duration"]
      """  Time spent on executing a document import call.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspTaskName:str = obj["DspTaskName"]
      """  field to shorten the link field ExecutionAction and display it on UI bavigation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActionNameExecutionAction:str = obj["ActionNameExecutionAction"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CancelImport_input:
   """ Required : 
   Company
   GroupID
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:int = obj["GroupID"]
      pass

class CancelImport_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:int = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:int = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ImportMgmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ImportMgmtTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ImportMgmtTableset] = obj["returnObj"]
      pass

class GetIntQueID_input:
   """ Required : 
   company
   groupID
   fileID
   documentNumber
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.groupID:str = obj["groupID"]
      self.fileID:str = obj["fileID"]
      self.documentNumber:str = obj["documentNumber"]
      pass

class GetIntQueID_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ImportMgmtListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFile_input:
   """ Required : 
   FilePath
   GroupID
   ds
   """  
   def __init__(self, obj):
      self.FilePath:str = obj["FilePath"]
      self.GroupID:int = obj["GroupID"]
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

class GetNewFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

class GetNewGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportDocument_input:
   """ Required : 
   ds
   groupID
   fileID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      pass

class GetNewImportDocument_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportExecutionPlanDependency_input:
   """ Required : 
   ds
   groupID
   fileID
   documentNumber
   executionPlanID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      self.documentNumber:int = obj["documentNumber"]
      self.executionPlanID:int = obj["executionPlanID"]
      pass

class GetNewImportExecutionPlanDependency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportExecutionPlan_input:
   """ Required : 
   ds
   groupID
   fileID
   documentNumber
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      self.documentNumber:int = obj["documentNumber"]
      pass

class GetNewImportExecutionPlan_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportFile_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      pass

class GetNewImportFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

class GetNewImportGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportTaskLog_input:
   """ Required : 
   ds
   groupID
   fileID
   documentNumber
   executionPlanID
   taskID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      self.documentNumber:int = obj["documentNumber"]
      self.executionPlanID:int = obj["executionPlanID"]
      self.taskID:int = obj["taskID"]
      pass

class GetNewImportTaskLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportTask_input:
   """ Required : 
   ds
   groupID
   fileID
   documentNumber
   executionPlanID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      self.documentNumber:int = obj["documentNumber"]
      self.executionPlanID:int = obj["executionPlanID"]
      pass

class GetNewImportTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseImportGroup
   whereClauseImportFile
   whereClauseImportDocument
   whereClauseImportTask
   whereClauseImportTaskLog
   whereClauseImportExecutionPlan
   whereClauseImportExecutionPlanDependency
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseImportGroup:str = obj["whereClauseImportGroup"]
      self.whereClauseImportFile:str = obj["whereClauseImportFile"]
      self.whereClauseImportDocument:str = obj["whereClauseImportDocument"]
      self.whereClauseImportTask:str = obj["whereClauseImportTask"]
      self.whereClauseImportTaskLog:str = obj["whereClauseImportTaskLog"]
      self.whereClauseImportExecutionPlan:str = obj["whereClauseImportExecutionPlan"]
      self.whereClauseImportExecutionPlanDependency:str = obj["whereClauseImportExecutionPlanDependency"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ImportMgmtTableset] = obj["returnObj"]
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

class Ice_Tablesets_ImportDocumentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Displays the Epicor system group used for the selected program. Epicor programs either belong to the application system (ERP) or the tools system (ICE).  """  
      self.ClassName:str = obj["ClassName"]
      """  Defines the class of the document, such Sales Order, Purchase Order, AR Invoice, etc.  """  
      self.DocumentType:str = obj["DocumentType"]
      """  Specifies the document type name that describes a particular shape of a document of the current class name, i.e. a Contract Sales Order from the class name Sales Order.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NumOfInputRows:int = obj["NumOfInputRows"]
      """  The number of rows contained in the document.  """  
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.Duration:int = obj["Duration"]
      """  Time spent on executing all document import calls.  """  
      self.PrimaryKey:str = obj["PrimaryKey"]
      """  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  """  
      self.NavDescription:str = obj["NavDescription"]
      """  column used only to be displayed on navigation controls.  """  
      self.NavFullDescription:str = obj["NavFullDescription"]
      """  column used only to be displayed on navigation controls.  """  
      self.ExistsIntQueIn:bool = obj["ExistsIntQueIn"]
      self.CancelledTasks:int = obj["CancelledTasks"]
      self.FailedTasks:int = obj["FailedTasks"]
      self.PausedTasks:int = obj["PausedTasks"]
      self.RowsPerMinute:int = obj["RowsPerMinute"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportExecutionPlanDependencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  ExecutionPlanID  """  
      self.DependsOn:int = obj["DependsOn"]
      """  Defines if the execution plan depends on other execution plans  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportExecutionPlanRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.ExecutionBlockID:int = obj["ExecutionBlockID"]
      """  Defines a block of execution plans that will run together in an isolated way, if multiple blocks exist per file they can potentially run in parallel  """  
      self.ExecutionAction:str = obj["ExecutionAction"]
      """  Defines the name of the method that would be executed on the current file and document combination  """  
      self.TaskSeq:int = obj["TaskSeq"]
      """  Defines the sequence on which the tasks of a block can potentially run as, ordered always in ascending order  """  
      self.Status:str = obj["Status"]
      """  defines the status of the current execution plan row, valid statuses are Pending, Processing, Completed, Paused, Cancelled and Error  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FileName:str = obj["FileName"]
      self.StartedEnded:str = obj["StartedEnded"]
      self.BitFlag:int = obj["BitFlag"]
      self.ImportTaskLinkStartedOn:str = obj["ImportTaskLinkStartedOn"]
      self.ImportTaskLinkDuration:int = obj["ImportTaskLinkDuration"]
      self.ImportTaskLinkEndedOn:str = obj["ImportTaskLinkEndedOn"]
      self.ImportTaskLinkNumOfInputRows:int = obj["ImportTaskLinkNumOfInputRows"]
      self.ImportTaskLinkPrimaryKey:str = obj["ImportTaskLinkPrimaryKey"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportFileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.Comments:str = obj["Comments"]
      """  Available if specified in the imported file, this field displays additional comments that defines importing needs about this file. These comments might include special file instructions, comments to the imported sales order sales order or other information that needs to be included.  """  
      self.FileName:str = obj["FileName"]
      """  Displays the directory path and filename for the imported file. By default, the file format is limited to JavaScript Object Notation (*.json) and Extensible Markup Language (*.xml).  """  
      self.Size:int = obj["Size"]
      """  Displays the size of the imported file in megabytes (MB).  """  
      self.UploadStatus:str = obj["UploadStatus"]
      """  Displays the current status of a file, valid statuses are PENDING,ERROR,COMPLETE.  """  
      self.NumberOfDocuments:int = obj["NumberOfDocuments"]
      """  Specifies the total number of documents in the imported file. A file may contain one or more documents. Each document must include a header (i.e. sales order header) and details (i.e. sales order lines).  """  
      self.ContinueProcessingOnError:bool = obj["ContinueProcessingOnError"]
      """  Determines how the process should proceed when an error is caught during the import process. Select this check box to skip the error entry and continue processing.  """  
      self.RollbackParentOnChildError:bool = obj["RollbackParentOnChildError"]
      """  Select this check box to roll back parent on child error.  """  
      self.RunSynchronously:bool = obj["RunSynchronously"]
      """  Select this check box to toggle between synchronous and asynchronous file execution. If you run the file synchronously, this file is processed immediately when the remaining files you have uploaded in the Upload sheet execute. Asynchronous execution means the call is executed immediately, but the action does not wait until the remaining files are finished and the results are processed.  """  
      self.OverrideCompany:str = obj["OverrideCompany"]
      """  Overrides the default company retrieved from the imported file that displays in the Company field in the Company Maintenance program.  """  
      self.OverridePlant:str = obj["OverridePlant"]
      """  Overrides the default plant retrieved from the imported file.  """  
      self.OverrideLanguage:str = obj["OverrideLanguage"]
      """  Overrides the default language retrieved from the imported file that displays in the Language ID field in the Language Maintenance program.  """  
      self.OverrideFormatCulture:str = obj["OverrideFormatCulture"]
      """  Overrides the default format culture retrieved from the imported file. Use the Format Culture drop-down list to select the culture code you want to define for this user. The culture code defines the interface and data format for a specific world culture. When you select a culture code for a user account, this specific user views and enters data in the method appropriate for the selected culture.  """  
      self.OverrideSchemaName:str = obj["OverrideSchemaName"]
      """  Override the default schema name of the imported file.  """  
      self.ImportSettings:str = obj["ImportSettings"]
      """  Contains a copy of the ImportSettings used by the current import file, describes the alternate settings that a user can override.  """  
      self.Formatter:str = obj["Formatter"]
      """  Describes the current specialized formatter used to parse the current file contents, by default GenericJSON and GenericXML are the valid values, customized formatters will be described in this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FormatName:str = obj["FormatName"]
      """  FormatName  """  
      self.FilePath:str = obj["FilePath"]
      self.FileExtension:str = obj["FileExtension"]
      self.ImportedDocuments:int = obj["ImportedDocuments"]
      """  the number of imported doucments  """  
      self.FailedDocuments:int = obj["FailedDocuments"]
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.StartedEnded:str = obj["StartedEnded"]
      self.TimeLeft:int = obj["TimeLeft"]
      self.ProgressPercent:int = obj["ProgressPercent"]
      self.RowsPerMinute:int = obj["RowsPerMinute"]
      self.Duration:int = obj["Duration"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  identification number of the group of the imported files  """  
      self.Description:str = obj["Description"]
      """  Further identifies each group.  """  
      self.Status:str = obj["Status"]
      """  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  identification number of the group of the imported files  """  
      self.Description:str = obj["Description"]
      """  Further identifies each group.  """  
      self.Status:str = obj["Status"]
      """  Displays the current status of a group, either OPEN or CLOSED; the group remains open until the user performs an upload or defaults to CLOSED when the Rest endpoint is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportMgmtListTableset:
   def __init__(self, obj):
      self.ImportGroupList:list[Ice_Tablesets_ImportGroupListRow] = obj["ImportGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ImportMgmtTableset:
   def __init__(self, obj):
      self.ImportGroup:list[Ice_Tablesets_ImportGroupRow] = obj["ImportGroup"]
      self.ImportFile:list[Ice_Tablesets_ImportFileRow] = obj["ImportFile"]
      self.ImportDocument:list[Ice_Tablesets_ImportDocumentRow] = obj["ImportDocument"]
      self.ImportTask:list[Ice_Tablesets_ImportTaskRow] = obj["ImportTask"]
      self.ImportTaskLog:list[Ice_Tablesets_ImportTaskLogRow] = obj["ImportTaskLog"]
      self.ImportExecutionPlan:list[Ice_Tablesets_ImportExecutionPlanRow] = obj["ImportExecutionPlan"]
      self.ImportExecutionPlanDependency:list[Ice_Tablesets_ImportExecutionPlanDependencyRow] = obj["ImportExecutionPlanDependency"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ImportTaskLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.TaskID:int = obj["TaskID"]
      """  Displays the sequence number of the task.  """  
      self.LogID:int = obj["LogID"]
      """  Displays the sequence number of the log  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  Displays the date and time on which the task was started.  """  
      self.Error:bool = obj["Error"]
      """  When selected, specifies an error occurred during document import processing. Click the Message field to display additional information about the error.  """  
      self.ErrorTableName:str = obj["ErrorTableName"]
      """  Displays the name of the system table where the error occurred.  """  
      self.ErrorRowNum:int = obj["ErrorRowNum"]
      """  Displays the row number where the import failed  """  
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      """  this identifier should match with RowGuid field from  ice.ImportKeyValueStore, it is used to display the rows on Integration Workbench  """  
      self.Message:str = obj["Message"]
      """  An import process passes through different statuses during its lifecycle. Message information displays as the document is processing.  """  
      self.MessageType:str = obj["MessageType"]
      """  Displays the type of the message. The following types are available are Informational and Error  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FileName:str = obj["FileName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ImportExecutionPlanLinkExecutionAction:str = obj["ImportExecutionPlanLinkExecutionAction"]
      self.PrimaryKeyPrimaryKey:str = obj["PrimaryKeyPrimaryKey"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ImportTaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:int = obj["GroupID"]
      """  Displays the identification number of the group of the imported files.  """  
      self.FileID:int = obj["FileID"]
      """  Displays the identification number of the imported file.  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  Displays the sequence number of the document.  """  
      self.ExecutionPlanID:int = obj["ExecutionPlanID"]
      """  Defines a unique identifier for the current execution plan row  """  
      self.TaskID:int = obj["TaskID"]
      """  Displays the sequence number of the task.  """  
      self.StartedOn:str = obj["StartedOn"]
      """  Displays the date and time on which the task was started.  """  
      self.EndedOn:str = obj["EndedOn"]
      """  Displays the date and time on which the task finished.  """  
      self.Status:str = obj["Status"]
      """  Displays the current state of the conversion task. Use this status to manage the conversion set and review if the tasks completed successfully. Available statuses are Processing, Complete and Error  """  
      self.NumOfInputRows:int = obj["NumOfInputRows"]
      """  The number of rows contained in the document.  """  
      self.UserID:str = obj["UserID"]
      """  Identifies the user who submitted, or launched the import task.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  Displays the identification number of the process.  """  
      self.ThreadID:int = obj["ThreadID"]
      """  Indicates which thread from the application server was used to run the call.  """  
      self.ServerName:str = obj["ServerName"]
      """  Defines the specific name for the server from which you capture the logs.  """  
      self.PrimaryKey:str = obj["PrimaryKey"]
      """  Indicates the current field is required by the database. You cannot change the security option for a Primary Key field; usually these fields are for identifiers like the Company ID, Part ID, and so on.  """  
      self.Duration:int = obj["Duration"]
      """  Time spent on executing a document import call.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspTaskName:str = obj["DspTaskName"]
      """  field to shorten the link field ExecutionAction and display it on UI bavigation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActionNameExecutionAction:str = obj["ActionNameExecutionAction"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtImportMgmtTableset:
   def __init__(self, obj):
      self.ImportGroup:list[Ice_Tablesets_ImportGroupRow] = obj["ImportGroup"]
      self.ImportFile:list[Ice_Tablesets_ImportFileRow] = obj["ImportFile"]
      self.ImportDocument:list[Ice_Tablesets_ImportDocumentRow] = obj["ImportDocument"]
      self.ImportTask:list[Ice_Tablesets_ImportTaskRow] = obj["ImportTask"]
      self.ImportTaskLog:list[Ice_Tablesets_ImportTaskLogRow] = obj["ImportTaskLog"]
      self.ImportExecutionPlan:list[Ice_Tablesets_ImportExecutionPlanRow] = obj["ImportExecutionPlan"]
      self.ImportExecutionPlanDependency:list[Ice_Tablesets_ImportExecutionPlanDependencyRow] = obj["ImportExecutionPlanDependency"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class PauseImport_input:
   """ Required : 
   Company
   GroupID
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:int = obj["GroupID"]
      pass

class PauseImport_output:
   def __init__(self, obj):
      pass

class RestartImport_input:
   """ Required : 
   Company
   GroupID
   FileID
   DocumentNumber
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:int = obj["GroupID"]
      self.FileID:int = obj["FileID"]
      """  If left as 0 complete group gets restarted  """  
      self.DocumentNumber:int = obj["DocumentNumber"]
      """  if left as 0 complete file gets restarted  """  
      pass

class RestartImport_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtImportMgmtTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtImportMgmtTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ImportMgmtTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadFilesAndImport_input:
   """ Required : 
   stream
   groupID
   fileID
   """  
   def __init__(self, obj):
      self.stream:str = obj["stream"]
      self.groupID:int = obj["groupID"]
      self.fileID:int = obj["fileID"]
      pass

class UploadFilesAndImport_output:
   def __init__(self, obj):
      pass

