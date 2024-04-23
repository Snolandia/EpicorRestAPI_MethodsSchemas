import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbForecastSvc
# Description: Global Forecasts are the transport in the inter-company PO-SO mechanism.
In a nutshell, from the purchasing company's PO Suggestions the user can "Send Forecasts"
to the producing company;  this creates GlbForecast records in the producing company.  These
GlbForecast records can be reviewed, modified and deleted or "accepted" (turning the
GlbForecast records into Forecast records).
This BO supports these activities.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbForecasts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbForecasts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbForecasts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbForecastRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts",headers=creds) as resp:
           return await resp.json()

async def post_GlbForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company, PartNum, Plant, ForeDate, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbForecast item
   Description: Calls GetByID to retrieve the GlbForecast item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbForecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company, PartNum, Plant, ForeDate, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbForecast for the service
   Description: Calls UpdateExt to update GlbForecast. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbForecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company, PartNum, Plant, ForeDate, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbForecast item
   Description: Call UpdateExt to delete GlbForecast item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbForecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbForecastListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbForecast, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbForecast=" + whereClauseGlbForecast
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, plant, foreDate, custNum, epicorHeaders = None):
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
   params += "foreDate=" + foreDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AcceptGlbForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AcceptGlbForecasts
   Description: This method conditionally adds/overwrites Forecast records by copying the data out of
GlbForecast records.
Similar to the ImportForecasts routine, which takes in a dataset derived from a spreadsheet file.
   OperationID: AcceptGlbForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AcceptGlbForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptGlbForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearGlbForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearGlbForecasts
   Description: This method deletes all GlbForecast records for the Current Plant, or all Plants, on or after the given date.
   OperationID: ClearGlbForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearGlbForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearGlbForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsConfigurable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsConfigurable
   Description: Returns `true` If any revision, or any revision of any child part in BOM, is/was configurable.
   OperationID: IsConfigurable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsConfigurable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsConfigurable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbForecast
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbForecastListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbForecastRow] = obj["value"]
      pass

