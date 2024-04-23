import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ShopLoadSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShopLoads(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShopLoads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShopLoads
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopLoadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/ShopLoads",headers=creds) as resp:
           return await resp.json()

async def post_ShopLoads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShopLoads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShopLoadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShopLoadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/ShopLoads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShopLoads_Company_ResourceGrpID_ResourceID_LoadDate(Company, ResourceGrpID, ResourceID, LoadDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShopLoad item
   Description: Calls GetByID to retrieve the ShopLoad item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShopLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param LoadDate: Desc: LoadDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShopLoadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/ShopLoads(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + LoadDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShopLoads_Company_ResourceGrpID_ResourceID_LoadDate(Company, ResourceGrpID, ResourceID, LoadDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShopLoad for the service
   Description: Calls UpdateExt to update ShopLoad. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShopLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param LoadDate: Desc: LoadDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShopLoadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/ShopLoads(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + LoadDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShopLoads_Company_ResourceGrpID_ResourceID_LoadDate(Company, ResourceGrpID, ResourceID, LoadDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShopLoad item
   Description: Call UpdateExt to delete ShopLoad item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShopLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param LoadDate: Desc: LoadDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/ShopLoads(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + LoadDate + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShopLoadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShopLoad, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseShopLoad=" + whereClauseShopLoad
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(resourceGrpID, resourceID, loadDate, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "resourceGrpID=" + resourceGrpID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "resourceID=" + resourceID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "loadDate=" + loadDate

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShopLoad(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShopLoad
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShopLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShopLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShopLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShopLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopLoadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShopLoadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShopLoadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShopLoadRow] = obj["value"]
      pass

class Erp_Tablesets_ShopLoadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.LoadDate:str = obj["LoadDate"]
      """  Date of the corresponding load hours.  """  
      self.ActualHours:int = obj["ActualHours"]
      """  Number of actual Load hours for this day (Not What If).  """  
      self.OverLoaded:bool = obj["OverLoaded"]
      """  Indicates if the workcenter "Actual Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.HoursOver:int = obj["HoursOver"]
      """  The number of hours that "Actual Load" is over capacity for this day in this workcenter.  """  
      self.PercOver:int = obj["PercOver"]
      """  Percentage that the work center is overloaded.  """  
      self.InformOverloaded:bool = obj["InformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is overloaded over it's reporting threshold.  """  
      self.WIHours:int = obj["WIHours"]
      """  Number of "What If" Load hours for this day.  """  
      self.WIOverLoaded:bool = obj["WIOverLoaded"]
      """  Indicates if the workcenter "What-If Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.WIHoursOver:int = obj["WIHoursOver"]
      """  The number of hours that "What-If Load" is over capacity for this day in this workcenter.  """  
      self.WIPercOver:int = obj["WIPercOver"]
      """  Percentage that the work center is What-If overloaded.  """  
      self.WIInformOverloaded:bool = obj["WIInformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is what-if overloaded over it's reporting threshold.  """  
      self.NonTimeCapacity:int = obj["NonTimeCapacity"]
      """  The Non-Time  Capacity used for this day.  """  
      self.WINonTimeCapacity:int = obj["WINonTimeCapacity"]
      """  The What-If Non-Time Capacity usage for this day.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Product Quantity  used for this day.  """  
      self.WIDailyProdQty:int = obj["WIDailyProdQty"]
      """  What if Daily Product Quantity  used for this day.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopLoadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.LoadDate:str = obj["LoadDate"]
      """  Date of the corresponding load hours.  """  
      self.ActualHours:int = obj["ActualHours"]
      """  Number of actual Load hours for this day (Not What If).  """  
      self.OverLoaded:bool = obj["OverLoaded"]
      """  Indicates if the workcenter "Actual Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.HoursOver:int = obj["HoursOver"]
      """  The number of hours that "Actual Load" is over capacity for this day in this workcenter.  """  
      self.PercOver:int = obj["PercOver"]
      """  Percentage that the work center is overloaded.  """  
      self.InformOverloaded:bool = obj["InformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is overloaded over it's reporting threshold.  """  
      self.WIHours:int = obj["WIHours"]
      """  Number of "What If" Load hours for this day.  """  
      self.WIOverLoaded:bool = obj["WIOverLoaded"]
      """  Indicates if the workcenter "What-If Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.WIHoursOver:int = obj["WIHoursOver"]
      """  The number of hours that "What-If Load" is over capacity for this day in this workcenter.  """  
      self.WIPercOver:int = obj["WIPercOver"]
      """  Percentage that the work center is What-If overloaded.  """  
      self.WIInformOverloaded:bool = obj["WIInformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is what-if overloaded over it's reporting threshold.  """  
      self.NonTimeCapacity:int = obj["NonTimeCapacity"]
      """  The Non-Time  Capacity used for this day.  """  
      self.WINonTimeCapacity:int = obj["WINonTimeCapacity"]
      """  The What-If Non-Time Capacity usage for this day.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Product Quantity  used for this day.  """  
      self.WIDailyProdQty:int = obj["WIDailyProdQty"]
      """  What if Daily Product Quantity  used for this day.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   resourceGrpID
   resourceID
   loadDate
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.resourceID:str = obj["resourceID"]
      self.loadDate:str = obj["loadDate"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ShopLoadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.LoadDate:str = obj["LoadDate"]
      """  Date of the corresponding load hours.  """  
      self.ActualHours:int = obj["ActualHours"]
      """  Number of actual Load hours for this day (Not What If).  """  
      self.OverLoaded:bool = obj["OverLoaded"]
      """  Indicates if the workcenter "Actual Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.HoursOver:int = obj["HoursOver"]
      """  The number of hours that "Actual Load" is over capacity for this day in this workcenter.  """  
      self.PercOver:int = obj["PercOver"]
      """  Percentage that the work center is overloaded.  """  
      self.InformOverloaded:bool = obj["InformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is overloaded over it's reporting threshold.  """  
      self.WIHours:int = obj["WIHours"]
      """  Number of "What If" Load hours for this day.  """  
      self.WIOverLoaded:bool = obj["WIOverLoaded"]
      """  Indicates if the workcenter "What-If Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.WIHoursOver:int = obj["WIHoursOver"]
      """  The number of hours that "What-If Load" is over capacity for this day in this workcenter.  """  
      self.WIPercOver:int = obj["WIPercOver"]
      """  Percentage that the work center is What-If overloaded.  """  
      self.WIInformOverloaded:bool = obj["WIInformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is what-if overloaded over it's reporting threshold.  """  
      self.NonTimeCapacity:int = obj["NonTimeCapacity"]
      """  The Non-Time  Capacity used for this day.  """  
      self.WINonTimeCapacity:int = obj["WINonTimeCapacity"]
      """  The What-If Non-Time Capacity usage for this day.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Product Quantity  used for this day.  """  
      self.WIDailyProdQty:int = obj["WIDailyProdQty"]
      """  What if Daily Product Quantity  used for this day.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopLoadListTableset:
   def __init__(self, obj):
      self.ShopLoadList:list[Erp_Tablesets_ShopLoadListRow] = obj["ShopLoadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShopLoadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.LoadDate:str = obj["LoadDate"]
      """  Date of the corresponding load hours.  """  
      self.ActualHours:int = obj["ActualHours"]
      """  Number of actual Load hours for this day (Not What If).  """  
      self.OverLoaded:bool = obj["OverLoaded"]
      """  Indicates if the workcenter "Actual Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.HoursOver:int = obj["HoursOver"]
      """  The number of hours that "Actual Load" is over capacity for this day in this workcenter.  """  
      self.PercOver:int = obj["PercOver"]
      """  Percentage that the work center is overloaded.  """  
      self.InformOverloaded:bool = obj["InformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is overloaded over it's reporting threshold.  """  
      self.WIHours:int = obj["WIHours"]
      """  Number of "What If" Load hours for this day.  """  
      self.WIOverLoaded:bool = obj["WIOverLoaded"]
      """  Indicates if the workcenter "What-If Load"  is over capacity  for this day. Updated via the JobOper write/delete triggers.  """  
      self.WIHoursOver:int = obj["WIHoursOver"]
      """  The number of hours that "What-If Load" is over capacity for this day in this workcenter.  """  
      self.WIPercOver:int = obj["WIPercOver"]
      """  Percentage that the work center is What-If overloaded.  """  
      self.WIInformOverloaded:bool = obj["WIInformOverloaded"]
      """  Flag that indicates that the work center is to be informed on and it is what-if overloaded over it's reporting threshold.  """  
      self.NonTimeCapacity:int = obj["NonTimeCapacity"]
      """  The Non-Time  Capacity used for this day.  """  
      self.WINonTimeCapacity:int = obj["WINonTimeCapacity"]
      """  The What-If Non-Time Capacity usage for this day.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Product Quantity  used for this day.  """  
      self.WIDailyProdQty:int = obj["WIDailyProdQty"]
      """  What if Daily Product Quantity  used for this day.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShopLoadTableset:
   def __init__(self, obj):
      self.ShopLoad:list[Erp_Tablesets_ShopLoadRow] = obj["ShopLoad"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtShopLoadTableset:
   def __init__(self, obj):
      self.ShopLoad:list[Erp_Tablesets_ShopLoadRow] = obj["ShopLoad"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   resourceGrpID
   resourceID
   loadDate
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.resourceID:str = obj["resourceID"]
      self.loadDate:str = obj["loadDate"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShopLoadTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopLoadTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopLoadTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShopLoadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewShopLoad_input:
   """ Required : 
   ds
   resourceGrpID
   resourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopLoadTableset] = obj["ds"]
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.resourceID:str = obj["resourceID"]
      pass

class GetNewShopLoad_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShopLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShopLoad
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShopLoad:str = obj["whereClauseShopLoad"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShopLoadTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtShopLoadTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShopLoadTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShopLoadTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShopLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

