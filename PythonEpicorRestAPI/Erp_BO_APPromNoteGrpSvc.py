import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APPromNoteGrpSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APPromNoteGrps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPromNoteGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPromNoteGrps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps",headers=creds) as resp:
           return await resp.json()

async def post_APPromNoteGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPromNoteGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPromNoteGrps_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPromNoteGrp item
   Description: Calls GetByID to retrieve the APPromNoteGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPromNoteGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPromNoteGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPromNoteGrp for the service
   Description: Calls UpdateExt to update APPromNoteGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPromNoteGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPromNoteGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPromNoteGrp item
   Description: Call UpdateExt to delete APPromNoteGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPromNoteGrp
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPromNoteGrps_Company_GroupID_APChkGrpAttches(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APChkGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APChkGrpAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")/APChkGrpAttches",headers=creds) as resp:
           return await resp.json()

async def get_APPromNoteGrps_Company_GroupID_APChkGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APChkGrpAttch item
   Description: Calls GetByID to retrieve the APChkGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APChkGrpAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APChkGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APChkGrpAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches",headers=creds) as resp:
           return await resp.json()

async def post_APChkGrpAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APChkGrpAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APChkGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APChkGrpAttch item
   Description: Calls GetByID to retrieve the APChkGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APChkGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APChkGrpAttch for the service
   Description: Calls UpdateExt to update APChkGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APChkGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APChkGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APChkGrpAttch item
   Description: Call UpdateExt to delete APChkGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APChkGrpAttch
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPChkGrp, whereClauseAPChkGrpAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPChkGrp=" + whereClauseAPChkGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPChkGrpAttch=" + whereClauseAPChkGrpAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPChkGrpNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPChkGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewAPChkGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForEditList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForEditList
   Description: This method informs the user if any of PI of this Group will not be included in Edit List
because of their First GL Stage Update status
   OperationID: CheckForEditList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForEditList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForEditList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZeroAmtTaxRec(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since  TAx logic calculates tax conditionally only for the first tax line the invoice could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockGroup
   Description: This procedure is GetById + Lock the Group.  This procedure can be run
instead of GetById if you want to lock along with doing a GetByID.
If the lock is acquired successfully, plSuccess is returned as true.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: Call this method when the user changes the Bank Account.
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostGrp
   Description: Method to call before posting invoices for a specific group..  This method will check if there are
records with zero tax amounts and return
message text asking the user if they would like to continue with posting or delete these tax records.
   OperationID: PrePostGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetBankAcctID
   Description: Purpose:     Set Bank Account ID before updating a just created ApChkGrp record.
Parameters:  APPromNoteGrp DataSet
Notes:
   OperationID: SetBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnLockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnLockGroup
   Description: Unlock the group.  The user who locked the group can only unlock it.
   OperationID: UnLockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPChkGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPChkGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPChkGrpAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPChkGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APChkGrpRow] = obj["value"]
      pass

class Erp_Tablesets_APChkGrpAttchRow:
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

