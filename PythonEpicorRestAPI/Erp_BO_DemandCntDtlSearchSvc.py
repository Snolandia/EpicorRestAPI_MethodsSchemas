import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandCntDtlSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandCntDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandCntDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandCntDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_DemandCntDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandCntDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandCntDtlSearch item
   Description: Calls GetByID to retrieve the DemandCntDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandCntDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandCntDtlSearch for the service
   Description: Calls UpdateExt to update DemandCntDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandCntDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandContractDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandCntDtlSearches_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandCntDtlSearch item
   Description: Call UpdateExt to delete DemandCntDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandCntDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/DemandCntDtlSearches(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandContractDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDemandContractDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDemandContractDtl=" + whereClauseDemandContractDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(demandContractNum, demandContractLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "demandContractNum=" + demandContractNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "demandContractLine=" + demandContractLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandContractDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandContractDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandContractDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandContractDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandContractDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandCntDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandContractDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandContractDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandContractDtlRow] = obj["value"]
      pass

class Erp_Tablesets_DemandContractDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandContractDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations.  """  
      self.DocPriceTolerance:int = obj["DocPriceTolerance"]
      """  Defines the tolerance for price difference validations in document currency.  """  
      self.Rpt1PriceTolerance:int = obj["Rpt1PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt2PriceTolerance:int = obj["Rpt2PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt3PriceTolerance:int = obj["Rpt3PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   demandContractNum
   demandContractLine
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandContractLine:int = obj["demandContractLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DemandCntDtlSearchTableset:
   def __init__(self, obj):
      self.DemandContractDtl:list[Erp_Tablesets_DemandContractDtlRow] = obj["DemandContractDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandContractDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandContractDtlListTableset:
   def __init__(self, obj):
      self.DemandContractDtlList:list[Erp_Tablesets_DemandContractDtlListRow] = obj["DemandContractDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandContractDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations.  """  
      self.DocPriceTolerance:int = obj["DocPriceTolerance"]
      """  Defines the tolerance for price difference validations in document currency.  """  
      self.Rpt1PriceTolerance:int = obj["Rpt1PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt2PriceTolerance:int = obj["Rpt2PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt3PriceTolerance:int = obj["Rpt3PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDemandCntDtlSearchTableset:
   def __init__(self, obj):
      self.DemandContractDtl:list[Erp_Tablesets_DemandContractDtlRow] = obj["DemandContractDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   demandContractNum
   demandContractLine
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandContractLine:int = obj["demandContractLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandContractDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDemandContractDtl_input:
   """ Required : 
   ds
   demandContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetNewDemandContractDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDemandContractDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandContractDtl:str = obj["whereClauseDemandContractDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDemandCntDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandCntDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandCntDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

