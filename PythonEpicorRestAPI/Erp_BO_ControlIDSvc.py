import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ControlIDSvc
# Description: Master file maintenance business logic for ControlID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs",headers=creds) as resp:
           return await resp.json()

async def post_ControlIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ControlIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlIDs_Company_ControlIDCode(Company, ControlIDCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlID item
   Description: Calls GetByID to retrieve the ControlID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs(" + Company + "," + ControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlIDs_Company_ControlIDCode(Company, ControlIDCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlID for the service
   Description: Calls UpdateExt to update ControlID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs(" + Company + "," + ControlIDCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlIDs_Company_ControlIDCode(Company, ControlIDCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlID item
   Description: Call UpdateExt to delete ControlID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs(" + Company + "," + ControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDs_Company_ControlIDCode_ControlIDSegments(Company, ControlIDCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ControlIDSegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ControlIDSegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs(" + Company + "," + ControlIDCode + ")/ControlIDSegments",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDs_Company_ControlIDCode_ControlIDSegments_Company_ControlIDCode_SegmentNum(Company, ControlIDCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDSegment item
   Description: Calls GetByID to retrieve the ControlIDSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDSegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDs(" + Company + "," + ControlIDCode + ")/ControlIDSegments(" + Company + "," + ControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDSegments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlIDSegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDSegments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDSegments",headers=creds) as resp:
           return await resp.json()

async def post_ControlIDSegments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDSegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ControlIDSegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDSegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlIDSegments_Company_ControlIDCode_SegmentNum(Company, ControlIDCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDSegment item
   Description: Calls GetByID to retrieve the ControlIDSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDSegments(" + Company + "," + ControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlIDSegments_Company_ControlIDCode_SegmentNum(Company, ControlIDCode, SegmentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlIDSegment for the service
   Description: Calls UpdateExt to update ControlIDSegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDSegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDSegments(" + Company + "," + ControlIDCode + "," + SegmentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlIDSegments_Company_ControlIDCode_SegmentNum(Company, ControlIDCode, SegmentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlIDSegment item
   Description: Call UpdateExt to delete ControlIDSegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDCode: Desc: ControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/ControlIDSegments(" + Company + "," + ControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseControlID, whereClauseControlIDSegment, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseControlID=" + whereClauseControlID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseControlIDSegment=" + whereClauseControlIDSegment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(controlIDCode, epicorHeaders = None):
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
   params += "controlIDCode=" + controlIDCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_WarningControlIDDeactivation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarningControlIDDeactivation
   Description: When active segment was deactivated, verifies if Control ID is still Active, to send a warning message to the user.
   OperationID: WarningControlIDDeactivation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarningControlIDDeactivation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarningControlIDDeactivation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List from Service Designer.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlIDSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlIDSegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlIDSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDSegmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDSegmentRow] = obj["value"]
      pass

class Erp_Tablesets_ControlIDListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.ControlIDDesc:str = obj["ControlIDDesc"]
      """  Description of the Control ID Code.  """  
      self.ControlIDType:str = obj["ControlIDType"]
      """  Identifies the Control ID Type.  Valid values are Package, Serial, and Load.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Control ID Code has been used.  Default is false.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.ControlIDDesc:str = obj["ControlIDDesc"]
      """  Description of the Control ID Code.  """  
      self.ControlIDType:str = obj["ControlIDType"]
      """  Identifies the Control ID Type.  Valid values are Package, Serial, and Load.  """  
      self.RangeFrom:str = obj["RangeFrom"]
      """  Control ID starting range at the company level.  """  
      self.RangeTo:str = obj["RangeTo"]
      """  Control ID ending range at the company level.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Control ID Code has been used.  Default is false.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      self.DefinedSegments:int = obj["DefinedSegments"]
      self.CharactersUsed:int = obj["CharactersUsed"]
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Unique Segment Number within the Control ID Code.  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position within the Control ID.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid values are Alphanumeric Sequential (A), Numeric Sequential (N), Date Numeric Sequential (DN), Date (D), and Fixed (F).  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  """  
      self.SegmentFormat:str = obj["SegmentFormat"]
      """  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  """  
      self.AlphaRangeFrom:str = obj["AlphaRangeFrom"]
      """  Segment starting string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeTo:str = obj["AlphaRangeTo"]
      """  Segment ending string of the alphanumeric range based on segment format.  """  
      self.NumericRangeFrom:int = obj["NumericRangeFrom"]
      """  Segment starting string of the numeric range based on segment format.  """  
      self.NumericRangeTo:int = obj["NumericRangeTo"]
      """  Segment ending string of the numeric range based on segment format.  """  
      self.RolloverTrigger:str = obj["RolloverTrigger"]
      """  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  """  
      self.RolloverAction:str = obj["RolloverAction"]
      """  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true then inactive.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  True if the Control ID format is a fixed length and should be padded to fill the format.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      self.ExampleSegmentValue:str = obj["ExampleSegmentValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   controlIDCode
   """  
   def __init__(self, obj):
      self.controlIDCode:str = obj["controlIDCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ControlIDListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.ControlIDDesc:str = obj["ControlIDDesc"]
      """  Description of the Control ID Code.  """  
      self.ControlIDType:str = obj["ControlIDType"]
      """  Identifies the Control ID Type.  Valid values are Package, Serial, and Load.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Control ID Code has been used.  Default is false.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDListTableset:
   def __init__(self, obj):
      self.ControlIDList:list[Erp_Tablesets_ControlIDListRow] = obj["ControlIDList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ControlIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.ControlIDDesc:str = obj["ControlIDDesc"]
      """  Description of the Control ID Code.  """  
      self.ControlIDType:str = obj["ControlIDType"]
      """  Identifies the Control ID Type.  Valid values are Package, Serial, and Load.  """  
      self.RangeFrom:str = obj["RangeFrom"]
      """  Control ID starting range at the company level.  """  
      self.RangeTo:str = obj["RangeTo"]
      """  Control ID ending range at the company level.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Control ID Code has been used.  Default is false.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      self.DefinedSegments:int = obj["DefinedSegments"]
      self.CharactersUsed:int = obj["CharactersUsed"]
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Unique Segment Number within the Control ID Code.  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position within the Control ID.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid values are Alphanumeric Sequential (A), Numeric Sequential (N), Date Numeric Sequential (DN), Date (D), and Fixed (F).  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  """  
      self.SegmentFormat:str = obj["SegmentFormat"]
      """  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  """  
      self.AlphaRangeFrom:str = obj["AlphaRangeFrom"]
      """  Segment starting string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeTo:str = obj["AlphaRangeTo"]
      """  Segment ending string of the alphanumeric range based on segment format.  """  
      self.NumericRangeFrom:int = obj["NumericRangeFrom"]
      """  Segment starting string of the numeric range based on segment format.  """  
      self.NumericRangeTo:int = obj["NumericRangeTo"]
      """  Segment ending string of the numeric range based on segment format.  """  
      self.RolloverTrigger:str = obj["RolloverTrigger"]
      """  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  """  
      self.RolloverAction:str = obj["RolloverAction"]
      """  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true then inactive.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  True if the Control ID format is a fixed length and should be padded to fill the format.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      self.ExampleSegmentValue:str = obj["ExampleSegmentValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDTableset:
   def __init__(self, obj):
      self.ControlID:list[Erp_Tablesets_ControlIDRow] = obj["ControlID"]
      self.ControlIDSegment:list[Erp_Tablesets_ControlIDSegmentRow] = obj["ControlIDSegment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtControlIDTableset:
   def __init__(self, obj):
      self.ControlID:list[Erp_Tablesets_ControlIDRow] = obj["ControlID"]
      self.ControlIDSegment:list[Erp_Tablesets_ControlIDSegmentRow] = obj["ControlIDSegment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   controlIDCode
   """  
   def __init__(self, obj):
      self.controlIDCode:str = obj["controlIDCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ControlIDTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewControlIDSegment_input:
   """ Required : 
   ds
   controlIDCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      self.controlIDCode:str = obj["controlIDCode"]
      pass

class GetNewControlIDSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewControlID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

class GetNewControlID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseControlID
   whereClauseControlIDSegment
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseControlID:str = obj["whereClauseControlID"]
      self.whereClauseControlIDSegment:str = obj["whereClauseControlIDSegment"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ControlIDTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtControlIDTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtControlIDTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class WarningControlIDDeactivation_input:
   """ Required : 
   controlCode
   segmentNum
   ds
   """  
   def __init__(self, obj):
      self.controlCode:str = obj["controlCode"]
      self.segmentNum:int = obj["segmentNum"]
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      pass

class WarningControlIDDeactivation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDTableset] = obj["ds"]
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