class Erp_Tablesets_APChkGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains error messages returned by the Post process.  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  Payment Instrument  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Yes if group having payment method with type ?Electronic Interface? was successfully processed  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.TotalCheckAmt:int = obj["TotalCheckAmt"]
      self.TotalDocCheckAmt:int = obj["TotalDocCheckAmt"]
      self.TotalMiscCheckAmt:int = obj["TotalMiscCheckAmt"]
      self.TotalAmountToAP:int = obj["TotalAmountToAP"]
      self.TotalDiscAmt:int = obj["TotalDiscAmt"]
      self.TotalDocDiscAmt:int = obj["TotalDocDiscAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.TotalDocMiscCheckAmt:int = obj["TotalDocMiscCheckAmt"]
      self.BankAcctIDEnabled:bool = obj["BankAcctIDEnabled"]
      self.Rpt1TotalCheckAmt:int = obj["Rpt1TotalCheckAmt"]
      self.Rpt2TotalCheckAmt:int = obj["Rpt2TotalCheckAmt"]
      self.Rpt3TotalCheckAmt:int = obj["Rpt3TotalCheckAmt"]
      self.Rpt1TotalDiscAmt:int = obj["Rpt1TotalDiscAmt"]
      self.Rpt2TotalDiscAmt:int = obj["Rpt2TotalDiscAmt"]
      self.Rpt3TotalDiscAmt:int = obj["Rpt3TotalDiscAmt"]
      self.Rpt1TotalMiscCheckAmt:int = obj["Rpt1TotalMiscCheckAmt"]
      self.Rpt2TotalMiscCheckAmt:int = obj["Rpt2TotalMiscCheckAmt"]
      self.Rpt3TotalMiscCheckAmt:int = obj["Rpt3TotalMiscCheckAmt"]
      self.TotalWithHoldTax:int = obj["TotalWithHoldTax"]
      self.TotalDocWithHoldTax:int = obj["TotalDocWithHoldTax"]
      self.Rpt1TotalWithHoldTax:int = obj["Rpt1TotalWithHoldTax"]
      self.Rpt3TotalWithHoldTax:int = obj["Rpt3TotalWithHoldTax"]
      self.Rpt2TotalWithHoldTax:int = obj["Rpt2TotalWithHoldTax"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      self.PymtProposal:bool = obj["PymtProposal"]
      self.BankTotalCheckAmt:int = obj["BankTotalCheckAmt"]
      self.BankTotalMiscCheckAmt:int = obj["BankTotalMiscCheckAmt"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankTotalDiscAmt:int = obj["BankTotalDiscAmt"]
      self.BankTotalWithholdTax:int = obj["BankTotalWithholdTax"]
      self.BankTotalAmountToAP:int = obj["BankTotalAmountToAP"]
      self.TotalDocAmountToAP:int = obj["TotalDocAmountToAP"]
      self.BankCurrDesc:str = obj["BankCurrDesc"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.FromImportPmt:bool = obj["FromImportPmt"]
      """  The flag to indicate if this Payment Group is created by processing Bank Import File.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.PayMethodOnlyBankCurr:bool = obj["PayMethodOnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
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
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APChkGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains error messages returned by the Post process.  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  Payment Instrument  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Yes if group having payment method with type ?Electronic Interface? was successfully processed  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Auto Generated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHOrderNum:int = obj["CHOrderNum"]
      """  CHOrderNum  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.CentralizedPayment:bool = obj["CentralizedPayment"]
      """  CentralizedPayment  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankTotalAmountToAP:int = obj["BankTotalAmountToAP"]
      self.BankTotalCheckAmt:int = obj["BankTotalCheckAmt"]
      self.BankTotalDiscAmt:int = obj["BankTotalDiscAmt"]
      self.BankTotalMiscCheckAmt:int = obj["BankTotalMiscCheckAmt"]
      self.BankTotalWithholdTax:int = obj["BankTotalWithholdTax"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      """  Displays the currency or currencies of payments in the group. If more than one payment currency is used in the group, user is able to switch between currencies to see total cash and total AP for the group, specific to the payments in that selected currency.  """  
      self.DocBankTotalCheckAmt:int = obj["DocBankTotalCheckAmt"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      """  Displays the generated batch reference for the group when batches are being used for the selected payment method.  """  
      self.EFTAllowZeroNet:bool = obj["EFTAllowZeroNet"]
      """  Yes if group having payment method with type ?Electronic Interface? allows for zero balance payments  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  Debit Memo due date on credits for Type 2 payments.  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  Special code to handle EFT payments, this is defined by the CSF as needed.  """  
      self.EIGrouping:bool = obj["EIGrouping"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.FromImportPmt:bool = obj["FromImportPmt"]
      """  The flag to indicate if this Payment Group is created by processing Bank Import File.  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  Norway CSF: is Nordea payment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  Norway CSF: Telepay Reply  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      self.Rpt1BankTotalCheckAmt:int = obj["Rpt1BankTotalCheckAmt"]
      self.Rpt1TotalCheckAmt:int = obj["Rpt1TotalCheckAmt"]
      self.Rpt1TotalDiscAmt:int = obj["Rpt1TotalDiscAmt"]
      self.Rpt1TotalMiscCheckAmt:int = obj["Rpt1TotalMiscCheckAmt"]
      self.Rpt1TotalWithHoldTax:int = obj["Rpt1TotalWithHoldTax"]
      self.Rpt2BankTotalCheckAmt:int = obj["Rpt2BankTotalCheckAmt"]
      self.Rpt2TotalCheckAmt:int = obj["Rpt2TotalCheckAmt"]
      self.Rpt2TotalDiscAmt:int = obj["Rpt2TotalDiscAmt"]
      self.Rpt2TotalMiscCheckAmt:int = obj["Rpt2TotalMiscCheckAmt"]
      self.Rpt2TotalWithHoldTax:int = obj["Rpt2TotalWithHoldTax"]
      self.Rpt3BankTotalCheckAmt:int = obj["Rpt3BankTotalCheckAmt"]
      self.Rpt3TotalCheckAmt:int = obj["Rpt3TotalCheckAmt"]
      self.Rpt3TotalDiscAmt:int = obj["Rpt3TotalDiscAmt"]
      self.Rpt3TotalMiscCheckAmt:int = obj["Rpt3TotalMiscCheckAmt"]
      self.Rpt3TotalWithHoldTax:int = obj["Rpt3TotalWithHoldTax"]
      self.SEEFTPO3Payment:bool = obj["SEEFTPO3Payment"]
      self.TotalAmountToAP:int = obj["TotalAmountToAP"]
      """  Total AP amount for the payment entry group.  """  
      self.TotalCheckAmt:int = obj["TotalCheckAmt"]
      """  Total Cash amount for the payment entry group.  """  
      self.TotalDiscAmt:int = obj["TotalDiscAmt"]
      """  Total discount amount for the payment entry group.  """  
      self.TotalDocAmountToAP:int = obj["TotalDocAmountToAP"]
      """  Total AP amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocCheckAmt:int = obj["TotalDocCheckAmt"]
      """  Total Cash amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocDiscAmt:int = obj["TotalDocDiscAmt"]
      """  Total discount amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocMiscCheckAmt:int = obj["TotalDocMiscCheckAmt"]
      """  Total miscellaneous amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocWithHoldTax:int = obj["TotalDocWithHoldTax"]
      """  Total withholding tax amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalMiscCheckAmt:int = obj["TotalMiscCheckAmt"]
      """  Total miscellaneous amount for the payment entry group.  """  
      self.TotalWithHoldTax:int = obj["TotalWithHoldTax"]
      """  Total withholding tax amount for the payment entry group.  """  
      self.UIGrouping:bool = obj["UIGrouping"]
      self.BankAcctIDEnabled:bool = obj["BankAcctIDEnabled"]
      self.BankCurrDesc:str = obj["BankCurrDesc"]
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Indicates if the selected bank account uses average rates on payments.  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  Indicates that the group is locked and currently in journal review.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: a payment is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.PayMethodOnlyBankCurr:bool = obj["PayMethodOnlyBankCurr"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckForEditList_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group for Edit List  """  
      pass

class CheckForEditList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.noPI:bool = obj["noPI"]
      self.noPIList:str = obj["parameters"]
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

class DeleteZeroAmtTaxRec_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class DeleteZeroAmtTaxRec_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APChkGrpAttchRow:
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

class Erp_Tablesets_APChkGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains error messages returned by the Post process.  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  Payment Instrument  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Yes if group having payment method with type ?Electronic Interface? was successfully processed  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.TotalCheckAmt:int = obj["TotalCheckAmt"]
      self.TotalDocCheckAmt:int = obj["TotalDocCheckAmt"]
      self.TotalMiscCheckAmt:int = obj["TotalMiscCheckAmt"]
      self.TotalAmountToAP:int = obj["TotalAmountToAP"]
      self.TotalDiscAmt:int = obj["TotalDiscAmt"]
      self.TotalDocDiscAmt:int = obj["TotalDocDiscAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.TotalDocMiscCheckAmt:int = obj["TotalDocMiscCheckAmt"]
      self.BankAcctIDEnabled:bool = obj["BankAcctIDEnabled"]
      self.Rpt1TotalCheckAmt:int = obj["Rpt1TotalCheckAmt"]
      self.Rpt2TotalCheckAmt:int = obj["Rpt2TotalCheckAmt"]
      self.Rpt3TotalCheckAmt:int = obj["Rpt3TotalCheckAmt"]
      self.Rpt1TotalDiscAmt:int = obj["Rpt1TotalDiscAmt"]
      self.Rpt2TotalDiscAmt:int = obj["Rpt2TotalDiscAmt"]
      self.Rpt3TotalDiscAmt:int = obj["Rpt3TotalDiscAmt"]
      self.Rpt1TotalMiscCheckAmt:int = obj["Rpt1TotalMiscCheckAmt"]
      self.Rpt2TotalMiscCheckAmt:int = obj["Rpt2TotalMiscCheckAmt"]
      self.Rpt3TotalMiscCheckAmt:int = obj["Rpt3TotalMiscCheckAmt"]
      self.TotalWithHoldTax:int = obj["TotalWithHoldTax"]
      self.TotalDocWithHoldTax:int = obj["TotalDocWithHoldTax"]
      self.Rpt1TotalWithHoldTax:int = obj["Rpt1TotalWithHoldTax"]
      self.Rpt3TotalWithHoldTax:int = obj["Rpt3TotalWithHoldTax"]
      self.Rpt2TotalWithHoldTax:int = obj["Rpt2TotalWithHoldTax"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      self.PymtProposal:bool = obj["PymtProposal"]
      self.BankTotalCheckAmt:int = obj["BankTotalCheckAmt"]
      self.BankTotalMiscCheckAmt:int = obj["BankTotalMiscCheckAmt"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankTotalDiscAmt:int = obj["BankTotalDiscAmt"]
      self.BankTotalWithholdTax:int = obj["BankTotalWithholdTax"]
      self.BankTotalAmountToAP:int = obj["BankTotalAmountToAP"]
      self.TotalDocAmountToAP:int = obj["TotalDocAmountToAP"]
      self.BankCurrDesc:str = obj["BankCurrDesc"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.FromImportPmt:bool = obj["FromImportPmt"]
      """  The flag to indicate if this Payment Group is created by processing Bank Import File.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.PayMethodOnlyBankCurr:bool = obj["PayMethodOnlyBankCurr"]
      """  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  """  
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
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APChkGrpListTableset:
   def __init__(self, obj):
      self.APChkGrpList:list[Erp_Tablesets_APChkGrpListRow] = obj["APChkGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APChkGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.Cashbook:bool = obj["Cashbook"]
      """  if this group is created by the Cashbook then other programs can not select this group.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """  Contains error messages returned by the Post process.  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PromissoryNote:bool = obj["PromissoryNote"]
      """  Payment Instrument  """  
      self.EIPaymSent:bool = obj["EIPaymSent"]
      """  Yes if group having payment method with type ?Electronic Interface? was successfully processed  """  
      self.GrpCreationVia:str = obj["GrpCreationVia"]
      """   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Auto Generated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHOrderNum:int = obj["CHOrderNum"]
      """  CHOrderNum  """  
      self.NOPaymentList:bool = obj["NOPaymentList"]
      """  NOPaymentList  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.CentralizedPayment:bool = obj["CentralizedPayment"]
      """  CentralizedPayment  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankTotalAmountToAP:int = obj["BankTotalAmountToAP"]
      self.BankTotalCheckAmt:int = obj["BankTotalCheckAmt"]
      self.BankTotalDiscAmt:int = obj["BankTotalDiscAmt"]
      self.BankTotalMiscCheckAmt:int = obj["BankTotalMiscCheckAmt"]
      self.BankTotalWithholdTax:int = obj["BankTotalWithholdTax"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencyList:str = obj["CurrencyList"]
      self.DispCurrencyCode:str = obj["DispCurrencyCode"]
      """  Displays the currency or currencies of payments in the group. If more than one payment currency is used in the group, user is able to switch between currencies to see total cash and total AP for the group, specific to the payments in that selected currency.  """  
      self.DocBankTotalCheckAmt:int = obj["DocBankTotalCheckAmt"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      """  Displays the generated batch reference for the group when batches are being used for the selected payment method.  """  
      self.EFTAllowZeroNet:bool = obj["EFTAllowZeroNet"]
      """  Yes if group having payment method with type ?Electronic Interface? allows for zero balance payments  """  
      self.EFTDebitMemoDueDate:str = obj["EFTDebitMemoDueDate"]
      """  Debit Memo due date on credits for Type 2 payments.  """  
      self.EFTDebitMemoHandlingCode:str = obj["EFTDebitMemoHandlingCode"]
      """  Special code to handle EFT payments, this is defined by the CSF as needed.  """  
      self.EIGrouping:bool = obj["EIGrouping"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.FromImportPmt:bool = obj["FromImportPmt"]
      """  The flag to indicate if this Payment Group is created by processing Bank Import File.  """  
      self.NOTelepayPayment:bool = obj["NOTelepayPayment"]
      """  Norway CSF: is Nordea payment  """  
      self.NOTelepayReply:bool = obj["NOTelepayReply"]
      """  Norway CSF: Telepay Reply  """  
      self.PymtProposal:bool = obj["PymtProposal"]
      self.Rpt1BankTotalCheckAmt:int = obj["Rpt1BankTotalCheckAmt"]
      self.Rpt1TotalCheckAmt:int = obj["Rpt1TotalCheckAmt"]
      self.Rpt1TotalDiscAmt:int = obj["Rpt1TotalDiscAmt"]
      self.Rpt1TotalMiscCheckAmt:int = obj["Rpt1TotalMiscCheckAmt"]
      self.Rpt1TotalWithHoldTax:int = obj["Rpt1TotalWithHoldTax"]
      self.Rpt2BankTotalCheckAmt:int = obj["Rpt2BankTotalCheckAmt"]
      self.Rpt2TotalCheckAmt:int = obj["Rpt2TotalCheckAmt"]
      self.Rpt2TotalDiscAmt:int = obj["Rpt2TotalDiscAmt"]
      self.Rpt2TotalMiscCheckAmt:int = obj["Rpt2TotalMiscCheckAmt"]
      self.Rpt2TotalWithHoldTax:int = obj["Rpt2TotalWithHoldTax"]
      self.Rpt3BankTotalCheckAmt:int = obj["Rpt3BankTotalCheckAmt"]
      self.Rpt3TotalCheckAmt:int = obj["Rpt3TotalCheckAmt"]
      self.Rpt3TotalDiscAmt:int = obj["Rpt3TotalDiscAmt"]
      self.Rpt3TotalMiscCheckAmt:int = obj["Rpt3TotalMiscCheckAmt"]
      self.Rpt3TotalWithHoldTax:int = obj["Rpt3TotalWithHoldTax"]
      self.SEEFTPO3Payment:bool = obj["SEEFTPO3Payment"]
      self.TotalAmountToAP:int = obj["TotalAmountToAP"]
      """  Total AP amount for the payment entry group.  """  
      self.TotalCheckAmt:int = obj["TotalCheckAmt"]
      """  Total Cash amount for the payment entry group.  """  
      self.TotalDiscAmt:int = obj["TotalDiscAmt"]
      """  Total discount amount for the payment entry group.  """  
      self.TotalDocAmountToAP:int = obj["TotalDocAmountToAP"]
      """  Total AP amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocCheckAmt:int = obj["TotalDocCheckAmt"]
      """  Total Cash amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocDiscAmt:int = obj["TotalDocDiscAmt"]
      """  Total discount amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocMiscCheckAmt:int = obj["TotalDocMiscCheckAmt"]
      """  Total miscellaneous amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalDocWithHoldTax:int = obj["TotalDocWithHoldTax"]
      """  Total withholding tax amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  """  
      self.TotalMiscCheckAmt:int = obj["TotalMiscCheckAmt"]
      """  Total miscellaneous amount for the payment entry group.  """  
      self.TotalWithHoldTax:int = obj["TotalWithHoldTax"]
      """  Total withholding tax amount for the payment entry group.  """  
      self.UIGrouping:bool = obj["UIGrouping"]
      self.BankAcctIDEnabled:bool = obj["BankAcctIDEnabled"]
      self.BankCurrDesc:str = obj["BankCurrDesc"]
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Indicates if the selected bank account uses average rates on payments.  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  Indicates that the group is locked and currently in journal review.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be posted: a payment is already in review journal or in posting process.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.PayMethodOnlyBankCurr:bool = obj["PayMethodOnlyBankCurr"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPromNoteGrpTableset:
   def __init__(self, obj):
      self.APChkGrp:list[Erp_Tablesets_APChkGrpRow] = obj["APChkGrp"]
      self.APChkGrpAttch:list[Erp_Tablesets_APChkGrpAttchRow] = obj["APChkGrpAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAPPromNoteGrpTableset:
   def __init__(self, obj):
      self.APChkGrp:list[Erp_Tablesets_APChkGrpRow] = obj["APChkGrp"]
      self.APChkGrpAttch:list[Erp_Tablesets_APChkGrpAttchRow] = obj["APChkGrpAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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
      self.returnObj:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APChkGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPChkGrpAttch_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewAPChkGrpAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPChkGrpNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

class GetNewAPChkGrpNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPChkGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

class GetNewAPChkGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPChkGrp
   whereClauseAPChkGrpAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPChkGrp:str = obj["whereClauseAPChkGrp"]
      self.whereClauseAPChkGrpAttch:str = obj["whereClauseAPChkGrpAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["returnObj"]
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

class LockGroup_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  The Group ID selected by the user.  """  
      pass

class LockGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.plSuccess:bool = obj["plSuccess"]
      pass

      """  output parameters  """  

class OnChangeBankAcctID_input:
   """ Required : 
   pcBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  The proposed value of BankAcctID.  """  
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePostGrp_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The Group ID of the Group to post  """  
      pass

class PrePostGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.taxRecMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetBankAcctID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

class SetBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnLockGroup_input:
   """ Required : 
   pcGroupID
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  The Group ID selected by the user.  """  
      pass

class UnLockGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plSuccess:bool = obj["plSuccess"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPPromNoteGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPPromNoteGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPromNoteGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