class Erp_Tablesets_GlbForecastListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      self.ForeQty:int = obj["ForeQty"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.TransDate:str = obj["TransDate"]
      self.AutoTransfer:bool = obj["AutoTransfer"]
      self.TransTime:int = obj["TransTime"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the forecast was transfered to the local forecast table  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandReference:str = obj["DemandReference"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.EndDate:str = obj["EndDate"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.KitFlag:str = obj["KitFlag"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReadyFlag:bool = obj["ReadyFlag"]
      self.InvalidData:bool = obj["InvalidData"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.CustId:str = obj["CustId"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartDescription from the Part table.  """  
      self.PartPlantMinimumQty:int = obj["PartPlantMinimumQty"]
      """  MinimumQty from the PartPlant table  """  
      self.PartPlantMaximumQty:int = obj["PartPlantMaximumQty"]
      """  MaximumQty from the PartPlant table.  """  
      self.PartPlantSafetyQty:int = obj["PartPlantSafetyQty"]
      """  SafetyQty from the PartPlant table.  """  
      self.PartPlantMinOrderQty:int = obj["PartPlantMinOrderQty"]
      """  MinOrderQty from the PartPlant table.  """  
      self.PartPlantOnHandQty:int = obj["PartPlantOnHandQty"]
      """  OnHandQty from the PartPlant table.  """  
      self.PartPlantLeadTime:int = obj["PartPlantLeadTime"]
      """  LeadTime from the PartPlant table.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Name field from the Customer table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbForecastRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      self.ForeQty:int = obj["ForeQty"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.TransDate:str = obj["TransDate"]
      self.AutoTransfer:bool = obj["AutoTransfer"]
      self.TransTime:int = obj["TransTime"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the forecast was transfered to the local forecast table  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandReference:str = obj["DemandReference"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.EndDate:str = obj["EndDate"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.KitFlag:str = obj["KitFlag"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.CustId:str = obj["CustId"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Name field from the Customer table.  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.InvalidData:bool = obj["InvalidData"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartDescription from the Part table.  """  
      self.PartPlantLeadTime:int = obj["PartPlantLeadTime"]
      """  LeadTime from the PartPlant table.  """  
      self.PartPlantMaximumQty:int = obj["PartPlantMaximumQty"]
      """  MaximumQty from the PartPlant table.  """  
      self.PartPlantMinimumQty:int = obj["PartPlantMinimumQty"]
      """  MinimumQty from the PartPlant table  """  
      self.PartPlantMinOrderQty:int = obj["PartPlantMinOrderQty"]
      """  MinOrderQty from the PartPlant table.  """  
      self.PartPlantOnHandQty:int = obj["PartPlantOnHandQty"]
      """  OnHandQty from the PartPlant table.  """  
      self.PartPlantSafetyQty:int = obj["PartPlantSafetyQty"]
      """  SafetyQty from the PartPlant table.  """  
      self.ReadyFlag:bool = obj["ReadyFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AcceptGlbForecasts_input:
   """ Required : 
   ds
   pcImportOptions
   plAllPlants
   pdFromDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      self.pcImportOptions:str = obj["pcImportOptions"]
      """  Valid choices are "A"=Add+Replace, "C"=Clear+Reload, "N"=New.  """  
      self.plAllPlants:bool = obj["plAllPlants"]
      """  If TRUE, clear all plants; if FALSE, clear Current Plant.  """  
      self.pdFromDate:str = obj["pdFromDate"]
      """  Only records on or after the given date will be considered for import.  """  
      pass

class AcceptGlbForecasts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ClearGlbForecasts_input:
   """ Required : 
   plAllPlants
   pdFromDate
   """  
   def __init__(self, obj):
      self.plAllPlants:bool = obj["plAllPlants"]
      """  If TRUE, clear all plants; if FALSE, clear Current Plant.  """  
      self.pdFromDate:str = obj["pdFromDate"]
      """  Only GlbForecast records on or after the given date will be deleted.  """  
      pass

class ClearGlbForecasts_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   partNum
   plant
   foreDate
   custNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.foreDate:str = obj["foreDate"]
      self.custNum:int = obj["custNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbForecastListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      self.ForeQty:int = obj["ForeQty"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.TransDate:str = obj["TransDate"]
      self.AutoTransfer:bool = obj["AutoTransfer"]
      self.TransTime:int = obj["TransTime"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the forecast was transfered to the local forecast table  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandReference:str = obj["DemandReference"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.EndDate:str = obj["EndDate"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.KitFlag:str = obj["KitFlag"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReadyFlag:bool = obj["ReadyFlag"]
      self.InvalidData:bool = obj["InvalidData"]
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.CustId:str = obj["CustId"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartDescription from the Part table.  """  
      self.PartPlantMinimumQty:int = obj["PartPlantMinimumQty"]
      """  MinimumQty from the PartPlant table  """  
      self.PartPlantMaximumQty:int = obj["PartPlantMaximumQty"]
      """  MaximumQty from the PartPlant table.  """  
      self.PartPlantSafetyQty:int = obj["PartPlantSafetyQty"]
      """  SafetyQty from the PartPlant table.  """  
      self.PartPlantMinOrderQty:int = obj["PartPlantMinOrderQty"]
      """  MinOrderQty from the PartPlant table.  """  
      self.PartPlantOnHandQty:int = obj["PartPlantOnHandQty"]
      """  OnHandQty from the PartPlant table.  """  
      self.PartPlantLeadTime:int = obj["PartPlantLeadTime"]
      """  LeadTime from the PartPlant table.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Name field from the Customer table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbForecastListTableset:
   def __init__(self, obj):
      self.GlbForecastList:list[Erp_Tablesets_GlbForecastListRow] = obj["GlbForecastList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbForecastRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      self.ForeQty:int = obj["ForeQty"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.TransDate:str = obj["TransDate"]
      self.AutoTransfer:bool = obj["AutoTransfer"]
      self.TransTime:int = obj["TransTime"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the forecast was transfered to the local forecast table  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DemandReference:str = obj["DemandReference"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.EndDate:str = obj["EndDate"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.KitFlag:str = obj["KitFlag"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.CustId:str = obj["CustId"]
      """  A user defined external customer ID.  This must be unique within the file.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Name field from the Customer table.  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      self.InvalidData:bool = obj["InvalidData"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  PartDescription from the Part table.  """  
      self.PartPlantLeadTime:int = obj["PartPlantLeadTime"]
      """  LeadTime from the PartPlant table.  """  
      self.PartPlantMaximumQty:int = obj["PartPlantMaximumQty"]
      """  MaximumQty from the PartPlant table.  """  
      self.PartPlantMinimumQty:int = obj["PartPlantMinimumQty"]
      """  MinimumQty from the PartPlant table  """  
      self.PartPlantMinOrderQty:int = obj["PartPlantMinOrderQty"]
      """  MinOrderQty from the PartPlant table.  """  
      self.PartPlantOnHandQty:int = obj["PartPlantOnHandQty"]
      """  OnHandQty from the PartPlant table.  """  
      self.PartPlantSafetyQty:int = obj["PartPlantSafetyQty"]
      """  SafetyQty from the PartPlant table.  """  
      self.ReadyFlag:bool = obj["ReadyFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbForecastTableset:
   def __init__(self, obj):
      self.GlbForecast:list[Erp_Tablesets_GlbForecastRow] = obj["GlbForecast"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbForecastTableset:
   def __init__(self, obj):
      self.GlbForecast:list[Erp_Tablesets_GlbForecastRow] = obj["GlbForecast"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   plant
   foreDate
   custNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.foreDate:str = obj["foreDate"]
      self.custNum:int = obj["custNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbForecastTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbForecastTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbForecastTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbForecastListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbForecast_input:
   """ Required : 
   ds
   partNum
   plant
   foreDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.foreDate:str = obj["foreDate"]
      pass

class GetNewGlbForecast_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbForecast
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbForecast:str = obj["whereClauseGlbForecast"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbForecastTableset] = obj["returnObj"]
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

class IsConfigurable_input:
   """ Required : 
   pcPartNum
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      pass

class IsConfigurable_output:
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
      self.ds:list[Erp_Tablesets_UpdExtGlbForecastTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbForecastTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

