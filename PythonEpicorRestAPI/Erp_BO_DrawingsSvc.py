import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DrawingsSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Drawings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Drawings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Drawings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DrawingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/Drawings",headers=creds) as resp:
           return await resp.json()

async def post_Drawings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Drawings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DrawingsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DrawingsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/Drawings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Drawings_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_AttachNum(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, AttachNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Drawing item
   Description: Calls GetByID to retrieve the Drawing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Drawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param AttachNum: Desc: AttachNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DrawingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/Drawings(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + AttachNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Drawings_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_AttachNum(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, AttachNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Drawing for the service
   Description: Calls UpdateExt to update Drawing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Drawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param AttachNum: Desc: AttachNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DrawingsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/Drawings(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + AttachNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Drawings_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_AttachNum(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, AttachNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Drawing item
   Description: Call UpdateExt to delete Drawing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Drawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/Drawings(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + AttachNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DrawingsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDrawings, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseDrawings=" + whereClauseDrawings
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToFile, key1, key2, key3, key4, key5, key6, attachNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "relatedToFile=" + relatedToFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key6=" + key6
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDrawingsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDrawingsList
   Description: Get XFileAttch list
   OperationID: GetDrawingsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDrawingsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDrawingsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobDocsTableName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobDocsTableName
   Description: Get Job Documents Table Name
   OperationID: GetJobDocsTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobDocsTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobDocsTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DrawingsGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DrawingsGetNew
   Description: Purpose: Wraps standard function GetNewDrawings() adding relatedToSchemaName and foreignSysRowID parameters
Parameters:  none
Notes:
   OperationID: DrawingsGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DrawingsGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DrawingsGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryIndexFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryIndexFields
   Description: Get Primary index fields
   OperationID: GetPrimaryIndexFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryIndexFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryIndexFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDrawings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDrawings
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDrawings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDrawings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDrawings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DrawingsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DrawingsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DrawingsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DrawingsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DrawingsRow] = obj["value"]
      pass

class Erp_Tablesets_DrawingsListRow:
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
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DrawingsRow:
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
      self.DupToKey5:str = obj["DupToKey5"]
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
      self.DocTypeID:str = obj["DocTypeID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   attachNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      self.attachNum:int = obj["attachNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DrawingsGetNew_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   relatedToSchemaName
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      pass

class DrawingsGetNew_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DrawingsListRow:
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
      self.DupToKey5:str = obj["DupToKey5"]
      """  See DupToRelatedToFile  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.SharePointID:str = obj["SharePointID"]
      """  The unique ID assigned by the Sharepoint system to attachments.  Field not required  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DrawingsListTableset:
   def __init__(self, obj):
      self.DrawingsList:list[Erp_Tablesets_DrawingsListRow] = obj["DrawingsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DrawingsRow:
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
      self.DupToKey5:str = obj["DupToKey5"]
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
      self.DocTypeID:str = obj["DocTypeID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeDescription:str = obj["DocTypeDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DrawingsTableset:
   def __init__(self, obj):
      self.Drawings:list[Erp_Tablesets_DrawingsRow] = obj["Drawings"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDrawingsTableset:
   def __init__(self, obj):
      self.Drawings:list[Erp_Tablesets_DrawingsRow] = obj["Drawings"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   attachNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      self.attachNum:int = obj["attachNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DrawingsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DrawingsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DrawingsTableset] = obj["returnObj"]
      pass

class GetDrawingsList_input:
   """ Required : 
   ipRelatedToFile
   ipKey1
   ipKey2
   ipKey3
   ipKey4
   ipKey5
   """  
   def __init__(self, obj):
      self.ipRelatedToFile:str = obj["ipRelatedToFile"]
      """  Related To file  """  
      self.ipKey1:str = obj["ipKey1"]
      """  Key1  """  
      self.ipKey2:str = obj["ipKey2"]
      """  Key2  """  
      self.ipKey3:str = obj["ipKey3"]
      """  Key3  """  
      self.ipKey4:str = obj["ipKey4"]
      """  Key4  """  
      self.ipKey5:str = obj["ipKey5"]
      """  Key5  """  
      pass

class GetDrawingsList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DrawingsTableset] = obj["returnObj"]
      pass

class GetJobDocsTableName_input:
   """ Required : 
   ip_JobNum
   ip_AssemblySeq
   ip_OprSeq
   """  
   def __init__(self, obj):
      self.ip_JobNum:str = obj["ip_JobNum"]
      """  Job number  """  
      self.ip_AssemblySeq:int = obj["ip_AssemblySeq"]
      """  Assembly sequence  """  
      self.ip_OprSeq:int = obj["ip_OprSeq"]
      """  Operation sequence  """  
      pass

class GetJobDocsTableName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.op_TableName:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_DrawingsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDrawings_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewDrawings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimaryIndexFields_input:
   """ Required : 
   ipTableName
   """  
   def __init__(self, obj):
      self.ipTableName:str = obj["ipTableName"]
      """  Table name  """  
      pass

class GetPrimaryIndexFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFieldList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDrawings
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDrawings:str = obj["whereClauseDrawings"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DrawingsTableset] = obj["returnObj"]
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

class OnChangeOfDocType_input:
   """ Required : 
   ipDocTypeID
   iOFileName
   """  
   def __init__(self, obj):
      self.ipDocTypeID:str = obj["ipDocTypeID"]
      """  The Document Type ID (tablenameAttch.DocTypeID) that has been entered.  """  
      self.iOFileName:str = obj["iOFileName"]
      """  The fully qualified file name that the user is referencing for this attachment.  """  
      pass

class OnChangeOfDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iOFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeOfFileName_input:
   """ Required : 
   ipFileName
   iOXFileRefNum
   iOXFileDesc
   iODocTypeID
   iOPDMDocID
   """  
   def __init__(self, obj):
      self.ipFileName:str = obj["ipFileName"]
      """  The fully qualified file name (tablenameAttch.FileName) that the user is referencing for this attachment.  """  
      self.iOXFileRefNum:int = obj["iOXFileRefNum"]
      """  External File Reference Number (tablenameAttch.XFileRefNum).  """  
      self.iOXFileDesc:str = obj["iOXFileDesc"]
      """  File Descripttion (tablenameAttch.DrawDesc).  """  
      self.iODocTypeID:str = obj["iODocTypeID"]
      """  Document Type ID (tablenameAttch.DocTypeID).  """  
      self.iOPDMDocID:str = obj["iOPDMDocID"]
      """  PDMDocID (tablenameAttch.PDMDocID).  """  
      pass

class OnChangeOfFileName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iOXFileRefNum:int = obj["parameters"]
      self.iOXFileDesc:str = obj["parameters"]
      self.iODocTypeID:str = obj["parameters"]
      self.iOPDMDocID:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDrawingsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDrawingsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DrawingsTableset] = obj["ds"]
      pass

      """  output parameters  """  

