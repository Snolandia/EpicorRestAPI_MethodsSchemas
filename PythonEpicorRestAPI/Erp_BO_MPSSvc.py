import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MPSSvc
# Description: This BO is used to maintain the Master Prodcution Schedule.
           The Master Production Schedule is store in the MasProd table.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MPS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MPS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasProdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/MPS",headers=creds) as resp:
           return await resp.json()

async def post_MPS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasProdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasProdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/MPS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MPS_Company_PartNum_Plant_DueDate_AttributeSetID_ParentPartNum(Company, PartNum, Plant, DueDate, AttributeSetID, ParentPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MP item
   Description: Calls GetByID to retrieve the MP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DueDate: Desc: DueDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasProdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/MPS(" + Company + "," + PartNum + "," + Plant + "," + DueDate + "," + AttributeSetID + "," + ParentPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MPS_Company_PartNum_Plant_DueDate_AttributeSetID_ParentPartNum(Company, PartNum, Plant, DueDate, AttributeSetID, ParentPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MP for the service
   Description: Calls UpdateExt to update MP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DueDate: Desc: DueDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasProdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/MPS(" + Company + "," + PartNum + "," + Plant + "," + DueDate + "," + AttributeSetID + "," + ParentPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MPS_Company_PartNum_Plant_DueDate_AttributeSetID_ParentPartNum(Company, PartNum, Plant, DueDate, AttributeSetID, ParentPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MP item
   Description: Call UpdateExt to delete MP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DueDate: Desc: DueDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/MPS(" + Company + "," + PartNum + "," + Plant + "," + DueDate + "," + AttributeSetID + "," + ParentPartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasProdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMasProd, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMasProd=" + whereClauseMasProd
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, plant, dueDate, attributeSetID, parentPartNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "partNum=" + partNum
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
   params += "dueDate=" + dueDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeSetID=" + attributeSetID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "parentPartNum=" + parentPartNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CopyFromForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyFromForecast
   Description: Copy the master production schedule from the forecast for the given Part/Plant
and the forecast horizon of the given date.  The forecast horizon is determined
from the company MRP configuration settings to determine a starting date.  All
forcast entries after that date will be copied to the Master Production Schedule.
   OperationID: CopyFromForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyFromForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyFromForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ForecastInHorizon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ForecastInHorizon
   Description: This will determine if a forecast entry exists for a part/plant within the forecast horizon
of a given date.  The forecast horizon starts at the given dates and looks backward the
number of days as defined in the MRP configuration.
   OperationID: ForecastInHorizon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ForecastInHorizon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ForecastInHorizon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getDate
   Description: This method will set the DueDate based on if there is a row currently in the MasProd dataset or not
   OperationID: getDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeSetIDFromRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMasProd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMasProd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasProd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasProd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasProd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MPSSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasProdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasProdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasProdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MasProdRow] = obj["value"]
      pass

class Erp_Tablesets_MasProdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this MasProd.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the master production schedule.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  Production Quantity  """  
      self.ProdQtyUOM:str = obj["ProdQtyUOM"]
      """  UOM of Production Quantity  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasProdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this MasProd.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the master production schedule.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  Production Quantity  """  
      self.ProdQtyUOM:str = obj["ProdQtyUOM"]
      """  UOM of Production Quantity  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CopyFromForecast_input:
   """ Required : 
   ipPartNum
   ipPlant
   ipDate
   ipAttributeSetID
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part number of the forecast/schedule  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The Plant of the forecast/schedule  """  
      self.ipDate:str = obj["ipDate"]
      """  The starting date of the schedule.  This is typically TODAY.  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  The Attribute Set Id  """  
      pass

class CopyFromForecast_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   partNum
   plant
   dueDate
   attributeSetID
   parentPartNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.dueDate:str = obj["dueDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MPSTableset:
   def __init__(self, obj):
      self.MasProd:list[Erp_Tablesets_MasProdRow] = obj["MasProd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MasProdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this MasProd.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the master production schedule.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  Production Quantity  """  
      self.ProdQtyUOM:str = obj["ProdQtyUOM"]
      """  UOM of Production Quantity  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MasProdListTableset:
   def __init__(self, obj):
      self.MasProdList:list[Erp_Tablesets_MasProdListRow] = obj["MasProdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MasProdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this MasProd.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the master production schedule.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  Production Quantity  """  
      self.ProdQtyUOM:str = obj["ProdQtyUOM"]
      """  UOM of Production Quantity  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtMPSTableset:
   def __init__(self, obj):
      self.MasProd:list[Erp_Tablesets_MasProdRow] = obj["MasProd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ForecastInHorizon_input:
   """ Required : 
   ipPartNum
   ipPlant
   ipDate
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part number of the forecast  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The Plant of the forecast  """  
      self.ipDate:str = obj["ipDate"]
      """  The starting date of the forecast.  This is typically TODAY.  """  
      pass

class ForecastInHorizon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opForecastExists:bool = obj["opForecastExists"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   plant
   dueDate
   attributeSetID
   parentPartNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.dueDate:str = obj["dueDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MPSTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MPSTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MPSTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MasProdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMasProd_input:
   """ Required : 
   ds
   partNum
   plant
   dueDate
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.dueDate:str = obj["dueDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetNewMasProd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMasProd
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMasProd:str = obj["whereClauseMasProd"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MPSTableset] = obj["returnObj"]
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

class PartsAttributeClassHasRevisionAndIsMRPTracked_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  current Attribute Class ID  """  
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateAttributeSetIDFromRevisionNum_input:
   """ Required : 
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  new revision selected  """  
      pass

class UpdateAttributeSetIDFromRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      self.planningAttributeSetSeq:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMPSTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMPSTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      pass

class getDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MPSTableset] = obj["ds"]
      pass

      """  output parameters  """  

