import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartCostSearchSvc
# Description: PartCostSearch retrieves the information about Part Costs
           Used to retrieve the Part Costs and its Totals
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartCostSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartCostSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartCostSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartCostRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches",headers=creds) as resp:
           return await resp.json()

async def post_PartCostSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartCostSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartCostRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartCostRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartCostSearches_Company_PartNum_CostID(Company, PartNum, CostID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartCostSearch item
   Description: Calls GetByID to retrieve the PartCostSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartCostSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartCostRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartCostSearches_Company_PartNum_CostID(Company, PartNum, CostID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartCostSearch for the service
   Description: Calls UpdateExt to update PartCostSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartCostSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartCostRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartCostSearches_Company_PartNum_CostID(Company, PartNum, CostID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartCostSearch item
   Description: Call UpdateExt to delete PartCostSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartCostSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/PartCostSearches(" + Company + "," + PartNum + "," + CostID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartCostListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartCost, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartCost=" + whereClausePartCost
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, costID, epicorHeaders = None):
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
   params += "costID=" + costID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartCost
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartCostSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartCostListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartCostRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartCostRow] = obj["value"]
      pass

class Erp_Tablesets_PartCostListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.AvgLaborCost:int = obj["AvgLaborCost"]
      """   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.AvgBurdenCost:int = obj["AvgBurdenCost"]
      """  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  """  
      self.AvgMaterialCost:int = obj["AvgMaterialCost"]
      """  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgSubContCost:int = obj["AvgSubContCost"]
      """  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgMtlBurCost:int = obj["AvgMtlBurCost"]
      """  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """  Standard Burden Unit Cost.
( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """  Standard Material Unit cost. ( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.LastLaborCost:int = obj["LastLaborCost"]
      """  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  """  
      self.LastBurdenCost:int = obj["LastBurdenCost"]
      """   Last Burden Unit Cost.
( see LastLaborCost for more info )  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      """  Last Material unit cost. ( see LastLaborCost for more info. )  """  
      self.LastSubContCost:int = obj["LastSubContCost"]
      """   Last Subcontract unit cost.
( see LastLaborCost for more info. )  """  
      self.LastMtlBurCost:int = obj["LastMtlBurCost"]
      """   Last Material Burden unit cost.
( see LastLaborCost for more info. )  """  
      self.FIFOAvgLaborCost:int = obj["FIFOAvgLaborCost"]
      """   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOAvgBurdenCost:int = obj["FIFOAvgBurdenCost"]
      """  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  """  
      self.FIFOAvgMaterialCost:int = obj["FIFOAvgMaterialCost"]
      """  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgSubContCost:int = obj["FIFOAvgSubContCost"]
      """  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgMtlBurCost:int = obj["FIFOAvgMtlBurCost"]
      """  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvgTotalCost:int = obj["AvgTotalCost"]
      """  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  """  
      self.StdTotalCost:int = obj["StdTotalCost"]
      """  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  """  
      self.LastTotalCost:int = obj["LastTotalCost"]
      """  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      """  used to display Cost Method description  """  
      self.FIFOAvgTotalCost:int = obj["FIFOAvgTotalCost"]
      """  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartCostRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.AvgLaborCost:int = obj["AvgLaborCost"]
      """   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.AvgBurdenCost:int = obj["AvgBurdenCost"]
      """  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  """  
      self.AvgMaterialCost:int = obj["AvgMaterialCost"]
      """  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgSubContCost:int = obj["AvgSubContCost"]
      """  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgMtlBurCost:int = obj["AvgMtlBurCost"]
      """  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """  Standard Burden Unit Cost.
( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """  Standard Material Unit cost. ( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.LastLaborCost:int = obj["LastLaborCost"]
      """  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  """  
      self.LastBurdenCost:int = obj["LastBurdenCost"]
      """   Last Burden Unit Cost.
( see LastLaborCost for more info )  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      """  Last Material unit cost. ( see LastLaborCost for more info. )  """  
      self.LastSubContCost:int = obj["LastSubContCost"]
      """   Last Subcontract unit cost.
( see LastLaborCost for more info. )  """  
      self.LastMtlBurCost:int = obj["LastMtlBurCost"]
      """   Last Material Burden unit cost.
( see LastLaborCost for more info. )  """  
      self.FIFOAvgLaborCost:int = obj["FIFOAvgLaborCost"]
      """   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOAvgBurdenCost:int = obj["FIFOAvgBurdenCost"]
      """  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  """  
      self.FIFOAvgMaterialCost:int = obj["FIFOAvgMaterialCost"]
      """  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgSubContCost:int = obj["FIFOAvgSubContCost"]
      """  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgMtlBurCost:int = obj["FIFOAvgMtlBurCost"]
      """  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalQtyAvg:int = obj["TotalQtyAvg"]
      """  Total OnHand Quantity used specific for Average Costing calculations  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      """  used to display Cost Method description  """  
      self.FIFOAvgTotalCost:int = obj["FIFOAvgTotalCost"]
      """  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  """  
      self.LastTotalCost:int = obj["LastTotalCost"]
      """  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      self.StdTotalCost:int = obj["StdTotalCost"]
      """  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  """  
      self.AvgTotalCost:int = obj["AvgTotalCost"]
      """  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   costID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.costID:str = obj["costID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartCostListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.AvgLaborCost:int = obj["AvgLaborCost"]
      """   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.AvgBurdenCost:int = obj["AvgBurdenCost"]
      """  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  """  
      self.AvgMaterialCost:int = obj["AvgMaterialCost"]
      """  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgSubContCost:int = obj["AvgSubContCost"]
      """  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgMtlBurCost:int = obj["AvgMtlBurCost"]
      """  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """  Standard Burden Unit Cost.
( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """  Standard Material Unit cost. ( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.LastLaborCost:int = obj["LastLaborCost"]
      """  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  """  
      self.LastBurdenCost:int = obj["LastBurdenCost"]
      """   Last Burden Unit Cost.
( see LastLaborCost for more info )  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      """  Last Material unit cost. ( see LastLaborCost for more info. )  """  
      self.LastSubContCost:int = obj["LastSubContCost"]
      """   Last Subcontract unit cost.
( see LastLaborCost for more info. )  """  
      self.LastMtlBurCost:int = obj["LastMtlBurCost"]
      """   Last Material Burden unit cost.
( see LastLaborCost for more info. )  """  
      self.FIFOAvgLaborCost:int = obj["FIFOAvgLaborCost"]
      """   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOAvgBurdenCost:int = obj["FIFOAvgBurdenCost"]
      """  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  """  
      self.FIFOAvgMaterialCost:int = obj["FIFOAvgMaterialCost"]
      """  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgSubContCost:int = obj["FIFOAvgSubContCost"]
      """  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgMtlBurCost:int = obj["FIFOAvgMtlBurCost"]
      """  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvgTotalCost:int = obj["AvgTotalCost"]
      """  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  """  
      self.StdTotalCost:int = obj["StdTotalCost"]
      """  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  """  
      self.LastTotalCost:int = obj["LastTotalCost"]
      """  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      """  used to display Cost Method description  """  
      self.FIFOAvgTotalCost:int = obj["FIFOAvgTotalCost"]
      """  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartCostListTableset:
   def __init__(self, obj):
      self.PartCostList:list[Erp_Tablesets_PartCostListRow] = obj["PartCostList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartCostRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.AvgLaborCost:int = obj["AvgLaborCost"]
      """   Average Unit Labor Cost of the Part. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Purchased Part receipts will roll this cost into average material cost and then set it to zeros.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.AvgBurdenCost:int = obj["AvgBurdenCost"]
      """  Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the AvgLaborCost for the formula for calculating average unit costs.  """  
      self.AvgMaterialCost:int = obj["AvgMaterialCost"]
      """  Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgSubContCost:int = obj["AvgSubContCost"]
      """  Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.AvgMtlBurCost:int = obj["AvgMtlBurCost"]
      """  Average Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.StdLaborCost:int = obj["StdLaborCost"]
      """   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.
(See AvgLaborCost for more info.)  """  
      self.StdBurdenCost:int = obj["StdBurdenCost"]
      """  Standard Burden Unit Cost.
( see StdLaborCost for more info )  """  
      self.StdMaterialCost:int = obj["StdMaterialCost"]
      """  Standard Material Unit cost. ( see StdLaborCost for more info).  """  
      self.StdSubContCost:int = obj["StdSubContCost"]
      """   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  """  
      self.StdMtlBurCost:int = obj["StdMtlBurCost"]
      """   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  """  
      self.LastLaborCost:int = obj["LastLaborCost"]
      """  Last Labor cost. Directly updated via the Part Master Maintenance program. Indirectly via Purchase Part receipts, Manufactured receipts or inventory cost adjustments if cost method is "last cost" .  The last costs are overlaid by the most recent receipt cost.  Both LastLaborCost and LastBurdenCost are set to zero when updated by a Purchased Part Receipt transaction.  """  
      self.LastBurdenCost:int = obj["LastBurdenCost"]
      """   Last Burden Unit Cost.
( see LastLaborCost for more info )  """  
      self.LastMaterialCost:int = obj["LastMaterialCost"]
      """  Last Material unit cost. ( see LastLaborCost for more info. )  """  
      self.LastSubContCost:int = obj["LastSubContCost"]
      """   Last Subcontract unit cost.
( see LastLaborCost for more info. )  """  
      self.LastMtlBurCost:int = obj["LastMtlBurCost"]
      """   Last Material Burden unit cost.
( see LastLaborCost for more info. )  """  
      self.FIFOAvgLaborCost:int = obj["FIFOAvgLaborCost"]
      """   FIFO Average Unit Labor Cost of the Part and updated only if the cost method is FIFO. This is an optional field. It is directly updated by Part Maintenance, indirectly by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program. Basically when updating a FIFO average cost the following logic is used.
 NEW FIFO AVG COST = sum of all (FIFO OnHandQty * FIFO Costs).
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part and CostID combination. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOAvgBurdenCost:int = obj["FIFOAvgBurdenCost"]
      """  FIFO Average burden unit cost. This is updated directly by Part Maintenance. It is indirectly updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOAvgLaborCost for the formula for calculating FIFO average unit costs.  """  
      self.FIFOAvgMaterialCost:int = obj["FIFOAvgMaterialCost"]
      """  FIFO Average Material Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgSubContCost:int = obj["FIFOAvgSubContCost"]
      """  FIFO Average Subcontract Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOAvgMtlBurCost:int = obj["FIFOAvgMtlBurCost"]
      """  FIFOAverage Material Burden Unit cost. Directly maintained by Part Maintenance. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOAvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalQtyAvg:int = obj["TotalQtyAvg"]
      """  Total OnHand Quantity used specific for Average Costing calculations  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      """  used to display Cost Method description  """  
      self.FIFOAvgTotalCost:int = obj["FIFOAvgTotalCost"]
      """  The sum of FIFOAvgBurdenCost, FIFOAvgLaborCost, FIFOAvgMaterialCost, FIFOAvgMtlBurCost and FIFOAvgSubContCost  """  
      self.LastTotalCost:int = obj["LastTotalCost"]
      """  The sum of LastBurdenCost, LastLaborCost, LastMaterialCost, LastMtlBurCost and LastSubContCost  """  
      self.PrimaryPlant:str = obj["PrimaryPlant"]
      self.StdTotalCost:int = obj["StdTotalCost"]
      """  The sum of StdBurdenCost, StdLaborCost, StdMaterialCost, StdMtlBurCost and StdSubContCost  """  
      self.AvgTotalCost:int = obj["AvgTotalCost"]
      """  The sum of AvgBurdenCost, AvgLaborCost, AvgMaterialCost, AvgMtlBurCost and AvgSubContCost  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartCostSearchTableset:
   def __init__(self, obj):
      self.PartCost:list[Erp_Tablesets_PartCostRow] = obj["PartCost"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartCostSearchTableset:
   def __init__(self, obj):
      self.PartCost:list[Erp_Tablesets_PartCostRow] = obj["PartCost"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   costID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.costID:str = obj["costID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartCostSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartCostSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartCostSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartCostListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartCost_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartCostSearchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartCostSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartCost
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartCost:str = obj["whereClausePartCost"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartCostSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPartCostSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartCostSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartCostSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartCostSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

