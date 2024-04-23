import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AttachmentSvc
# Description: Class for handling of attachments.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Attachments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Attachments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Attachments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XFileAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments",headers=creds) as resp:
           return await resp.json()

async def post_Attachments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Attachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName, RelatedToFile, ForeignSysRowID, AttachNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Attachment item
   Description: Calls GetByID to retrieve the Attachment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Attachment
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param AttachNum: Desc: AttachNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName, RelatedToFile, ForeignSysRowID, AttachNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Attachment for the service
   Description: Calls UpdateExt to update Attachment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Attachment
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param AttachNum: Desc: AttachNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName, RelatedToFile, ForeignSysRowID, AttachNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Attachment item
   Description: Call UpdateExt to delete Attachment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Attachment
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param AttachNum: Desc: AttachNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AttachmentCredentials(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AttachmentCredentials items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AttachmentCredentials
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AttachmentCredentialsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials",headers=creds) as resp:
           return await resp.json()

async def post_AttachmentCredentials(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AttachmentCredentials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AttachmentCredentials_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AttachmentCredential item
   Description: Calls GetByID to retrieve the AttachmentCredential item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AttachmentCredential
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AttachmentCredentials_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AttachmentCredential for the service
   Description: Calls UpdateExt to update AttachmentCredential. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AttachmentCredential
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AttachmentCredentials_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AttachmentCredential item
   Description: Call UpdateExt to delete AttachmentCredential item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AttachmentCredential
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XFileAttchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseXFileAttch, whereClauseAttachmentCredentials, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseXFileAttch=" + whereClauseXFileAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAttachmentCredentials=" + whereClauseAttachmentCredentials
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToSchemaName, relatedToFile, foreignSysRowID, attachNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "relatedToSchemaName=" + relatedToSchemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "relatedToFile=" + relatedToFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "foreignSysRowID=" + foreignSysRowID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attachNum=" + attachNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPathReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPathReferences
   Description: Returns a list of rows that reference the same path.
   OperationID: GetPathReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPathReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPathReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfFileName
   Description: Call when FileName is changed.
The purpose of this method is to find out if a given FileName is already
known in the database. That is, does a XFileRef record exist.
Client program should pass the current values from the dataset for the given parameters.
The returned parameter values should unconditionally moved to the corresponding fields in the dataset.
   OperationID: OnChangeOfFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfDocType
   Description: Call when DocTypeID is changed.
Will reset the path portion of the file name with the BaseURL of the DocType.
Note: It will not overlay a fully qualified filename.
   OperationID: OnChangeOfDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ServerDirectoryExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ServerDirectoryExists
   Description: Determines whether the given path refers to an existing directory on the server.
   OperationID: ServerDirectoryExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ServerDirectoryExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ServerDirectoryExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFile
   Description: Get a file's content from the server
   OperationID: DownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadFile
   Description: Set a file's content on the server
   OperationID: UploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileExists
   Description: Check if file exists on the server
   OperationID: FileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFile
   Description: Deletes the specified file.
   OperationID: DeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DetermineTransferModeByStorageType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DetermineTransferModeByStorageType
   Description: Determines whether the storage type for the given doctype uses client or service
document transfer.  If no storage type is specified then will return the company default
storage type transfer mode if a company default is specified. Returns the literal 'NONE' if
no storage type found.
   OperationID: DetermineTransferModeByStorageType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DetermineTransferModeByStorageType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineTransferModeByStorageType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadFileToDocTypeStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadFileToDocTypeStorage
   Description: Upload file to the storage defined by document type (or default company storage)
   OperationID: UploadFileToDocTypeStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFileToDocTypeStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFileToDocTypeStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadNonERPFileToDocTypeStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadNonERPFileToDocTypeStorage
   Description: Upload a NON ERP file to the storage defined by document type (or default company storage)
   OperationID: UploadNonERPFileToDocTypeStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadNonERPFileToDocTypeStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadNonERPFileToDocTypeStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadFileFromDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadFileFromDocumentStorage
   OperationID: DownloadFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadNonERPFileFromDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadNonERPFileFromDocumentStorage
   OperationID: DownloadNonERPFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadNonERPFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadNonERPFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFileFromDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFileFromDocumentStorage
   Description: Delete a file from its associated storage system.
   OperationID: DeleteFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteNonERPFileFromDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteNonERPFileFromDocumentStorage
   Description: Delete a file from its associated storage system.
   OperationID: DeleteNonERPFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteNonERPFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNonERPFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFileMetaDataFromDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileMetaDataFromDocumentStorage
   OperationID: GetFileMetaDataFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileMetaDataFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileMetaDataFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMetadataOnDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMetadataOnDocumentStorage
   Description: Updates the files metadata on the storage system.
   OperationID: UpdateMetadataOnDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMetadataOnDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMetadataOnDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FileExistsOnDocumentStorage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FileExistsOnDocumentStorage
   Description: Determines if the document already exists in storage.
   OperationID: FileExistsOnDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExistsOnDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExistsOnDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCredentialsForServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCredentialsForServer
   Description: Get external attachment system credentials (username, domain and authentication type) for this company or document type.
   OperationID: GetCredentialsForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCredentialsForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCredentialsForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAccountForServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAccountForServer
   Description: Get external attachment system account user name for this company or doc type.
   OperationID: GetAccountForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccountForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccountForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAccountForServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAccountForServer
   Description: Set external attachment system account info for the company or doc type. Security Manager access right is requried.
   OperationID: SetAccountForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAccountForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAccountForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAccountForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAccountForUser
   Description: Get external attachment system account info for this company or doc type for logged in user
   OperationID: GetAccountForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccountForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccountForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAccountForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAccountForUser
   Description: Set SP account info for the company or doc type for loggedin user
   OperationID: SetAccountForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAccountForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAccountForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAccountsForUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearAccountsForUser
   Description: Clear stored external attachment system user accounts for current company and any document type
   OperationID: ClearAccountsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAccountsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAccountsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewXFileAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewXFileAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXFileAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXFileAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXFileAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarTestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarTestConnection
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarTestConnectionCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarTestConnectionCompany
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateCompanyFolder(epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateCompanyFolder
   Description: Create folder for company in the DocStar system
   OperationID: DocStarCreateCompanyFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateCompanyFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateDocumentTypeFolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateDocumentTypeFolder
   Description: Create folder for document type in the DocStar system
   OperationID: DocStarCreateDocumentTypeFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateDocumentTypeFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateDocumentTypeFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateDocumentFolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateDocumentFolder
   Description: Create folder for table inside document type folder in the DocStar system
   OperationID: DocStarCreateDocumentFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateDocumentFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateDocumentFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateCustomFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateCustomFields
   Description: Create custom fields in DocStar system
   OperationID: DocStarCreateCustomFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateCustomFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateCustomFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarUploadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarUploadFile
   Description: Upload file to DocStar system and store metadata
   OperationID: DocStarUploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarUploadFileAsVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarUploadFileAsVersion
   Description: Upload file to DocStar system and store metadata
   OperationID: DocStarUploadFileAsVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUploadFileAsVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUploadFileAsVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarDownloadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarDownloadFile
   OperationID: DocStarDownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarDownloadNonERPFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarDownloadNonERPFile
   OperationID: DocStarDownloadNonERPFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDownloadNonERPFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDownloadNonERPFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarUpdateMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarUpdateMetadata
   Description: Update metadata for the file
   OperationID: DocStarUpdateMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUpdateMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUpdateMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarGetMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarGetMetadata
   OperationID: DocStarGetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarGetMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarGetMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarDeleteNonERPFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarDeleteNonERPFile
   Description: Delete file to Recycle Bin
   OperationID: DocStarDeleteNonERPFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDeleteNonERPFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDeleteNonERPFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarDeleteFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarDeleteFile
   Description: Delete file to Recycle Bin
   OperationID: DocStarDeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarFileExistsForTableRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarFileExistsForTableRow
   Description: Check if docStar file with the same name already exists in the XFileRef attachment table for this Epicor table record
   OperationID: DocStarFileExistsForTableRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarFileExistsForTableRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarFileExistsForTableRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocStarCreateBrowserUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocStarCreateBrowserUrl
   Description: Builds a URL in DocStar which will be used to open the attachment within DocStar.
   OperationID: DocStarCreateBrowserUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateBrowserUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateBrowserUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DropboxFileExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DropboxFileExists
   Description: Determines if the file exists on Dropbox using the given path.
   OperationID: DropboxFileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DropboxFileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DropboxFileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GoogleUpdateMetaData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GoogleUpdateMetaData
   Description: Updates the file metadata.
   OperationID: GoogleUpdateMetaData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GoogleUpdateMetaData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GoogleUpdateMetaData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpUploadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpUploadFile
   Description: Upload file to Sharepoint and store metadata
   OperationID: SpUploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpUploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpUploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpDownloadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpDownloadFile
   Description: Download file and its metadata from SharePoint
   OperationID: SpDownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpDownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpDownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpGetMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpGetMetadata
   OperationID: SpGetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpGetMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpGetMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpUpdateMetadata(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpUpdateMetadata
   Description: Update metadata for Sharepoint file
   OperationID: SpUpdateMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpUpdateMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpUpdateMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpDeleteFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpDeleteFile
   Description: Delete file from SharePoint
   OperationID: SpDeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpDeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpDeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpFileExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpFileExists
   Description: Check if file exists on the sharepoint site
   OperationID: SpFileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpFileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpFileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpCreateDocumentLibrary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpCreateDocumentLibrary
   Description: Create Sharepoint Document library.
   OperationID: SpCreateDocumentLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateDocumentLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateDocumentLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpCreateDocumentFolder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpCreateDocumentFolder
   Description: Create Sharepoint document folder for table.
   OperationID: SpCreateDocumentFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateDocumentFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateDocumentFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpCreateContentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpCreateContentType
   Description: Create Sharepoint Content type.
   OperationID: SpCreateContentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateContentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateContentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpAddFieldToContentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpAddFieldToContentType
   Description: Add field to the Sharepoint content type. Security Manager access right is requried.
   OperationID: SpAddFieldToContentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpAddFieldToContentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpAddFieldToContentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpTestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpTestConnection
   Description: Test connection to SharePoint
   OperationID: SpTestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpTestConnectionCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpTestConnectionCompany
   Description: Test connection to SharePoint
   OperationID: SpTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SpOnlineTestConnectionCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SpOnlineTestConnectionCompany
   Description: Test connection to SharePoint Online.
   OperationID: SpOnlineTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpOnlineTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpOnlineTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AttachmentCredentialsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AttachmentCredentialsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XFileAttchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XFileAttchRow] = obj["value"]
      pass

class Ice_Tablesets_AttachmentCredentialsRow:
   def __init__(self, obj):
      self.UserName:str = obj["UserName"]
      self.Domain:str = obj["Domain"]
      self.AuthType:str = obj["AuthType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XFileAttchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  """  
      self.AttachNum:int = obj["AttachNum"]
      """   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  """  
      self.XFileRefNum:int = obj["XFileRefNum"]
      """  Foreign Key to XFileRef record.  """  
      self.DoTrigger:bool = obj["DoTrigger"]
      """  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  """  
      self.DupToRelatedToFile:str = obj["DupToRelatedToFile"]
      """  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  """  
      self.DupToKey1:str = obj["DupToKey1"]
      """  See DupToRelatedToFile  """  
      self.DupToKey2:str = obj["DupToKey2"]
      """  See DupToRelatedToFile  """  
      self.DupToKey3:str = obj["DupToKey3"]
      """  See DupToRelatedToFile  """  
      self.DupToKey4:str = obj["DupToKey4"]
      """  See DupToRelatedToFile  """  
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.DupToAttachNum:int = obj["DupToAttachNum"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XFileAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  """  
      self.AttachNum:int = obj["AttachNum"]
      """   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  """  
      self.XFileRefNum:int = obj["XFileRefNum"]
      """  Foreign Key to XFileRef record.  """  
      self.DoTrigger:bool = obj["DoTrigger"]
      """  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  """  
      self.DupToRelatedToFile:str = obj["DupToRelatedToFile"]
      """  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  """  
      self.DupToKey1:str = obj["DupToKey1"]
      """  See DupToRelatedToFile  """  
      self.DupToKey2:str = obj["DupToKey2"]
      """  See DupToRelatedToFile  """  
      self.DupToKey3:str = obj["DupToKey3"]
      """  See DupToRelatedToFile  """  
      self.DupToKey4:str = obj["DupToKey4"]
      """  See DupToRelatedToFile  """  
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.DupToAttachNum:int = obj["DupToAttachNum"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.XFileRefDocTypeID:str = obj["XFileRefDocTypeID"]
      self.XFileRefPDMDocID:str = obj["XFileRefPDMDocID"]
      self.XFileRefXFileName:str = obj["XFileRefXFileName"]
      self.XFileRefXFileDesc:str = obj["XFileRefXFileDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ClearAccountsForUser_input:
   """ Required : 
   storageType
   """  
   def __init__(self, obj):
      self.storageType:int = obj["storageType"]
      """  Storage type this account is created for  """  
      pass

class ClearAccountsForUser_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToFile
   foreignSysRowID
   attachNum
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      self.attachNum:int = obj["attachNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteFileFromDocumentStorage_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  The xFileRef file ID associated with the document.  """  
      pass

class DeleteFileFromDocumentStorage_output:
   def __init__(self, obj):
      pass

class DeleteFile_input:
   """ Required : 
   xFileRefNum
   makeBackup
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  id of the attachment  """  
      self.makeBackup:bool = obj["makeBackup"]
      """  copy backup to 'deleted' directory  """  
      pass

class DeleteFile_output:
   def __init__(self, obj):
      pass

class DeleteNonERPFileFromDocumentStorage_input:
   """ Required : 
   xFileRefNum
   companyId
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  The xFileRef file ID associated with the document.  """  
      self.companyId:str = obj["companyId"]
      pass

class DeleteNonERPFileFromDocumentStorage_output:
   def __init__(self, obj):
      pass

class DetermineTransferModeByStorageType_input:
   """ Required : 
   docTypeID
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      pass

class DetermineTransferModeByStorageType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  'S' for service transfer, 'C' for client transfer and 'NONE' if no storage type can be determined.  """  
      pass

class DocStarCreateBrowserUrl_input:
   """ Required : 
   docTypeID
   documentId
   userName
   userPwd
   domain
   authType
   saveLogin
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type for the attachment  """  
      self.documentId:str = obj["documentId"]
      """  Document identifier  """  
      self.userName:str = obj["userName"]
      """  User Identifier  """  
      self.userPwd:str = obj["userPwd"]
      """  Encrypted user password  """  
      self.domain:str = obj["domain"]
      """  Domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type  """  
      self.saveLogin:bool = obj["saveLogin"]
      """  If true saves the user account information  """  
      pass

class DocStarCreateBrowserUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Url for the attachment document within DocStar  """  
      pass

class DocStarCreateCompanyFolder_output:
   def __init__(self, obj):
      pass

class DocStarCreateCustomFields_input:
   """ Required : 
   docTypeID
   customFieldNames
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      self.customFieldNames:str = obj["customFieldNames"]
      pass

class DocStarCreateCustomFields_output:
   def __init__(self, obj):
      pass

class DocStarCreateDocumentFolder_input:
   """ Required : 
   docTypeID
   tableName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      pass

class DocStarCreateDocumentFolder_output:
   def __init__(self, obj):
      pass

class DocStarCreateDocumentTypeFolder_input:
   """ Required : 
   docTypeID
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      pass

class DocStarCreateDocumentTypeFolder_output:
   def __init__(self, obj):
      pass

class DocStarDeleteFile_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  File ID from xFileRef table  """  
      pass

class DocStarDeleteFile_output:
   def __init__(self, obj):
      pass

class DocStarDeleteNonERPFile_input:
   """ Required : 
   xFileRefNum
   companyId
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  File ID from xFileRef table  """  
      self.companyId:str = obj["companyId"]
      pass

class DocStarDeleteNonERPFile_output:
   def __init__(self, obj):
      pass

class DocStarDownloadFile_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.metadata      #schema had no properties on an object.
      pass

class DocStarDownloadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class DocStarDownloadNonERPFile_input:
   """ Required : 
   xFileRefNum
   companyId
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.companyId:str = obj["companyId"]
      self.metadata      #schema had no properties on an object.
      pass

class DocStarDownloadNonERPFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class DocStarFileExistsForTableRow_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  document type or empty, if default  """  
      self.parentTable:str = obj["parentTable"]
      """  table where attacment belongs  """  
      self.fileName:str = obj["fileName"]
      """  file name  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      pass

class DocStarFileExistsForTableRow_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  returns xFileRefNum or 0  """  
      pass

   def parameters(self, obj):
      self.xFileName:str = obj["parameters"]
      self.AttachNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class DocStarGetMetadata_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.metadata      #schema had no properties on an object.
      pass

class DocStarGetMetadata_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class DocStarTestConnectionCompany_input:
   """ Required : 
   docTypeID
   userName
   userPwd
   domain
   authType
   hostName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access  """  
      self.userName:str = obj["userName"]
      """  suggested username  """  
      self.userPwd:str = obj["userPwd"]
      """  suggested password  """  
      self.domain:str = obj["domain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM or USERNAME  """  
      self.hostName:str = obj["hostName"]
      """  Host Name  """  
      pass

class DocStarTestConnectionCompany_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown  """  
      pass

class DocStarTestConnection_input:
   """ Required : 
   docTypeID
   userName
   userPwd
   domain
   authType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access  """  
      self.userName:str = obj["userName"]
      """  suggested username  """  
      self.userPwd:str = obj["userPwd"]
      """  suggested password  """  
      self.domain:str = obj["domain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM or USERNAME  """  
      pass

class DocStarTestConnection_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown  """  
      pass

class DocStarUpdateMetadata_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  File ID from xFileRef table  """  
      self.metadata      #schema had no properties on an object.
      """  metadata to update  """  
      pass

class DocStarUpdateMetadata_output:
   def __init__(self, obj):
      pass

class DocStarUploadFileAsVersion_input:
   """ Required : 
   xFileRefNum
   fileName
   data
   docTypeID
   parentTable
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.fileName:str = obj["fileName"]
      """  file name without path  """  
      self.data:str = obj["data"]
      """  file binary data  """  
      self.docTypeID:str = obj["docTypeID"]
      """  Document type for the attachment  """  
      self.parentTable:str = obj["parentTable"]
      """  Table where file is attached  """  
      self.metadata      #schema had no properties on an object.
      """  Metadata values to store with file  """  
      pass

class DocStarUploadFileAsVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DocStarUploadFile_input:
   """ Required : 
   fileName
   data
   docTypeID
   parentTable
   metadata
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  file name without path  """  
      self.data:str = obj["data"]
      """  file binary data  """  
      self.docTypeID:str = obj["docTypeID"]
      """  Document type for the attachment  """  
      self.parentTable:str = obj["parentTable"]
      """  Table where file is attached  """  
      self.metadata      #schema had no properties on an object.
      """  Metadata values to store with file  """  
      pass

class DocStarUploadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DownloadFileFromDocumentStorage_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.metadata      #schema had no properties on an object.
      pass

class DownloadFileFromDocumentStorage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class DownloadFile_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  id of the attachment  """  
      pass

class DownloadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File data  """  
      pass

class DownloadNonERPFileFromDocumentStorage_input:
   """ Required : 
   xFileRefNum
   companyId
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.companyId:str = obj["companyId"]
      self.metadata      #schema had no properties on an object.
      pass

class DownloadNonERPFileFromDocumentStorage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class DropboxFileExists_input:
   """ Required : 
   dropboxFilePath
   """  
   def __init__(self, obj):
      self.dropboxFilePath:str = obj["dropboxFilePath"]
      """  The dropbox file path.  """  
      pass

class DropboxFileExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if the file exists, otherwise false.  """  
      pass

class FileExistsOnDocumentStorage_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  The xFileRef file ID associated with the document.  """  
      pass

class FileExistsOnDocumentStorage_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class FileExists_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  document type or empty, if default  """  
      self.parentTable:str = obj["parentTable"]
      """  table where attacment belongs  """  
      self.fileName:str = obj["fileName"]
      """  Path to the file on the server  """  
      pass

class FileExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if exists  """  
      pass

class GetAccountForServer_input:
   """ Required : 
   docTypeID
   storageType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string for company level.  """  
      self.storageType:int = obj["storageType"]
      """  Storage type this accound is created for.  """  
      pass

class GetAccountForServer_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  User name used on server side.  """  
      pass

   def parameters(self, obj):
      self.authType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAccountForUser_input:
   """ Required : 
   docTypeID
   storageType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string for company level  """  
      self.storageType:int = obj["storageType"]
      """  Storage type this accound is created for  """  
      pass

class GetAccountForUser_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if record is found  """  
      pass

   def parameters(self, obj):
      self.spUserName:str = obj["parameters"]
      self.spUserPwd:str = obj["parameters"]
      self.spDomain:str = obj["parameters"]
      self.authType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToFile
   foreignSysRowID
   attachNum
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      self.attachNum:int = obj["attachNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AttachmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_AttachmentTableset] = obj["returnObj"]
      pass

class GetCredentialsForServer_input:
   """ Required : 
   docTypeID
   storageType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string for company level.  """  
      self.storageType:int = obj["storageType"]
      """  Storage type this accound is created for.  """  
      pass

class GetCredentialsForServer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachmentCredentialsRow] = obj["returnObj"]
      """  Credentials used on server side.  """  
      pass

class GetFileMetaDataFromDocumentStorage_input:
   """ Required : 
   xFileRefNum
   metaData
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.metaData      #schema had no properties on an object.
      pass

class GetFileMetaDataFromDocumentStorage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.metaData: UNKNOW TYPE(error 2338) = obj["metaData"]
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
      self.returnObj:list[Ice_Tablesets_XFileAttchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewXFileAttch_input:
   """ Required : 
   ds
   relatedToSchemaName
   relatedToFile
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AttachmentTableset] = obj["ds"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      pass

class GetNewXFileAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AttachmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPathReferences_input:
   """ Required : 
   path
   """  
   def __init__(self, obj):
      self.path:str = obj["path"]
      """  The path to match.  """  
      pass

class GetPathReferences_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_XFileAttchListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseXFileAttch
   whereClauseAttachmentCredentials
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseXFileAttch:str = obj["whereClauseXFileAttch"]
      self.whereClauseAttachmentCredentials:str = obj["whereClauseAttachmentCredentials"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachmentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GoogleUpdateMetaData_input:
   """ Required : 
   xFileRefNum
   metadata
   addProps
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  The xFileRef file ID associated with the document.  """  
      self.metadata      #schema had no properties on an object.
      """  Dictionary containing the file metadata to update.  """  
      self.addProps:bool = obj["addProps"]
      """  Indicates whether or not to add custom properties.  """  
      pass

class GoogleUpdateMetaData_output:
   def __init__(self, obj):
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

class Ice_Tablesets_AttachmentCredentialsRow:
   def __init__(self, obj):
      self.UserName:str = obj["UserName"]
      self.Domain:str = obj["Domain"]
      self.AuthType:str = obj["AuthType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AttachmentTableset:
   def __init__(self, obj):
      self.XFileAttch:list[Ice_Tablesets_XFileAttchRow] = obj["XFileAttch"]
      self.AttachmentCredentials:list[Ice_Tablesets_AttachmentCredentialsRow] = obj["AttachmentCredentials"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtAttachmentTableset:
   def __init__(self, obj):
      self.XFileAttch:list[Ice_Tablesets_XFileAttchRow] = obj["XFileAttch"]
      self.AttachmentCredentials:list[Ice_Tablesets_AttachmentCredentialsRow] = obj["AttachmentCredentials"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XFileAttchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  """  
      self.AttachNum:int = obj["AttachNum"]
      """   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  """  
      self.XFileRefNum:int = obj["XFileRefNum"]
      """  Foreign Key to XFileRef record.  """  
      self.DoTrigger:bool = obj["DoTrigger"]
      """  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  """  
      self.DupToRelatedToFile:str = obj["DupToRelatedToFile"]
      """  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  """  
      self.DupToKey1:str = obj["DupToKey1"]
      """  See DupToRelatedToFile  """  
      self.DupToKey2:str = obj["DupToKey2"]
      """  See DupToRelatedToFile  """  
      self.DupToKey3:str = obj["DupToKey3"]
      """  See DupToRelatedToFile  """  
      self.DupToKey4:str = obj["DupToKey4"]
      """  See DupToRelatedToFile  """  
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.DupToAttachNum:int = obj["DupToAttachNum"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XFileAttchListTableset:
   def __init__(self, obj):
      self.XFileAttchList:list[Ice_Tablesets_XFileAttchListRow] = obj["XFileAttchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XFileAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  """  
      self.AttachNum:int = obj["AttachNum"]
      """   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  """  
      self.XFileRefNum:int = obj["XFileRefNum"]
      """  Foreign Key to XFileRef record.  """  
      self.DoTrigger:bool = obj["DoTrigger"]
      """  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  """  
      self.DupToRelatedToFile:str = obj["DupToRelatedToFile"]
      """  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  """  
      self.DupToKey1:str = obj["DupToKey1"]
      """  See DupToRelatedToFile  """  
      self.DupToKey2:str = obj["DupToKey2"]
      """  See DupToRelatedToFile  """  
      self.DupToKey3:str = obj["DupToKey3"]
      """  See DupToRelatedToFile  """  
      self.DupToKey4:str = obj["DupToKey4"]
      """  See DupToRelatedToFile  """  
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.DupToAttachNum:int = obj["DupToAttachNum"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.XFileRefDocTypeID:str = obj["XFileRefDocTypeID"]
      self.XFileRefPDMDocID:str = obj["XFileRefPDMDocID"]
      self.XFileRefXFileName:str = obj["XFileRefXFileName"]
      self.XFileRefXFileDesc:str = obj["XFileRefXFileDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class OnChangeOfDocType_input:
   """ Required : 
   docTypeID
   fileName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  The Document Type ID (tablenameAttch.DocTypeID) that has been entered.  """  
      self.fileName:str = obj["fileName"]
      """  The fully qualified file name that the user is referencing for this attachment.  """  
      pass

class OnChangeOfDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeOfFileName_input:
   """ Required : 
   fileName
   xFileRefNum
   xFileDesc
   docTypeID
   pdmDocID
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  The fully qualified file name (tablenameAttch.FileName) that the user is referencing for this attachment.  """  
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  External File Reference Number (tablenameAttch.XFileRefNum).  """  
      self.xFileDesc:str = obj["xFileDesc"]
      """  File description (tablenameAttch.DrawDesc).  """  
      self.docTypeID:str = obj["docTypeID"]
      """  Document Type ID (tablenameAttch.DocTypeID).  """  
      self.pdmDocID:str = obj["pdmDocID"]
      """  PDM Document ID (tablenameAttch.PDMDocID).  """  
      pass

class OnChangeOfFileName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.xFileRefNum:int = obj["parameters"]
      self.xFileDesc:str = obj["parameters"]
      self.docTypeID:str = obj["parameters"]
      self.pdmDocID:str = obj["parameters"]
      pass

      """  output parameters  """  

class ServerDirectoryExists_input:
   """ Required : 
   path
   """  
   def __init__(self, obj):
      self.path:str = obj["path"]
      """  The path to test  """  
      pass

class ServerDirectoryExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SetAccountForServer_input:
   """ Required : 
   docTypeID
   storageType
   spUserName
   spUserPwd
   spDomain
   authType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string for company level  """  
      self.storageType:int = obj["storageType"]
      """  Storage type this accound is created for  """  
      self.spUserName:str = obj["spUserName"]
      """  User name  """  
      self.spUserPwd:str = obj["spUserPwd"]
      """  Password  """  
      self.spDomain:str = obj["spDomain"]
      """  Domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM for Windows or SPO for SharePoint Online  """  
      pass

class SetAccountForServer_output:
   def __init__(self, obj):
      pass

class SetAccountForUser_input:
   """ Required : 
   docTypeID
   storageType
   spUserName
   spUserPwd
   spDomain
   authType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to change access to company  """  
      self.storageType:int = obj["storageType"]
      """  Storage type this accound is created for  """  
      self.spUserName:str = obj["spUserName"]
      """  suggested username  """  
      self.spUserPwd:str = obj["spUserPwd"]
      """  suggested password  """  
      self.spDomain:str = obj["spDomain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM for Windows or SPO for SharePoint Online  """  
      pass

class SetAccountForUser_output:
   def __init__(self, obj):
      pass

class SpAddFieldToContentType_input:
   """ Required : 
   docTypeID
   contentTypeName
   columnName
   displayName
   dataType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      self.contentTypeName:str = obj["contentTypeName"]
      self.columnName:str = obj["columnName"]
      self.displayName:str = obj["displayName"]
      self.dataType:str = obj["dataType"]
      pass

class SpAddFieldToContentType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SpCreateContentType_input:
   """ Required : 
   docTypeID
   contentTypeName
   contentTypeDescription
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      self.contentTypeName:str = obj["contentTypeName"]
      self.contentTypeDescription:str = obj["contentTypeDescription"]
      pass

class SpCreateContentType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SpCreateDocumentFolder_input:
   """ Required : 
   docTypeID
   tableName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      self.tableName:str = obj["tableName"]
      """  Table to use for attachments  """  
      pass

class SpCreateDocumentFolder_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SpCreateDocumentLibrary_input:
   """ Required : 
   docTypeID
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type  """  
      pass

class SpCreateDocumentLibrary_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SpDeleteFile_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  File ID  """  
      pass

class SpDeleteFile_output:
   def __init__(self, obj):
      pass

class SpDownloadFile_input:
   """ Required : 
   xFileRefNum
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  file ID  """  
      pass

class SpDownloadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SpFileExists_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  document type or empty, if default  """  
      self.parentTable:str = obj["parentTable"]
      """  table where attacment belongs  """  
      self.fileName:str = obj["fileName"]
      """  Path to the file on the server  """  
      pass

class SpFileExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if exists  """  
      pass

class SpGetMetadata_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      self.metadata      #schema had no properties on an object.
      pass

class SpGetMetadata_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.metadata: UNKNOW TYPE(error 2338) = obj["metadata"]
      pass

      """  output parameters  """  

class SpOnlineTestConnectionCompany_input:
   """ Required : 
   docTypeID
   directoryID
   applicationID
   certificateThumbPrint
   sharePointRoot
   authorityEndpoint
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access.  """  
      self.directoryID:str = obj["directoryID"]
      """  Azure Active Directory ID.  """  
      self.applicationID:str = obj["applicationID"]
      """  Azure Active Directory WEb application ID.  """  
      self.certificateThumbPrint:str = obj["certificateThumbPrint"]
      self.sharePointRoot:str = obj["sharePointRoot"]
      """  Share Point Root  """  
      self.authorityEndpoint:str = obj["authorityEndpoint"]
      """  Authority endpoint. Default will be used if nothing specified.  """  
      pass

class SpOnlineTestConnectionCompany_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown.  """  
      pass

class SpTestConnectionCompany_input:
   """ Required : 
   docTypeID
   spUserName
   spUserPwd
   spDomain
   authType
   sharePointRoot
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access  """  
      self.spUserName:str = obj["spUserName"]
      """  suggested username  """  
      self.spUserPwd:str = obj["spUserPwd"]
      """  suggested password  """  
      self.spDomain:str = obj["spDomain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - should be NTLM.  """  
      self.sharePointRoot:str = obj["sharePointRoot"]
      """  Share Point Root  """  
      pass

class SpTestConnectionCompany_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown  """  
      pass

class SpTestConnection_input:
   """ Required : 
   docTypeID
   spUserName
   spUserPwd
   spDomain
   authType
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  Document type ID, or empty string to test company access  """  
      self.spUserName:str = obj["spUserName"]
      """  suggested username  """  
      self.spUserPwd:str = obj["spUserPwd"]
      """  suggested password  """  
      self.spDomain:str = obj["spDomain"]
      """  domain for Windows authentication  """  
      self.authType:str = obj["authType"]
      """  Authentication type - NTLM for Windows or SPO for SharePoint Online  """  
      pass

class SpTestConnection_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Message that connection succeeded. In case of failure exception will be thrown  """  
      pass

class SpUpdateMetadata_input:
   """ Required : 
   xFileRefNum
   addSpPropsFields
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  File ID from xFileRef table  """  
      self.addSpPropsFields:bool = obj["addSpPropsFields"]
      """  set to false to update only description, true - to update comment and status  """  
      self.metadata      #schema had no properties on an object.
      """  metadata to update  """  
      pass

class SpUpdateMetadata_output:
   def __init__(self, obj):
      pass

class SpUploadFile_input:
   """ Required : 
   fileName
   data
   docTypeID
   parentTable
   metadata
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  file name without path  """  
      self.data:str = obj["data"]
      """  file binary data  """  
      self.docTypeID:str = obj["docTypeID"]
      """  Document type for the attachment  """  
      self.parentTable:str = obj["parentTable"]
      """  Table where file is attached  """  
      self.metadata      #schema had no properties on an object.
      """  SharePoint metadata  """  
      pass

class SpUploadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAttachmentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAttachmentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMetadataOnDocumentStorage_input:
   """ Required : 
   xFileRefNum
   metadata
   """  
   def __init__(self, obj):
      self.xFileRefNum:int = obj["xFileRefNum"]
      """  The xFileRef file ID associated with the document.  """  
      self.metadata      #schema had no properties on an object.
      """  Dictionary containing the file metadata to update.  """  
      pass

class UpdateMetadataOnDocumentStorage_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AttachmentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AttachmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadFileToDocTypeStorage_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   data
   metadata
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      self.parentTable:str = obj["parentTable"]
      self.fileName:str = obj["fileName"]
      self.data:str = obj["data"]
      self.metadata      #schema had no properties on an object.
      pass

class UploadFileToDocTypeStorage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  server file path  """  
      pass

class UploadFile_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   data
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      """  document type or empty, if default  """  
      self.parentTable:str = obj["parentTable"]
      """  table where attacment belongs  """  
      self.fileName:str = obj["fileName"]
      """  filename, without path  """  
      self.data:str = obj["data"]
      """  file content  """  
      pass

class UploadFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class UploadNonERPFileToDocTypeStorage_input:
   """ Required : 
   docTypeID
   parentTable
   fileName
   data
   metadata
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      self.parentTable:str = obj["parentTable"]
      self.fileName:str = obj["fileName"]
      self.data:str = obj["data"]
      self.metadata      #schema had no properties on an object.
      pass

class UploadNonERPFileToDocTypeStorage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  server file path  """  
      pass

