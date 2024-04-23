import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MaintReqSvc
# Description: Maintenance Request Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MaintReqs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MaintReqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaintReqs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs",headers=creds) as resp:
           return await resp.json()

async def post_MaintReqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaintReqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MaintReqs_Company_Plant_ReqID(Company, Plant, ReqID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MaintReq item
   Description: Calls GetByID to retrieve the MaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MaintReqs_Company_Plant_ReqID(Company, Plant, ReqID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MaintReq for the service
   Description: Calls UpdateExt to update MaintReq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaintReq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MaintReqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MaintReqs_Company_Plant_ReqID(Company, Plant, ReqID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MaintReq item
   Description: Call UpdateExt to delete MaintReq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaintReq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MaintReqs_Company_Plant_ReqID_MaintReqAttches(Company, Plant, ReqID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MaintReqAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MaintReqAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")/MaintReqAttches",headers=creds) as resp:
           return await resp.json()

async def get_MaintReqs_Company_Plant_ReqID_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company, Plant, ReqID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MaintReqAttch item
   Description: Calls GetByID to retrieve the MaintReqAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReqAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqs(" + Company + "," + Plant + "," + ReqID + ")/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MaintReqAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MaintReqAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaintReqAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches",headers=creds) as resp:
           return await resp.json()

async def post_MaintReqAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaintReqAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company, Plant, ReqID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MaintReqAttch item
   Description: Calls GetByID to retrieve the MaintReqAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaintReqAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company, Plant, ReqID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MaintReqAttch for the service
   Description: Calls UpdateExt to update MaintReqAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaintReqAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MaintReqAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MaintReqAttches_Company_Plant_ReqID_DrawingSeq(Company, Plant, ReqID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MaintReqAttch item
   Description: Call UpdateExt to delete MaintReqAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaintReqAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ReqID: Desc: ReqID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/MaintReqAttches(" + Company + "," + Plant + "," + ReqID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MaintReqListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMaintReq, whereClauseMaintReqAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMaintReq=" + whereClauseMaintReq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMaintReqAttch=" + whereClauseMaintReqAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, reqID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "reqID=" + reqID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnApproveJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnApproveJob
   Description: This method should be called when request is approved.
   OperationID: OnApproveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnApproveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnApproveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEquipID
   Description: This method should be called when EquipID change.
   OperationID: OnChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIssueTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: OnChangeIssueTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResTopics
   Description: This method should be invoked when the ResTopics changes.
Validates and sets the individual ResTopic fields.
   OperationID: OnChangeResTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StatusRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StatusRequest
   Description: This method should be called when Status Request is changed.
   OperationID: StatusRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StatusRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StatusRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMaintPlant(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMaintPlant
   Description: Purpose: Rejecting or Approving a Maintenance Request requires that it is done from
the plant that is responsible for maintenance of the Requesting Plant.
Parameters:  none
Notes:
   OperationID: ValidateMaintPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaintPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewMaintReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMaintReq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMaintReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMaintReqAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMaintReqAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMaintReqAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMaintReqAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMaintReqAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaintReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MaintReqAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MaintReqListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MaintReqRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MaintReqRow] = obj["value"]
      pass

class Erp_Tablesets_MaintReqAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
      self.ReqID:str = obj["ReqID"]
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

class Erp_Tablesets_MaintReqListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.EquipID:str = obj["EquipID"]
      """  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  """  
      self.ReqStatus:str = obj["ReqStatus"]
      """   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  """  
      self.RequiredDate:str = obj["RequiredDate"]
      """  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  """  
      self.Priority:str = obj["Priority"]
      """  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  """  
      self.IssueDesc:str = obj["IssueDesc"]
      """  Describes the issue with the equipment that is prompting this request for maintenance.  """  
      self.Requestor:str = obj["Requestor"]
      """  User ID that made the Request.  """  
      self.Reviewer:str = obj["Reviewer"]
      """  User ID that reviewed the request.  """  
      self.RequestDt:str = obj["RequestDt"]
      """  Date the request was created  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time the Request was made. Expressed as seconds since midnight.  """  
      self.ResponseDate:str = obj["ResponseDate"]
      """  Date when the response was received.  """  
      self.ResponseTime:int = obj["ResponseTime"]
      """  Time the Response was made. Expressed as seconds since midnight.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  """  
      self.ResDesc:str = obj["ResDesc"]
      """  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  """  
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.EquipIDInServiceDate:str = obj["EquipIDInServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.EquipIDModel:str = obj["EquipIDModel"]
      """  Model Number  """  
      self.EquipIDTypeID:str = obj["EquipIDTypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.EquipIDOEM:str = obj["EquipIDOEM"]
      """  OEM Number  """  
      self.EquipIDWarrantyExpDate:str = obj["EquipIDWarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.EquipIDSerialNum:str = obj["EquipIDSerialNum"]
      """  Serial Number of equipment  """  
      self.EquipIDLocID:str = obj["EquipIDLocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.EquipIDPlant:str = obj["EquipIDPlant"]
      """  Plant in which the equipment is currently located.  """  
      self.EquipIDBrand:str = obj["EquipIDBrand"]
      """  Brand of equipment  """  
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      """  Full description of the Help Desk topic.  """  
      self.SchedPriDescription:str = obj["SchedPriDescription"]
      """  Description of the priority.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MaintReqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.EquipID:str = obj["EquipID"]
      """  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  """  
      self.ReqStatus:str = obj["ReqStatus"]
      """   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  """  
      self.RequiredDate:str = obj["RequiredDate"]
      """  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  """  
      self.Priority:str = obj["Priority"]
      """  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  """  
      self.IssueDesc:str = obj["IssueDesc"]
      """  Describes the issue with the equipment that is prompting this request for maintenance.  """  
      self.Requestor:str = obj["Requestor"]
      """  User ID that made the Request.  """  
      self.Reviewer:str = obj["Reviewer"]
      """  User ID that reviewed the request.  """  
      self.RequestDt:str = obj["RequestDt"]
      """  Date the request was created  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time the Request was made. Expressed as seconds since midnight.  """  
      self.ResponseDate:str = obj["ResponseDate"]
      """  Date when the response was received.  """  
      self.ResponseTime:int = obj["ResponseTime"]
      """  Time the Response was made. Expressed as seconds since midnight.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  """  
      self.ResDesc:str = obj["ResDesc"]
      """  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EquipIDBrand:str = obj["EquipIDBrand"]
      self.EquipIDOEM:str = obj["EquipIDOEM"]
      self.EquipIDLocID:str = obj["EquipIDLocID"]
      self.EquipIDTypeID:str = obj["EquipIDTypeID"]
      self.EquipIDModel:str = obj["EquipIDModel"]
      self.EquipIDInServiceDate:str = obj["EquipIDInServiceDate"]
      self.EquipIDSerialNum:str = obj["EquipIDSerialNum"]
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      self.EquipIDPlant:str = obj["EquipIDPlant"]
      self.EquipIDWarrantyExpDate:str = obj["EquipIDWarrantyExpDate"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedPriDescription:str = obj["SchedPriDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   reqID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.reqID:str = obj["reqID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MaintReqAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
      self.ReqID:str = obj["ReqID"]
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

class Erp_Tablesets_MaintReqListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.EquipID:str = obj["EquipID"]
      """  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  """  
      self.ReqStatus:str = obj["ReqStatus"]
      """   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  """  
      self.RequiredDate:str = obj["RequiredDate"]
      """  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  """  
      self.Priority:str = obj["Priority"]
      """  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  """  
      self.IssueDesc:str = obj["IssueDesc"]
      """  Describes the issue with the equipment that is prompting this request for maintenance.  """  
      self.Requestor:str = obj["Requestor"]
      """  User ID that made the Request.  """  
      self.Reviewer:str = obj["Reviewer"]
      """  User ID that reviewed the request.  """  
      self.RequestDt:str = obj["RequestDt"]
      """  Date the request was created  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time the Request was made. Expressed as seconds since midnight.  """  
      self.ResponseDate:str = obj["ResponseDate"]
      """  Date when the response was received.  """  
      self.ResponseTime:int = obj["ResponseTime"]
      """  Time the Response was made. Expressed as seconds since midnight.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  """  
      self.ResDesc:str = obj["ResDesc"]
      """  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  """  
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.EquipIDInServiceDate:str = obj["EquipIDInServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.EquipIDModel:str = obj["EquipIDModel"]
      """  Model Number  """  
      self.EquipIDTypeID:str = obj["EquipIDTypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.EquipIDOEM:str = obj["EquipIDOEM"]
      """  OEM Number  """  
      self.EquipIDWarrantyExpDate:str = obj["EquipIDWarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.EquipIDSerialNum:str = obj["EquipIDSerialNum"]
      """  Serial Number of equipment  """  
      self.EquipIDLocID:str = obj["EquipIDLocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.EquipIDPlant:str = obj["EquipIDPlant"]
      """  Plant in which the equipment is currently located.  """  
      self.EquipIDBrand:str = obj["EquipIDBrand"]
      """  Brand of equipment  """  
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      """  Full description of the Help Desk topic.  """  
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      """  Full description of the Help Desk topic.  """  
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      """  Full description of the Help Desk topic.  """  
      self.SchedPriDescription:str = obj["SchedPriDescription"]
      """  Description of the priority.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MaintReqListTableset:
   def __init__(self, obj):
      self.MaintReqList:list[Erp_Tablesets_MaintReqListRow] = obj["MaintReqList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MaintReqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.EquipID:str = obj["EquipID"]
      """  Indentifies the piece of equipment that the MR is for. Must be valid in the Equip table, and must be in the same Site.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if MR is Open or Closed. A request remains Open until it is either rejected and acknowledged in MR Entry, Cancelled, or the maintenance job is Close.  """  
      self.ReqStatus:str = obj["ReqStatus"]
      """   Response from Reviewer.
Pnd - Pending, Aprv - Approved, Rej - Rejected.
The Requestor can Cancel the request "Can" - Cancelled,  """  
      self.RequiredDate:str = obj["RequiredDate"]
      """  The date that maintenance is required by.  Will be used as default due date of the Maintenance Job (JobHead.ReqDueDate)  """  
      self.Priority:str = obj["Priority"]
      """  Priority of this request. Will be used to set the JobHead.SchedCode. Must be a valid value in SchedPri table.  """  
      self.IssueDesc:str = obj["IssueDesc"]
      """  Describes the issue with the equipment that is prompting this request for maintenance.  """  
      self.Requestor:str = obj["Requestor"]
      """  User ID that made the Request.  """  
      self.Reviewer:str = obj["Reviewer"]
      """  User ID that reviewed the request.  """  
      self.RequestDt:str = obj["RequestDt"]
      """  Date the request was created  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time the Request was made. Expressed as seconds since midnight.  """  
      self.ResponseDate:str = obj["ResponseDate"]
      """  Date when the response was received.  """  
      self.ResponseTime:int = obj["ResponseTime"]
      """  Time the Response was made. Expressed as seconds since midnight.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number that is assigned to this Maintenance Request. A read only field updated by the system with the Request is Approved.  """  
      self.ResDesc:str = obj["ResDesc"]
      """  Describes the Resoltion of this request.  This and the 3 ResID fields only pertains to Request that were Cancelled.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1. Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent only when Request is cancelled. (ReqStatus = "CAN") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  Pertinent only when Request is cancelled.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  The Site that handles Maintenance for the Request.  A Request is created for a piece of Equipment in a Site.  That Site may have another Site designated as its "Maintenance Site".  See Site.MaintSite.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  Used as an alternate method to enter Resolution Topics.  A space separated list of ResTopicID's. They will update the physical ResTopicID1 - 10 fields.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EquipIDBrand:str = obj["EquipIDBrand"]
      self.EquipIDOEM:str = obj["EquipIDOEM"]
      self.EquipIDLocID:str = obj["EquipIDLocID"]
      self.EquipIDTypeID:str = obj["EquipIDTypeID"]
      self.EquipIDModel:str = obj["EquipIDModel"]
      self.EquipIDInServiceDate:str = obj["EquipIDInServiceDate"]
      self.EquipIDSerialNum:str = obj["EquipIDSerialNum"]
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      self.EquipIDPlant:str = obj["EquipIDPlant"]
      self.EquipIDWarrantyExpDate:str = obj["EquipIDWarrantyExpDate"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedPriDescription:str = obj["SchedPriDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MaintReqTableset:
   def __init__(self, obj):
      self.MaintReq:list[Erp_Tablesets_MaintReqRow] = obj["MaintReq"]
      self.MaintReqAttch:list[Erp_Tablesets_MaintReqAttchRow] = obj["MaintReqAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMaintReqTableset:
   def __init__(self, obj):
      self.MaintReq:list[Erp_Tablesets_MaintReqRow] = obj["MaintReq"]
      self.MaintReqAttch:list[Erp_Tablesets_MaintReqAttchRow] = obj["MaintReqAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   reqID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.reqID:str = obj["reqID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaintReqTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MaintReqTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MaintReqTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MaintReqListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMaintReqAttch_input:
   """ Required : 
   ds
   plant
   reqID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.reqID:str = obj["reqID"]
      pass

class GetNewMaintReqAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMaintReq_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewMaintReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMaintReq
   whereClauseMaintReqAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMaintReq:str = obj["whereClauseMaintReq"]
      self.whereClauseMaintReqAttch:str = obj["whereClauseMaintReqAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaintReqTableset] = obj["returnObj"]
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

class OnApproveJob_input:
   """ Required : 
   plant
   reqID
   onHold
   ds
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      """  plant  """  
      self.reqID:str = obj["reqID"]
      """  reqID  """  
      self.onHold:bool = obj["onHold"]
      """  onHold  """  
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class OnApproveJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEquipID_input:
   """ Required : 
   equipID
   ds
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  equipID  """  
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class OnChangeEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeIssueTopics_input:
   """ Required : 
   topics
   ds
   """  
   def __init__(self, obj):
      self.topics:str = obj["topics"]
      """  Proposed topics string id  """  
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class OnChangeIssueTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResTopics_input:
   """ Required : 
   topics
   ds
   """  
   def __init__(self, obj):
      self.topics:str = obj["topics"]
      """  Proposed topics string id  """  
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class OnChangeResTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StatusRequest_input:
   """ Required : 
   ipReqID
   ipPlant
   ipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipReqID:str = obj["ipReqID"]
      """  RequestID  """  
      self.ipPlant:str = obj["ipPlant"]
      """  Plant  """  
      self.ipStatus:str = obj["ipStatus"]
      """  StatusRequest  """  
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class StatusRequest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMaintReqTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMaintReqTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaintReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateMaintPlant_output:
   def __init__(self, obj):
      pass

