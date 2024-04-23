import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartPlantSearchSvc
# Description: Part Plant Search object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartPlantSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartPlantSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartPlantSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches",headers=creds) as resp:
           return await resp.json()

async def post_PartPlantSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartPlantSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartPlantSearches_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartPlantSearch item
   Description: Calls GetByID to retrieve the PartPlantSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartPlantSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartPlantSearches_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartPlantSearch for the service
   Description: Calls UpdateExt to update PartPlantSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartPlantSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartPlantSearches_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartPlantSearch item
   Description: Call UpdateExt to delete PartPlantSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartPlantSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/PartPlantSearches(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartPlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartPlant, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartPlant=" + whereClausePartPlant
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, plant, epicorHeaders = None):
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "plant=" + plant

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetActiveParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActiveParts
   Description: Calls the standard GetRows and filters the Inactive parts
   OperationID: GetActiveParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActiveParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartPlantPlanningParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartPlantPlanningParameters
   Description: Returns either base PartPlant data or attribute PartPlantPlanningAttribute data, depending if attributeSetID is supplied.
   OperationID: GetPartPlantPlanningParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartPlantPlanningParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartPlantPlanningParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartPlantSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartPlantListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartPlantRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartPlantRow] = obj["value"]
      pass

class Erp_Tablesets_PartPlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.PrimWhse:str = obj["PrimWhse"]
      """  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.MinOrderQty:int = obj["MinOrderQty"]
      """  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      """  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      """  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.MfgLotMultiple:int = obj["MfgLotMultiple"]
      """  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  """  
      self.DaysOfSupply:int = obj["DaysOfSupply"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ReOrderLevel:bool = obj["ReOrderLevel"]
      """  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  """  
      self.MRPRecalcNeeded:bool = obj["MRPRecalcNeeded"]
      """  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  """  
      self.ProcessMRP:bool = obj["ProcessMRP"]
      """  Flag indicating if MRP should process this part.  """  
      self.GenerateSugg:bool = obj["GenerateSugg"]
      """  Flag indicating if PO suggestion should be generated for this part.  """  
      self.GetFromLocalWhse:bool = obj["GetFromLocalWhse"]
      """  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  """  
      self.ForecastTime:int = obj["ForecastTime"]
      """  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  """  
      self.TransferPlant:str = obj["TransferPlant"]
      """  Default Site that part is transfered from when it is obtained via Site transfer.  """  
      self.SourceType:str = obj["SourceType"]
      """   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  """  
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      """  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Used to determine the start date  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Days needed to move part to stock or next job.  Deducted from Due Date.  """  
      self.PlanTimeFence:int = obj["PlanTimeFence"]
      """  Days out from the current date when dates on jobs, PO, TO cannot be changed  """  
      self.ReschedOutDelta:int = obj["ReschedOutDelta"]
      """  MRP parameter not to reschedule if number of days change below  """  
      self.ReschedInDelta:int = obj["ReschedInDelta"]
      """  Same as ReschedOutDelta but for messages  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this Part/Site  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  """  
      self.KitAllowChangeParms:bool = obj["KitAllowChangeParms"]
      """  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent item is shipped.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.ShortHorizonDays:int = obj["ShortHorizonDays"]
      """  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  """  
      self.ShortHorizonMinMfgLotSize:int = obj["ShortHorizonMinMfgLotSize"]
      """  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.ShortHorizonMaxMfgLotSize:int = obj["ShortHorizonMaxMfgLotSize"]
      """  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.LimitProdYldRecalc:bool = obj["LimitProdYldRecalc"]
      """  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ShortHorizonDaysSupp:int = obj["ShortHorizonDaysSupp"]
      """  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  """  
      self.DemandQty:int = obj["DemandQty"]
      """  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.NeverReuseMRPJob:bool = obj["NeverReuseMRPJob"]
      """  System flag future use  """  
      self.DeleteMRPJobs:bool = obj["DeleteMRPJobs"]
      """  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  """  
      self.TotMfgLeadTimeSys:int = obj["TotMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  """  
      self.TotMfgLeadTimeMnl:int = obj["TotMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  """  
      self.LvlMfgLeadTimeSys:int = obj["LvlMfgLeadTimeSys"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  """  
      self.LvlMfgLeadTimeMnl:int = obj["LvlMfgLeadTimeMnl"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  """  
      self.MfgLeadTimeCalcDate:str = obj["MfgLeadTimeCalcDate"]
      """  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  """  
      self.MfgLeadTimeMnlDate:str = obj["MfgLeadTimeMnlDate"]
      """  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  """  
      self.AutoConsumeStock:bool = obj["AutoConsumeStock"]
      """  Auto consume available stock when MRP runs and creates a job.  """  
      self.StartMinLotQty:bool = obj["StartMinLotQty"]
      """  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  """  
      self.MinLotLeadTime:int = obj["MinLotLeadTime"]
      """  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  """  
      self.MfgLeadTimeMnl:bool = obj["MfgLeadTimeMnl"]
      """  Indicates manufacturing lead times are entered manually by the user.  """  
      self.MfgLeadTimeEnteredBy:str = obj["MfgLeadTimeEnteredBy"]
      """  Userid of user who entered manual manufacturing lead times.  """  
      self.MinStartQty:int = obj["MinStartQty"]
      """  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  """  
      self.RawMaterial:bool = obj["RawMaterial"]
      """  Raw Material  """  
      self.MultiLevelCTP:bool = obj["MultiLevelCTP"]
      """  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.ConsumeSafety:bool = obj["ConsumeSafety"]
      """  Indicates if MRP should allow consumption of safety stock within the purchase lead time  """  
      self.SLTVendorNum:int = obj["SLTVendorNum"]
      """  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  """  
      self.SLTPurPoint:str = obj["SLTPurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.ShortLeadTime:int = obj["ShortLeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  """  
      self.ICTrader:bool = obj["ICTrader"]
      self.InActive:bool = obj["InActive"]
      self.DisableQtyBrng:bool = obj["DisableQtyBrng"]
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Used to indicate if the Serial Number format button should be enabled.  """  
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      """  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  """  
      self.SNNumODigits:int = obj["SNNumODigits"]
      """  Used to designate the number of digits for an Integer or Mask type serial number format.  """  
      self.PlantConfCtrlSerialTracking:int = obj["PlantConfCtrlSerialTracking"]
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base UOM Code from Part Master  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PersonName:str = obj["PersonName"]
      """   Name of person.

Purchasing: This is printed on the PO by the authorized signature 
line.
Alerts: Used as email address for recipients not defined on global alert  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.PrimWhseDescription:str = obj["PrimWhseDescription"]
      """  Description.  """  
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type. 
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.TransferPlantName:str = obj["TransferPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.PrimWhse:str = obj["PrimWhse"]
      """  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.MinOrderQty:int = obj["MinOrderQty"]
      """  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      """  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      """  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.MfgLotMultiple:int = obj["MfgLotMultiple"]
      """  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  """  
      self.DaysOfSupply:int = obj["DaysOfSupply"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ReOrderLevel:bool = obj["ReOrderLevel"]
      """  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  """  
      self.MRPRecalcNeeded:bool = obj["MRPRecalcNeeded"]
      """  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  """  
      self.ProcessMRP:bool = obj["ProcessMRP"]
      """  Flag indicating if MRP should process this part.  """  
      self.GenerateSugg:bool = obj["GenerateSugg"]
      """  Flag indicating if PO suggestion should be generated for this part.  """  
      self.GetFromLocalWhse:bool = obj["GetFromLocalWhse"]
      """  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  """  
      self.ForecastTime:int = obj["ForecastTime"]
      """  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  """  
      self.TransferPlant:str = obj["TransferPlant"]
      """  Default Site that part is transfered from when it is obtained via Site transfer.  """  
      self.SourceType:str = obj["SourceType"]
      """   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  """  
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      """  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Used to determine the start date  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Days needed to move part to stock or next job.  Deducted from Due Date.  """  
      self.PlanTimeFence:int = obj["PlanTimeFence"]
      """  Days out from the current date when dates on jobs, PO, TO cannot be changed  """  
      self.ReschedOutDelta:int = obj["ReschedOutDelta"]
      """  MRP parameter not to reschedule if number of days change below  """  
      self.ReschedInDelta:int = obj["ReschedInDelta"]
      """  Same as ReschedOutDelta but for messages  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this Part/Site  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  """  
      self.KitAllowChangeParms:bool = obj["KitAllowChangeParms"]
      """  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent item is shipped.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.ShortHorizonDays:int = obj["ShortHorizonDays"]
      """  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  """  
      self.ShortHorizonMinMfgLotSize:int = obj["ShortHorizonMinMfgLotSize"]
      """  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.ShortHorizonMaxMfgLotSize:int = obj["ShortHorizonMaxMfgLotSize"]
      """  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.LimitProdYldRecalc:bool = obj["LimitProdYldRecalc"]
      """  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ShortHorizonDaysSupp:int = obj["ShortHorizonDaysSupp"]
      """  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  """  
      self.DemandQty:int = obj["DemandQty"]
      """  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.NeverReuseMRPJob:bool = obj["NeverReuseMRPJob"]
      """  System flag future use  """  
      self.DeleteMRPJobs:bool = obj["DeleteMRPJobs"]
      """  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  """  
      self.TotMfgLeadTimeSys:int = obj["TotMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  """  
      self.TotMfgLeadTimeMnl:int = obj["TotMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  """  
      self.LvlMfgLeadTimeSys:int = obj["LvlMfgLeadTimeSys"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  """  
      self.LvlMfgLeadTimeMnl:int = obj["LvlMfgLeadTimeMnl"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  """  
      self.MfgLeadTimeCalcDate:str = obj["MfgLeadTimeCalcDate"]
      """  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  """  
      self.MfgLeadTimeMnlDate:str = obj["MfgLeadTimeMnlDate"]
      """  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  """  
      self.AutoConsumeStock:bool = obj["AutoConsumeStock"]
      """  Auto consume available stock when MRP runs and creates a job.  """  
      self.StartMinLotQty:bool = obj["StartMinLotQty"]
      """  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  """  
      self.MinLotLeadTime:int = obj["MinLotLeadTime"]
      """  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  """  
      self.MfgLeadTimeMnl:bool = obj["MfgLeadTimeMnl"]
      """  Indicates manufacturing lead times are entered manually by the user.  """  
      self.MfgLeadTimeEnteredBy:str = obj["MfgLeadTimeEnteredBy"]
      """  Userid of user who entered manual manufacturing lead times.  """  
      self.MinStartQty:int = obj["MinStartQty"]
      """  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  """  
      self.RawMaterial:bool = obj["RawMaterial"]
      """  Raw Material  """  
      self.MultiLevelCTP:bool = obj["MultiLevelCTP"]
      """  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.ConsumeSafety:bool = obj["ConsumeSafety"]
      """  Indicates if MRP should allow consumption of safety stock within the purchase lead time  """  
      self.SLTVendorNum:int = obj["SLTVendorNum"]
      """  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  """  
      self.SLTPurPoint:str = obj["SLTPurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.ShortLeadTime:int = obj["ShortLeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentLeadTime:int = obj["UrgentLeadTime"]
      """  This is the lead time used when generating a new suggestion within the lead time window.  If this field is 0 and the Supplier is determined from the Supplier Price List, the suggestion will use the lead time from the price list.  """  
      self.UrgentMinOrdQty:int = obj["UrgentMinOrdQty"]
      """  This is the minimum qty required when generating a new suggestion within the lead time window.  """  
      self.UrgentMultQty:int = obj["UrgentMultQty"]
      """  This is used to calculate the suggestion qty to the nearest multiple when generating a new suggestion within the lead time window.  """  
      self.UrgentPurPoint:str = obj["UrgentPurPoint"]
      """  See UrgentVendorNum  """  
      self.UrgentVendorNum:int = obj["UrgentVendorNum"]
      """  If this field is not populated then the system will use the standard Supplier from PartPlant, or the last Supplier the part was purchased from, or the Supplier from the first Price list found for the part.  """  
      self.PartRunMRP:bool = obj["PartRunMRP"]
      """  PartRunMRP  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.MMSExclude:bool = obj["MMSExclude"]
      """  Indicates if this part will be excluded in the Inventory Min/Max/Safety calculation.  """  
      self.MMSSales:bool = obj["MMSSales"]
      """  Indicates if sales history for this part will be included in the Inventory Min/Max/Safety calculation.  """  
      self.MMSIssue:bool = obj["MMSIssue"]
      """  Indicates if job materials history for this part will be included in the Inventory Min/Max/Safety calculation.  """  
      self.MMSHistory:int = obj["MMSHistory"]
      """  User defined number in days, of how far back to look in usage history.  """  
      self.MMSSafetyFactor:int = obj["MMSSafetyFactor"]
      """  User defined, percentage of MIN to be set as Safety stock value.  """  
      self.MMSMaxFactor:int = obj["MMSMaxFactor"]
      """  User defined, used in calculation to defined MAX stock value.  """  
      self.SavedMinimumQty:int = obj["SavedMinimumQty"]
      """  WIll hold the proposed Min when the Min/Max/Safety process is ran  """  
      self.SavedMaximumQty:int = obj["SavedMaximumQty"]
      """  WIll hold the proposed Max when the Min/Max/Safety process is ran  """  
      self.SavedSafetyQty:int = obj["SavedSafetyQty"]
      """  WIll hold the proposed Safety when the Min/Max/Safety process is ran  """  
      self.SavedCalculatedUsageQty:int = obj["SavedCalculatedUsageQty"]
      """  It will hold the last TotalUsage used for the Saved Min/Max/Safety  """  
      self.SavedOnDateTime:str = obj["SavedOnDateTime"]
      """  Last Date when the Saved Min/Max/Safety were updated  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.ACWDays:int = obj["ACWDays"]
      """  Auto consume window days, this is the number of days that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.GenNewPCIDDelaySeconds:int = obj["GenNewPCIDDelaySeconds"]
      """  GenNewPCIDDelaySeconds  """  
      self.GenNewPCIDLimitDays:int = obj["GenNewPCIDLimitDays"]
      """  GenNewPCIDLimitDays  """  
      self.TopLvlMfgLeadTimeSys:int = obj["TopLvlMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only.  Does not include the time on lower level parts.  Not editable by the user.  """  
      self.TopLvlMfgLeadTimeMnl:int = obj["TopLvlMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only. Does not include the time on lower level parts. Directly maintained by the user.  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.IncludedIntoAllocationBase:bool = obj["IncludedIntoAllocationBase"]
      """  Included Into Allocation Base  """  
      self.ForecastDaysBefore:int = obj["ForecastDaysBefore"]
      """  Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce forecast.  """  
      self.ForecastDaysAfter:int = obj["ForecastDaysAfter"]
      """  Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days after of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base UOM Code from Part Master  """  
      self.CalculatedLeadTime:int = obj["CalculatedLeadTime"]
      """  Used to calculate the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ExtLeadTime:int = obj["ExtLeadTime"]
      self.SNNumODigits:int = obj["SNNumODigits"]
      """  Used to designate the number of digits for an Integer or Mask type serial number format.  """  
      self.UrgentVendorName:str = obj["UrgentVendorName"]
      self.UrgentVendorVendorID:str = obj["UrgentVendorVendorID"]
      self.DisableQtyBrng:bool = obj["DisableQtyBrng"]
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Used to indicate if the Serial Number format button should be enabled.  """  
      self.ICTrader:bool = obj["ICTrader"]
      self.InActive:bool = obj["InActive"]
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  """  
      self.PlantConfCtrlSerialTracking:int = obj["PlantConfCtrlSerialTracking"]
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      """  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  """  
      self.HasOnHandQty:bool = obj["HasOnHandQty"]
      """  Indicates if there is any quantity on hand for this part  """  
      self.IsActCostingAllocEnabled:bool = obj["IsActCostingAllocEnabled"]
      self.MaximumQtyNofP:int = obj["MaximumQtyNofP"]
      """  Number of Pieces for MaximumQty  """  
      self.MaxMfgLotSizeNofP:int = obj["MaxMfgLotSizeNofP"]
      """  Number of Pieces for MaxMfgLotSize  """  
      self.MfgLotMultipleNofP:int = obj["MfgLotMultipleNofP"]
      """  Number of Pieces for MfgLotMultiple  """  
      self.MinimumQtyNofP:int = obj["MinimumQtyNofP"]
      """  Number of Pieces for MinimumQty  """  
      self.MinMfgLotSizeNofP:int = obj["MinMfgLotSizeNofP"]
      """  Number of Pieces for MinMfgLotSize  """  
      self.MinOrderQtyNofP:int = obj["MinOrderQtyNofP"]
      """  Number of Pieces for MinOrderQty  """  
      self.MinStartQtyNofP:int = obj["MinStartQtyNofP"]
      """  Number of Pieces for MinStartQty  """  
      self.QtyDisplayOption:str = obj["QtyDisplayOption"]
      self.SafetyQtyNofP:int = obj["SafetyQtyNofP"]
      """  Number of Pieces for SafetyQty  """  
      self.ShortHorizonMaxMfgLotSizeNofP:int = obj["ShortHorizonMaxMfgLotSizeNofP"]
      """  Number of Pieces for ShortHorizonMaxMfgLotSize  """  
      self.ShortHorizonMinMfgLotSizeNofP:int = obj["ShortHorizonMinMfgLotSizeNofP"]
      """  Number of Pieces for ShortHorizonMinMfgLotSize  """  
      self.UrgentMinOrdQtyNofP:int = obj["UrgentMinOrdQtyNofP"]
      """  Number of Pieces for UrgentMinOrdQty  """  
      self.UrgentMultQtyNofP:int = obj["UrgentMultQtyNofP"]
      """  Number of Pieces for UrgentMultQty  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PersonName:str = obj["PersonName"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseDescription:str = obj["PrimWhseDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.TransferPlantName:str = obj["TransferPlantName"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartPlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.PrimWhse:str = obj["PrimWhse"]
      """  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.MinOrderQty:int = obj["MinOrderQty"]
      """  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      """  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      """  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.MfgLotMultiple:int = obj["MfgLotMultiple"]
      """  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  """  
      self.DaysOfSupply:int = obj["DaysOfSupply"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ReOrderLevel:bool = obj["ReOrderLevel"]
      """  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  """  
      self.MRPRecalcNeeded:bool = obj["MRPRecalcNeeded"]
      """  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  """  
      self.ProcessMRP:bool = obj["ProcessMRP"]
      """  Flag indicating if MRP should process this part.  """  
      self.GenerateSugg:bool = obj["GenerateSugg"]
      """  Flag indicating if PO suggestion should be generated for this part.  """  
      self.GetFromLocalWhse:bool = obj["GetFromLocalWhse"]
      """  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  """  
      self.ForecastTime:int = obj["ForecastTime"]
      """  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  """  
      self.TransferPlant:str = obj["TransferPlant"]
      """  Default Site that part is transfered from when it is obtained via Site transfer.  """  
      self.SourceType:str = obj["SourceType"]
      """   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  """  
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      """  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Used to determine the start date  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Days needed to move part to stock or next job.  Deducted from Due Date.  """  
      self.PlanTimeFence:int = obj["PlanTimeFence"]
      """  Days out from the current date when dates on jobs, PO, TO cannot be changed  """  
      self.ReschedOutDelta:int = obj["ReschedOutDelta"]
      """  MRP parameter not to reschedule if number of days change below  """  
      self.ReschedInDelta:int = obj["ReschedInDelta"]
      """  Same as ReschedOutDelta but for messages  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this Part/Site  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  """  
      self.KitAllowChangeParms:bool = obj["KitAllowChangeParms"]
      """  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent item is shipped.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.ShortHorizonDays:int = obj["ShortHorizonDays"]
      """  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  """  
      self.ShortHorizonMinMfgLotSize:int = obj["ShortHorizonMinMfgLotSize"]
      """  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.ShortHorizonMaxMfgLotSize:int = obj["ShortHorizonMaxMfgLotSize"]
      """  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.LimitProdYldRecalc:bool = obj["LimitProdYldRecalc"]
      """  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ShortHorizonDaysSupp:int = obj["ShortHorizonDaysSupp"]
      """  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  """  
      self.DemandQty:int = obj["DemandQty"]
      """  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.NeverReuseMRPJob:bool = obj["NeverReuseMRPJob"]
      """  System flag future use  """  
      self.DeleteMRPJobs:bool = obj["DeleteMRPJobs"]
      """  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  """  
      self.TotMfgLeadTimeSys:int = obj["TotMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  """  
      self.TotMfgLeadTimeMnl:int = obj["TotMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  """  
      self.LvlMfgLeadTimeSys:int = obj["LvlMfgLeadTimeSys"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  """  
      self.LvlMfgLeadTimeMnl:int = obj["LvlMfgLeadTimeMnl"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  """  
      self.MfgLeadTimeCalcDate:str = obj["MfgLeadTimeCalcDate"]
      """  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  """  
      self.MfgLeadTimeMnlDate:str = obj["MfgLeadTimeMnlDate"]
      """  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  """  
      self.AutoConsumeStock:bool = obj["AutoConsumeStock"]
      """  Auto consume available stock when MRP runs and creates a job.  """  
      self.StartMinLotQty:bool = obj["StartMinLotQty"]
      """  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  """  
      self.MinLotLeadTime:int = obj["MinLotLeadTime"]
      """  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  """  
      self.MfgLeadTimeMnl:bool = obj["MfgLeadTimeMnl"]
      """  Indicates manufacturing lead times are entered manually by the user.  """  
      self.MfgLeadTimeEnteredBy:str = obj["MfgLeadTimeEnteredBy"]
      """  Userid of user who entered manual manufacturing lead times.  """  
      self.MinStartQty:int = obj["MinStartQty"]
      """  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  """  
      self.RawMaterial:bool = obj["RawMaterial"]
      """  Raw Material  """  
      self.MultiLevelCTP:bool = obj["MultiLevelCTP"]
      """  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.ConsumeSafety:bool = obj["ConsumeSafety"]
      """  Indicates if MRP should allow consumption of safety stock within the purchase lead time  """  
      self.SLTVendorNum:int = obj["SLTVendorNum"]
      """  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  """  
      self.SLTPurPoint:str = obj["SLTPurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.ShortLeadTime:int = obj["ShortLeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  """  
      self.ICTrader:bool = obj["ICTrader"]
      self.InActive:bool = obj["InActive"]
      self.DisableQtyBrng:bool = obj["DisableQtyBrng"]
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Used to indicate if the Serial Number format button should be enabled.  """  
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      """  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  """  
      self.SNNumODigits:int = obj["SNNumODigits"]
      """  Used to designate the number of digits for an Integer or Mask type serial number format.  """  
      self.PlantConfCtrlSerialTracking:int = obj["PlantConfCtrlSerialTracking"]
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base UOM Code from Part Master  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PersonName:str = obj["PersonName"]
      """   Name of person.

Purchasing: This is printed on the PO by the authorized signature 
line.
Alerts: Used as email address for recipients not defined on global alert  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.PrimWhseDescription:str = obj["PrimWhseDescription"]
      """  Description.  """  
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type. 
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.TransferPlantName:str = obj["TransferPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartPlantListTableset:
   def __init__(self, obj):
      self.PartPlantList:list[Erp_Tablesets_PartPlantListRow] = obj["PartPlantList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.PrimWhse:str = obj["PrimWhse"]
      """  Defines which warehouse is to be used as the Primary Warehouse for this part in this Site. A primary warehouse is the one that this part is most commonly found in.  This warehouse is used as the default in many programs, such as entry of sales order line  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.MinOrderQty:int = obj["MinOrderQty"]
      """  Used to establish a suggested Order Qty when purchasing this Part for this Site. This value will be shown on the time phase report.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Number of Vendor master that this part is normally purchased from. The Purchase Order Management module uses it.  used in suggested vendor analysis.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this part should be backflushed for this Site. Backflushing is the process of automatically issuing the material to jobs based on the operation quantity completed.  When completed and scrap quantities are reported to a job operation (via labo  """  
      self.MfgLotSize:int = obj["MfgLotSize"]
      """  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  """  
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      """  This is the minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      """  This is the maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.MfgLotMultiple:int = obj["MfgLotMultiple"]
      """  This is the manufacturing lot size multiple.  MRP will create jobs in multiples of this field.  Any excess amount will be sent to stock.  Zero is no lot multiple (lot-for-lot).  Example:  Required Quantity = 500, Lot Multiple = 150, Lot Maximum = 450, 2 jobs will be created with production quantities of 450, and 150.  """  
      self.DaysOfSupply:int = obj["DaysOfSupply"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ReOrderLevel:bool = obj["ReOrderLevel"]
      """  This is the flag indicating the inventory level we need to bring up to when it falls below re-order point(safety + minimum). Valid values are MAX and MIN.  """  
      self.MRPRecalcNeeded:bool = obj["MRPRecalcNeeded"]
      """  System maintained field.  Indicates that MRP needs to be recalculated for this part/Site.  """  
      self.ProcessMRP:bool = obj["ProcessMRP"]
      """  Flag indicating if MRP should process this part.  """  
      self.GenerateSugg:bool = obj["GenerateSugg"]
      """  Flag indicating if PO suggestion should be generated for this part.  """  
      self.GetFromLocalWhse:bool = obj["GetFromLocalWhse"]
      """  This flag controls if a supply is always created in this Site for a part. If it is no then the default Site that provides a supply is from a part's product group unless the Site from product group is blank, in that case the default Site should be from the  """  
      self.ForecastTime:int = obj["ForecastTime"]
      """  Number of days forward to capture SugPODtl records for transfer as Forecast records.  Only for Intercompany trading partners  """  
      self.TransferPlant:str = obj["TransferPlant"]
      """  Default Site that part is transfered from when it is obtained via Site transfer.  """  
      self.SourceType:str = obj["SourceType"]
      """   Indicates the normal source for this part in the Site.
Values are; K = Sales Kit,M = Manufactured,P = Purchased,T = Transferred.B = Planning BOM. 
Initial default is base on Part.TypeCode.  """  
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      """  Used to record the normal order lead time for a Part from the transfer Site to this Site. This value is represented in days. It is optional.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Used to determine the start date  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Days needed to move part to stock or next job.  Deducted from Due Date.  """  
      self.PlanTimeFence:int = obj["PlanTimeFence"]
      """  Days out from the current date when dates on jobs, PO, TO cannot be changed  """  
      self.ReschedOutDelta:int = obj["ReschedOutDelta"]
      """  MRP parameter not to reschedule if number of days change below  """  
      self.ReschedInDelta:int = obj["ReschedInDelta"]
      """  Same as ReschedOutDelta but for messages  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the part class. Used as the default in the Automated Purchasing process.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the default Production Planner. This person is responsible for handling  the manufacturing suggestions of parts in this Product Group.
Used as the default for "new" manufacturing suggestions and on Job Header. Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this Part/Site  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if kit component lines can be added, deleted and modified during Sales Order and Quote entry.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kit part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  If this field is set to "No", then KitPricing must be set to "P" .  """  
      self.KitAllowChangeParms:bool = obj["KitAllowChangeParms"]
      """  Indicates if changes the kit parameters is allowed during Sales Order and Quote entry.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushed when a kit parent item is shipped.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Kit Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  """  
      self.ShortHorizonDays:int = obj["ShortHorizonDays"]
      """  Number of days out that the ShortHorizonMinMfgLotSize and ShortHorizonMaxMfgLotSize will be used instead of MinLotSize and MaxLotSize.  """  
      self.ShortHorizonMinMfgLotSize:int = obj["ShortHorizonMinMfgLotSize"]
      """  This is the Short Horizon minimum manufacturing lot size.  If the required quantity is less than this amount then MRP will create a job with this production quantity.  The excess amount will be sent to stock.  Zero is no minimum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  """  
      self.ShortHorizonMaxMfgLotSize:int = obj["ShortHorizonMaxMfgLotSize"]
      """  This is the Short Horizon maximum manufacturing lot size.  If the required quantity is greater than this amount then MRP will create additional job(s) to satisfy the required production quantity.  Zero is no maximum.  If nonzero, this field must be an even multiple of the MfgLotMultiple field.  Example:  Required Quantity = 500, Maximum Lot Size = 150, 4 jobs will be created with production quantities of 150, 150, 150, and 50.  """  
      self.LimitProdYldRecalc:bool = obj["LimitProdYldRecalc"]
      """  If set = true and the production yield is being recalculated for an assembly or any of its subassemblies, then the recalculation and quantity adjustments will stop at the assembly level and reduce the overrun quantity and if necessary adjust the PullQty rather than rolling up to its parent  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Sets the default for Part.QtyBearing. The Part.QtyBearing fields works in conjunction with the Part.Non-Stock field to enable the part master parts to be setup for expense items.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ShortHorizonDaysSupp:int = obj["ShortHorizonDaysSupp"]
      """  Used to record the short horizon order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a percentage difference between the count quantity and the frozen quantity by more than the percent tolerance figure is considered out of tolerance. Calculated as ?adjustment qty / frozen qty? expressed as a percent.  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this part/Site and the value in PcntTolerance will be used to determine if the count variance is within tol  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this part/Site and the value in QtyTolerance will be used to determine if the count variance is within t  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this part/Site and the value in ValueTolerance will be used to determine if the count variance is within toleranc  """  
      self.QtyAdjTolerance:int = obj["QtyAdjTolerance"]
      """  Used to provide a means to control whether a count quantity discrepancy should be posted as an adjustment to inventory. This value is used for parts for which no qty adj tolerance is set up in PartWhse. Zero indicates all quantity adjustments will be posted. This parameter is used to control the count discrepancy of parts that are counted by weight on a scale. Counts often vary based upon humidity. If the count of the part is within this tolerance but different from the frozen quantity then no inventory adjustment will be posted.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse. Zero indicates that any quantity variance is considered out of tolerance. A number greater than zero indicates that a count quantity that varies from the frozen quantity by more than the quantity tolerance figure is considered out of tolerance.  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  """  
      self.DemandQty:int = obj["DemandQty"]
      """  This is a summary of the total outstanding manufacturing allocation requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  This is a summary of the total outstanding manufacturing requirements for this Part in this Site.  It is updated from Order Release records that are being manufactured. The outstanding  Sales Order Requirements is calculated from Open ORderRel records as  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  This is a summary of the total outstanding job allocation requirements for this Part in this Site.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Number  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Cross Reference Part Type  """  
      self.NeverReuseMRPJob:bool = obj["NeverReuseMRPJob"]
      """  System flag future use  """  
      self.DeleteMRPJobs:bool = obj["DeleteMRPJobs"]
      """  Flag indicates the need to delete unfirm Jobs even if MRP is run with the recycle job option  """  
      self.TotMfgLeadTimeSys:int = obj["TotMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the total lead time needed to generate the part, which includes the time on lower level parts, lead times, etc.  Not editable by the user.  """  
      self.TotMfgLeadTimeMnl:int = obj["TotMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the total lead time needed to generate the part.  Directly maintained by the user.  """  
      self.LvlMfgLeadTimeSys:int = obj["LvlMfgLeadTimeSys"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). The user cannot edit this value.  """  
      self.LvlMfgLeadTimeMnl:int = obj["LvlMfgLeadTimeMnl"]
      """  Displays the manufacturing lead time calculated by the system. This is the lead time required to manufacture the part at the level of this part, it includes the time to manufacture the subassemblies in the same job (Pull as Assembly materials). Directly maintained by the user.  """  
      self.MfgLeadTimeCalcDate:str = obj["MfgLeadTimeCalcDate"]
      """  The date the system manufacturing lead times (TotMfglLeadTimeSys and LvlMfgLeadTimeSys) were calculated.  """  
      self.MfgLeadTimeMnlDate:str = obj["MfgLeadTimeMnlDate"]
      """  The date the manual manufacturing lead times (TotMfgLeadTimeSys and LvlMfgLeadTimeSys) were entered by the user.  """  
      self.AutoConsumeStock:bool = obj["AutoConsumeStock"]
      """  Auto consume available stock when MRP runs and creates a job.  """  
      self.StartMinLotQty:bool = obj["StartMinLotQty"]
      """  Start the minimum lot quantity for a job when there is enough quantity to do so.  If enough quantity is available for the minimum lot quantity, the job will be split - one job for the quantity that can be started, another job for the remaining quantity.  Used when MRP creates jobs.  """  
      self.MinLotLeadTime:int = obj["MinLotLeadTime"]
      """  The lead time to consider for constrained materials when determining if a quantity can be started on a job.  Applicable when StartMinLotQty is true.  """  
      self.MfgLeadTimeMnl:bool = obj["MfgLeadTimeMnl"]
      """  Indicates manufacturing lead times are entered manually by the user.  """  
      self.MfgLeadTimeEnteredBy:str = obj["MfgLeadTimeEnteredBy"]
      """  Userid of user who entered manual manufacturing lead times.  """  
      self.MinStartQty:int = obj["MinStartQty"]
      """  Indicates the minumum quantity that can be started when splitting a job.  Used when the StartMinLotQty option is selected.  """  
      self.RawMaterial:bool = obj["RawMaterial"]
      """  Raw Material  """  
      self.MultiLevelCTP:bool = obj["MultiLevelCTP"]
      """  Available for stock manufactured parts.  Indicates if capable to promise considers sub-assemblies when determining the capable to promise date.  When false, capable to promise only looks at ATP for the capable to promise part - subassemblies are not considered.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Vendor, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.ConsumeSafety:bool = obj["ConsumeSafety"]
      """  Indicates if MRP should allow consumption of safety stock within the purchase lead time  """  
      self.SLTVendorNum:int = obj["SLTVendorNum"]
      """  Number of Alternate Vendor master that this part can be purchased from with short lead times. The Purchase Order will be generated for this supplier when suggestions fall within the purchasing lead time and the projected supply drops below safely.  """  
      self.SLTPurPoint:str = obj["SLTPurPoint"]
      """  Default Vendor purchase point ID.  """  
      self.ShortLeadTime:int = obj["ShortLeadTime"]
      """  Used to record the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentLeadTime:int = obj["UrgentLeadTime"]
      """  This is the lead time used when generating a new suggestion within the lead time window.  If this field is 0 and the Supplier is determined from the Supplier Price List, the suggestion will use the lead time from the price list.  """  
      self.UrgentMinOrdQty:int = obj["UrgentMinOrdQty"]
      """  This is the minimum qty required when generating a new suggestion within the lead time window.  """  
      self.UrgentMultQty:int = obj["UrgentMultQty"]
      """  This is used to calculate the suggestion qty to the nearest multiple when generating a new suggestion within the lead time window.  """  
      self.UrgentPurPoint:str = obj["UrgentPurPoint"]
      """  See UrgentVendorNum  """  
      self.UrgentVendorNum:int = obj["UrgentVendorNum"]
      """  If this field is not populated then the system will use the standard Supplier from PartPlant, or the last Supplier the part was purchased from, or the Supplier from the first Price list found for the part.  """  
      self.PartRunMRP:bool = obj["PartRunMRP"]
      """  PartRunMRP  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.MMSExclude:bool = obj["MMSExclude"]
      """  Indicates if this part will be excluded in the Inventory Min/Max/Safety calculation.  """  
      self.MMSSales:bool = obj["MMSSales"]
      """  Indicates if sales history for this part will be included in the Inventory Min/Max/Safety calculation.  """  
      self.MMSIssue:bool = obj["MMSIssue"]
      """  Indicates if job materials history for this part will be included in the Inventory Min/Max/Safety calculation.  """  
      self.MMSHistory:int = obj["MMSHistory"]
      """  User defined number in days, of how far back to look in usage history.  """  
      self.MMSSafetyFactor:int = obj["MMSSafetyFactor"]
      """  User defined, percentage of MIN to be set as Safety stock value.  """  
      self.MMSMaxFactor:int = obj["MMSMaxFactor"]
      """  User defined, used in calculation to defined MAX stock value.  """  
      self.SavedMinimumQty:int = obj["SavedMinimumQty"]
      """  WIll hold the proposed Min when the Min/Max/Safety process is ran  """  
      self.SavedMaximumQty:int = obj["SavedMaximumQty"]
      """  WIll hold the proposed Max when the Min/Max/Safety process is ran  """  
      self.SavedSafetyQty:int = obj["SavedSafetyQty"]
      """  WIll hold the proposed Safety when the Min/Max/Safety process is ran  """  
      self.SavedCalculatedUsageQty:int = obj["SavedCalculatedUsageQty"]
      """  It will hold the last TotalUsage used for the Saved Min/Max/Safety  """  
      self.SavedOnDateTime:str = obj["SavedOnDateTime"]
      """  Last Date when the Saved Min/Max/Safety were updated  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.ACWDays:int = obj["ACWDays"]
      """  Auto consume window days, this is the number of days that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.GenNewPCIDDelaySeconds:int = obj["GenNewPCIDDelaySeconds"]
      """  GenNewPCIDDelaySeconds  """  
      self.GenNewPCIDLimitDays:int = obj["GenNewPCIDLimitDays"]
      """  GenNewPCIDLimitDays  """  
      self.TopLvlMfgLeadTimeSys:int = obj["TopLvlMfgLeadTimeSys"]
      """  System calculated manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only.  Does not include the time on lower level parts.  Not editable by the user.  """  
      self.TopLvlMfgLeadTimeMnl:int = obj["TopLvlMfgLeadTimeMnl"]
      """  Manually entered manufacturing lead time.  This is the lead time needed to generate the part at the level of this part only. Does not include the time on lower level parts. Directly maintained by the user.  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.IncludedIntoAllocationBase:bool = obj["IncludedIntoAllocationBase"]
      """  Included Into Allocation Base  """  
      self.ForecastDaysBefore:int = obj["ForecastDaysBefore"]
      """  Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce forecast.  """  
      self.ForecastDaysAfter:int = obj["ForecastDaysAfter"]
      """  Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity. Ex: Forecast date of 3/31/98, Days after of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base UOM Code from Part Master  """  
      self.CalculatedLeadTime:int = obj["CalculatedLeadTime"]
      """  Used to calculate the normal order lead time for a Part for this Site. This value is represented in days. It is optional. Used in calculation of suggested order dates, as a default value in job material detail records.  """  
      self.ExtLeadTime:int = obj["ExtLeadTime"]
      self.SNNumODigits:int = obj["SNNumODigits"]
      """  Used to designate the number of digits for an Integer or Mask type serial number format.  """  
      self.UrgentVendorName:str = obj["UrgentVendorName"]
      self.UrgentVendorVendorID:str = obj["UrgentVendorVendorID"]
      self.DisableQtyBrng:bool = obj["DisableQtyBrng"]
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Used to indicate if the Serial Number format button should be enabled.  """  
      self.ICTrader:bool = obj["ICTrader"]
      self.InActive:bool = obj["InActive"]
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouses where the bin is a nettable bin (WhseBin.NonNettable = NO).  """  
      self.PlantConfCtrlSerialTracking:int = obj["PlantConfCtrlSerialTracking"]
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      """  Used to designate the number of leading zeros for an Integer or Mask type serial number format.  """  
      self.HasOnHandQty:bool = obj["HasOnHandQty"]
      """  Indicates if there is any quantity on hand for this part  """  
      self.IsActCostingAllocEnabled:bool = obj["IsActCostingAllocEnabled"]
      self.MaximumQtyNofP:int = obj["MaximumQtyNofP"]
      """  Number of Pieces for MaximumQty  """  
      self.MaxMfgLotSizeNofP:int = obj["MaxMfgLotSizeNofP"]
      """  Number of Pieces for MaxMfgLotSize  """  
      self.MfgLotMultipleNofP:int = obj["MfgLotMultipleNofP"]
      """  Number of Pieces for MfgLotMultiple  """  
      self.MinimumQtyNofP:int = obj["MinimumQtyNofP"]
      """  Number of Pieces for MinimumQty  """  
      self.MinMfgLotSizeNofP:int = obj["MinMfgLotSizeNofP"]
      """  Number of Pieces for MinMfgLotSize  """  
      self.MinOrderQtyNofP:int = obj["MinOrderQtyNofP"]
      """  Number of Pieces for MinOrderQty  """  
      self.MinStartQtyNofP:int = obj["MinStartQtyNofP"]
      """  Number of Pieces for MinStartQty  """  
      self.QtyDisplayOption:str = obj["QtyDisplayOption"]
      self.SafetyQtyNofP:int = obj["SafetyQtyNofP"]
      """  Number of Pieces for SafetyQty  """  
      self.ShortHorizonMaxMfgLotSizeNofP:int = obj["ShortHorizonMaxMfgLotSizeNofP"]
      """  Number of Pieces for ShortHorizonMaxMfgLotSize  """  
      self.ShortHorizonMinMfgLotSizeNofP:int = obj["ShortHorizonMinMfgLotSizeNofP"]
      """  Number of Pieces for ShortHorizonMinMfgLotSize  """  
      self.UrgentMinOrdQtyNofP:int = obj["UrgentMinOrdQtyNofP"]
      """  Number of Pieces for UrgentMinOrdQty  """  
      self.UrgentMultQtyNofP:int = obj["UrgentMultQtyNofP"]
      """  Number of Pieces for UrgentMultQty  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PersonName:str = obj["PersonName"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseDescription:str = obj["PrimWhseDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.TransferPlantName:str = obj["TransferPlantName"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartPlantSearchTableset:
   def __init__(self, obj):
      self.PartPlant:list[Erp_Tablesets_PartPlantRow] = obj["PartPlant"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartPlantSearchTableset:
   def __init__(self, obj):
      self.PartPlant:list[Erp_Tablesets_PartPlantRow] = obj["PartPlant"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetActiveParts_input:
   """ Required : 
   WhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  Whereclause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetActiveParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartPlantListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartPlant_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartPlantSearchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartPlantSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartPlantPlanningParameters_input:
   """ Required : 
   partNum
   attributeSetID
   plant
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.plant:str = obj["plant"]
      pass

class GetPartPlantPlanningParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePartPlant
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartPlant:str = obj["whereClausePartPlant"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlantSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPartPlantSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartPlantSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartPlantSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartPlantSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

