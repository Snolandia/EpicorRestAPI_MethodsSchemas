import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbPartSearchSvc
# Description: Global Part Search object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbPartSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbPartSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbPartSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches",headers=creds) as resp:
           return await resp.json()

async def post_GlbPartSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbPartSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company, GlbCompany, GlbPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbPartSearch item
   Description: Calls GetByID to retrieve the GlbPartSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPartNum: Desc: GlbPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company, GlbCompany, GlbPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbPartSearch for the service
   Description: Calls UpdateExt to update GlbPartSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPartNum: Desc: GlbPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbPartSearches_Company_GlbCompany_GlbPartNum(Company, GlbCompany, GlbPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbPartSearch item
   Description: Call UpdateExt to delete GlbPartSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbPartSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPartNum: Desc: GlbPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/GlbPartSearches(" + Company + "," + GlbCompany + "," + GlbPartNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbPart, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbPart=" + whereClauseGlbPart
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbPartNum, epicorHeaders = None):
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
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbPartNum=" + glbPartNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPartSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbPartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbPartRow] = obj["value"]
      pass

class Erp_Tablesets_GlbPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """  Indicates if this part is dimension tracked  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPartNum:str = obj["GlbPartNum"]
      """  The Owner's PartNum field identifies the Part and is used as the primary key.  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPartNum:str = obj["OldPartNum"]
      """  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.SNFormat:str = obj["SNFormat"]
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.Constrained:bool = obj["Constrained"]
      self.UPCCode1:str = obj["UPCCode1"]
      self.UPCCode2:str = obj["UPCCode2"]
      self.UPCCode3:str = obj["UPCCode3"]
      self.EDICode:str = obj["EDICode"]
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.WebInStock:bool = obj["WebInStock"]
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MDPV:int = obj["MDPV"]
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      self.NetVolume:int = obj["NetVolume"]
      self.RecDocReq:bool = obj["RecDocReq"]
      self.ShipDocReq:bool = obj["ShipDocReq"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.AESExp:str = obj["AESExp"]
      self.ECCNNumber:str = obj["ECCNNumber"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.UOMClassID:str = obj["UOMClassID"]
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      self.LotBatch:bool = obj["LotBatch"]
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      self.LotCureDt:bool = obj["LotCureDt"]
      self.LotDigits:int = obj["LotDigits"]
      self.LotExpDt:bool = obj["LotExpDt"]
      self.LotFirmware:bool = obj["LotFirmware"]
      self.LotHeat:bool = obj["LotHeat"]
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      self.LotMfgDt:bool = obj["LotMfgDt"]
      self.LotMfgLot:bool = obj["LotMfgLot"]
      self.LotNxtNum:int = obj["LotNxtNum"]
      self.LotPrefix:str = obj["LotPrefix"]
      self.LotSeqID:str = obj["LotSeqID"]
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      self.DropShip:bool = obj["DropShip"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.IsConfigured:bool = obj["IsConfigured"]
      self.RefCategory:str = obj["RefCategory"]
      self.CSFCJ5:bool = obj["CSFCJ5"]
      self.CSFLMW:bool = obj["CSFLMW"]
      self.GrossWeight:int = obj["GrossWeight"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispPartNum:str = obj["DispPartNum"]
      self.LinkPartNum:str = obj["LinkPartNum"]
      self.TypeCodeDescription:str = obj["TypeCodeDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.StockPart:bool = obj["StockPart"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """  Indicates if this part is dimension tracked  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPartNum:str = obj["GlbPartNum"]
      """  The Owner's PartNum field identifies the Part and is used as the primary key.  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPartNum:str = obj["OldPartNum"]
      """  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.SNFormat:str = obj["SNFormat"]
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.Constrained:bool = obj["Constrained"]
      self.UPCCode1:str = obj["UPCCode1"]
      self.UPCCode2:str = obj["UPCCode2"]
      self.UPCCode3:str = obj["UPCCode3"]
      self.EDICode:str = obj["EDICode"]
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.WebInStock:bool = obj["WebInStock"]
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MDPV:int = obj["MDPV"]
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      self.NetVolume:int = obj["NetVolume"]
      self.RecDocReq:bool = obj["RecDocReq"]
      self.ShipDocReq:bool = obj["ShipDocReq"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.AESExp:str = obj["AESExp"]
      self.ECCNNumber:str = obj["ECCNNumber"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.UOMClassID:str = obj["UOMClassID"]
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      self.LotBatch:bool = obj["LotBatch"]
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      self.LotCureDt:bool = obj["LotCureDt"]
      self.LotDigits:int = obj["LotDigits"]
      self.LotExpDt:bool = obj["LotExpDt"]
      self.LotFirmware:bool = obj["LotFirmware"]
      self.LotHeat:bool = obj["LotHeat"]
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      self.LotMfgDt:bool = obj["LotMfgDt"]
      self.LotMfgLot:bool = obj["LotMfgLot"]
      self.LotNxtNum:int = obj["LotNxtNum"]
      self.LotPrefix:str = obj["LotPrefix"]
      self.LotSeqID:str = obj["LotSeqID"]
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      self.DropShip:bool = obj["DropShip"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.IsConfigured:bool = obj["IsConfigured"]
      self.RefCategory:str = obj["RefCategory"]
      self.CSFCJ5:bool = obj["CSFCJ5"]
      self.CSFLMW:bool = obj["CSFLMW"]
      self.GrossWeight:int = obj["GrossWeight"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ISRegion:str = obj["ISRegion"]
      """  ISRegion  """  
      self.INChapterID:str = obj["INChapterID"]
      """  INChapterID  """  
      self.EstimateID:str = obj["EstimateID"]
      """  EstimateID  """  
      self.EstimateOrPlan:str = obj["EstimateOrPlan"]
      """  EstimateOrPlan  """  
      self.DiffPrc2PrchUOM:bool = obj["DiffPrc2PrchUOM"]
      """  DiffPrc2PrchUOM  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.PricingFactor:int = obj["PricingFactor"]
      """  PricingFactor  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.MobilePart:bool = obj["MobilePart"]
      """  MobilePart  """  
      self.AGUseGoodMark:bool = obj["AGUseGoodMark"]
      """  AGUseGoodMark  """  
      self.AGProductMark:bool = obj["AGProductMark"]
      """  AGProductMark  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  CSF Peru -  SUNAT Type  """  
      self.PESUNATUOM:str = obj["PESUNATUOM"]
      """  PESUNATUOM  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.PartLengthWidthHeightUM:str = obj["PartLengthWidthHeightUM"]
      """  PartLengthWidthHeightUM  """  
      self.DiameterUM:str = obj["DiameterUM"]
      """  DiameterUM  """  
      self.DiameterInside:int = obj["DiameterInside"]
      """  DiameterInside  """  
      self.DiameterOutside:int = obj["DiameterOutside"]
      """  DiameterOutside  """  
      self.ThicknessUM:str = obj["ThicknessUM"]
      """  ThicknessUM  """  
      self.Thickness:int = obj["Thickness"]
      """  Thickness  """  
      self.ThicknessMax:int = obj["ThicknessMax"]
      """  ThicknessMax  """  
      self.Durometer:str = obj["Durometer"]
      """  Durometer  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.EngineeringAlert:str = obj["EngineeringAlert"]
      """  EngineeringAlert  """  
      self.Condition:str = obj["Condition"]
      """  Condition  """  
      self.IsCompliant:bool = obj["IsCompliant"]
      """  IsCompliant  """  
      self.IsRestricted:bool = obj["IsRestricted"]
      """  IsRestricted  """  
      self.IsSafetyItem:bool = obj["IsSafetyItem"]
      """  IsSafetyItem  """  
      self.CommercialBrand:str = obj["CommercialBrand"]
      """  CommercialBrand  """  
      self.CommercialSubBrand:str = obj["CommercialSubBrand"]
      """  CommercialSubBrand  """  
      self.CommercialCategory:str = obj["CommercialCategory"]
      """  CommercialCategory  """  
      self.CommercialSubCategory:str = obj["CommercialSubCategory"]
      """  CommercialSubCategory  """  
      self.CommercialStyle:str = obj["CommercialStyle"]
      """  CommercialStyle  """  
      self.CommercialSize1:str = obj["CommercialSize1"]
      """  CommercialSize1  """  
      self.CommercialSize2:str = obj["CommercialSize2"]
      """  CommercialSize2  """  
      self.CommercialColor:str = obj["CommercialColor"]
      """  CommercialColor  """  
      self.IsGiftCard:bool = obj["IsGiftCard"]
      """  IsGiftCard  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  PhotoFile  """  
      self.PartPhotoExists:bool = obj["PartPhotoExists"]
      """  PartPhotoExists  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.PartSpecificPackingUOM:bool = obj["PartSpecificPackingUOM"]
      """  PartSpecificPackingUOM  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  CNSpecification  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  SyncToExternalCRM  """  
      self.ExternalCRMPartID:str = obj["ExternalCRMPartID"]
      """  ExternalCRMPartID  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  ExternalCRMLastSync  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  ExternalCRMSyncRequired  """  
      self.PESUNATTypeCode:str = obj["PESUNATTypeCode"]
      """  PESUNATTypeCode  """  
      self.PESUNATUOMCode:str = obj["PESUNATUOMCode"]
      """  PESUNATUOMCode  """  
      self.CNCodeVersion:str = obj["CNCodeVersion"]
      """  CNCodeVersion  """  
      self.CNTaxCategoryCode:str = obj["CNTaxCategoryCode"]
      """  CNTaxCategoryCode  """  
      self.CNHasPreferentialTreatment:bool = obj["CNHasPreferentialTreatment"]
      """  CNHasPreferentialTreatment  """  
      self.CNPreferentialTreatmentContent:str = obj["CNPreferentialTreatmentContent"]
      """  CNPreferentialTreatmentContent  """  
      self.CNZeroTaxRateMark:str = obj["CNZeroTaxRateMark"]
      """  CNZeroTaxRateMark  """  
      self.SubLevelCode:int = obj["SubLevelCode"]
      """  SubLevelCode  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User the part was created by  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date the part was created on  """  
      self.AttBatch:str = obj["AttBatch"]
      """  AttBatch  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  AttMfgBatch  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  AttMfgLot  """  
      self.AttHeat:str = obj["AttHeat"]
      """  AttHeat  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  AttFirmware  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  AttBeforeDt  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  AttMfgDt  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  AttCureDt  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  AttExpDt  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  DeferPurchaseReceipt  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  DeferJobReceipt  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  DeferInspection  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  DeferQtyAdjustment  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  DeferInventoryMove  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  DeferShipments  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  DeferInventoryCounts  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  DeferReturnMaterials  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date/Time when the Part record was last updated.  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  SendToFSA  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  ExternalMESSyncRequired  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  ExternalMESLastSync  """  
      self.FSAItem:bool = obj["FSAItem"]
      """  FSAItem  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  FSAEquipment  """  
      self.BOLClass:str = obj["BOLClass"]
      """  BOLClass  """  
      self.FairMarketValue:int = obj["FairMarketValue"]
      """  FairMarketValue  """  
      self.SAFTProdCategory:str = obj["SAFTProdCategory"]
      """  SAFTProdCategory  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  AttrClassID  """  
      self.LocationIDNumReq:bool = obj["LocationIDNumReq"]
      """  LocationIDNumReq  """  
      self.LocationTrackInv:bool = obj["LocationTrackInv"]
      """  LocationTrackInv  """  
      self.LocationMtlView:bool = obj["LocationMtlView"]
      """  LocationMtlView  """  
      self.LCNRVReporting:bool = obj["LCNRVReporting"]
      """  LCNRVReporting  """  
      self.LCNRVEstimatedUnitPrice:int = obj["LCNRVEstimatedUnitPrice"]
      """  LCNRVEstimatedUnitPrice  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.LocationFormatID:str = obj["LocationFormatID"]
      """  LocationFormatID  """  
      self.IsServices:bool = obj["IsServices"]
      """  IsServices  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PEDetrGoodServiceCode  """  
      self.PEProductServiceCode:str = obj["PEProductServiceCode"]
      """  PEProductServiceCode  """  
      self.DualUOMClassID:str = obj["DualUOMClassID"]
      """  DualUOMClassID  """  
      self.CNProductName:str = obj["CNProductName"]
      """  CNProductName  """  
      self.CNWeight:int = obj["CNWeight"]
      """  CNWeight  """  
      self.CNWeightUOM:str = obj["CNWeightUOM"]
      """  CNWeightUOM  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.ExternalID:str = obj["ExternalID"]
      """  ExternalID  """  
      self.CommoditySchemeID:str = obj["CommoditySchemeID"]
      """  CommoditySchemeID  """  
      self.CommoditySchemeVersion:str = obj["CommoditySchemeVersion"]
      """  CommoditySchemeVersion  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  TrackInventoryByRevision  """  
      self.PlanningByRevision:bool = obj["PlanningByRevision"]
      """  PlanningByRevision  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMPartType:int = obj["FSMPartType"]
      """  FSMPartType  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.LinkPartNum:str = obj["LinkPartNum"]
      self.UserDecimal3:int = obj["UserDecimal3"]
      """  UserDecimal3  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.UserDecimal4:int = obj["UserDecimal4"]
      """  UserDecimal4  """  
      self.StockPart:bool = obj["StockPart"]
      self.TypeCodeDescription:str = obj["TypeCodeDescription"]
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.DispPartNum:str = obj["DispPartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   glbCompany
   glbPartNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbPartNum:str = obj["glbPartNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbPartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """  Indicates if this part is dimension tracked  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPartNum:str = obj["GlbPartNum"]
      """  The Owner's PartNum field identifies the Part and is used as the primary key.  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPartNum:str = obj["OldPartNum"]
      """  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.SNFormat:str = obj["SNFormat"]
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.Constrained:bool = obj["Constrained"]
      self.UPCCode1:str = obj["UPCCode1"]
      self.UPCCode2:str = obj["UPCCode2"]
      self.UPCCode3:str = obj["UPCCode3"]
      self.EDICode:str = obj["EDICode"]
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.WebInStock:bool = obj["WebInStock"]
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MDPV:int = obj["MDPV"]
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      self.NetVolume:int = obj["NetVolume"]
      self.RecDocReq:bool = obj["RecDocReq"]
      self.ShipDocReq:bool = obj["ShipDocReq"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.AESExp:str = obj["AESExp"]
      self.ECCNNumber:str = obj["ECCNNumber"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.UOMClassID:str = obj["UOMClassID"]
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      self.LotBatch:bool = obj["LotBatch"]
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      self.LotCureDt:bool = obj["LotCureDt"]
      self.LotDigits:int = obj["LotDigits"]
      self.LotExpDt:bool = obj["LotExpDt"]
      self.LotFirmware:bool = obj["LotFirmware"]
      self.LotHeat:bool = obj["LotHeat"]
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      self.LotMfgDt:bool = obj["LotMfgDt"]
      self.LotMfgLot:bool = obj["LotMfgLot"]
      self.LotNxtNum:int = obj["LotNxtNum"]
      self.LotPrefix:str = obj["LotPrefix"]
      self.LotSeqID:str = obj["LotSeqID"]
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      self.DropShip:bool = obj["DropShip"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.IsConfigured:bool = obj["IsConfigured"]
      self.RefCategory:str = obj["RefCategory"]
      self.CSFCJ5:bool = obj["CSFCJ5"]
      self.CSFLMW:bool = obj["CSFLMW"]
      self.GrossWeight:int = obj["GrossWeight"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispPartNum:str = obj["DispPartNum"]
      self.LinkPartNum:str = obj["LinkPartNum"]
      self.TypeCodeDescription:str = obj["TypeCodeDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.StockPart:bool = obj["StockPart"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPartListTableset:
   def __init__(self, obj):
      self.GlbPartList:list[Erp_Tablesets_GlbPartListRow] = obj["GlbPartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  This field can not be blank.  """  
      self.ClassID:str = obj["ClassID"]
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """  This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.
Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """  Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget. To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """  Indicates if this part is dimension tracked  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Sales Order entry as the default on line item details.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """   NOTE: NOT IMPLEMENTED ON INITIAL 5.0.300 RELEASE.
if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """   The reason code that links to a Reason master record, which indicates why the part has been placed on hold.
Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPartNum:str = obj["GlbPartNum"]
      """  The Owner's PartNum field identifies the Part and is used as the primary key.  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPartNum:str = obj["OldPartNum"]
      """  The Original Owner's PartNum field identifies the Part and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.SNFormat:str = obj["SNFormat"]
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.Constrained:bool = obj["Constrained"]
      self.UPCCode1:str = obj["UPCCode1"]
      self.UPCCode2:str = obj["UPCCode2"]
      self.UPCCode3:str = obj["UPCCode3"]
      self.EDICode:str = obj["EDICode"]
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global parts.  The user can come back at a later time and choose to link a skipped part if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.WebInStock:bool = obj["WebInStock"]
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MDPV:int = obj["MDPV"]
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      self.NetVolume:int = obj["NetVolume"]
      self.RecDocReq:bool = obj["RecDocReq"]
      self.ShipDocReq:bool = obj["ShipDocReq"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.AESExp:str = obj["AESExp"]
      self.ECCNNumber:str = obj["ECCNNumber"]
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      self.ExpLicType:str = obj["ExpLicType"]
      self.HazClass:str = obj["HazClass"]
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      self.HazItem:bool = obj["HazItem"]
      self.HazPackInstr:str = obj["HazPackInstr"]
      self.HazSub:str = obj["HazSub"]
      self.HazTechName:str = obj["HazTechName"]
      self.HTS:str = obj["HTS"]
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      self.NAFTAPref:str = obj["NAFTAPref"]
      self.NAFTAProd:str = obj["NAFTAProd"]
      self.SchedBcode:str = obj["SchedBcode"]
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.UOMClassID:str = obj["UOMClassID"]
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      self.LotBatch:bool = obj["LotBatch"]
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      self.LotCureDt:bool = obj["LotCureDt"]
      self.LotDigits:int = obj["LotDigits"]
      self.LotExpDt:bool = obj["LotExpDt"]
      self.LotFirmware:bool = obj["LotFirmware"]
      self.LotHeat:bool = obj["LotHeat"]
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      self.LotMfgDt:bool = obj["LotMfgDt"]
      self.LotMfgLot:bool = obj["LotMfgLot"]
      self.LotNxtNum:int = obj["LotNxtNum"]
      self.LotPrefix:str = obj["LotPrefix"]
      self.LotSeqID:str = obj["LotSeqID"]
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      self.DropShip:bool = obj["DropShip"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.IsConfigured:bool = obj["IsConfigured"]
      self.RefCategory:str = obj["RefCategory"]
      self.CSFCJ5:bool = obj["CSFCJ5"]
      self.CSFLMW:bool = obj["CSFLMW"]
      self.GrossWeight:int = obj["GrossWeight"]
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ISRegion:str = obj["ISRegion"]
      """  ISRegion  """  
      self.INChapterID:str = obj["INChapterID"]
      """  INChapterID  """  
      self.EstimateID:str = obj["EstimateID"]
      """  EstimateID  """  
      self.EstimateOrPlan:str = obj["EstimateOrPlan"]
      """  EstimateOrPlan  """  
      self.DiffPrc2PrchUOM:bool = obj["DiffPrc2PrchUOM"]
      """  DiffPrc2PrchUOM  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.PricingFactor:int = obj["PricingFactor"]
      """  PricingFactor  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.MobilePart:bool = obj["MobilePart"]
      """  MobilePart  """  
      self.AGUseGoodMark:bool = obj["AGUseGoodMark"]
      """  AGUseGoodMark  """  
      self.AGProductMark:bool = obj["AGProductMark"]
      """  AGProductMark  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  CSF Peru -  SUNAT Type  """  
      self.PESUNATUOM:str = obj["PESUNATUOM"]
      """  PESUNATUOM  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.PartLengthWidthHeightUM:str = obj["PartLengthWidthHeightUM"]
      """  PartLengthWidthHeightUM  """  
      self.DiameterUM:str = obj["DiameterUM"]
      """  DiameterUM  """  
      self.DiameterInside:int = obj["DiameterInside"]
      """  DiameterInside  """  
      self.DiameterOutside:int = obj["DiameterOutside"]
      """  DiameterOutside  """  
      self.ThicknessUM:str = obj["ThicknessUM"]
      """  ThicknessUM  """  
      self.Thickness:int = obj["Thickness"]
      """  Thickness  """  
      self.ThicknessMax:int = obj["ThicknessMax"]
      """  ThicknessMax  """  
      self.Durometer:str = obj["Durometer"]
      """  Durometer  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.EngineeringAlert:str = obj["EngineeringAlert"]
      """  EngineeringAlert  """  
      self.Condition:str = obj["Condition"]
      """  Condition  """  
      self.IsCompliant:bool = obj["IsCompliant"]
      """  IsCompliant  """  
      self.IsRestricted:bool = obj["IsRestricted"]
      """  IsRestricted  """  
      self.IsSafetyItem:bool = obj["IsSafetyItem"]
      """  IsSafetyItem  """  
      self.CommercialBrand:str = obj["CommercialBrand"]
      """  CommercialBrand  """  
      self.CommercialSubBrand:str = obj["CommercialSubBrand"]
      """  CommercialSubBrand  """  
      self.CommercialCategory:str = obj["CommercialCategory"]
      """  CommercialCategory  """  
      self.CommercialSubCategory:str = obj["CommercialSubCategory"]
      """  CommercialSubCategory  """  
      self.CommercialStyle:str = obj["CommercialStyle"]
      """  CommercialStyle  """  
      self.CommercialSize1:str = obj["CommercialSize1"]
      """  CommercialSize1  """  
      self.CommercialSize2:str = obj["CommercialSize2"]
      """  CommercialSize2  """  
      self.CommercialColor:str = obj["CommercialColor"]
      """  CommercialColor  """  
      self.IsGiftCard:bool = obj["IsGiftCard"]
      """  IsGiftCard  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  PhotoFile  """  
      self.PartPhotoExists:bool = obj["PartPhotoExists"]
      """  PartPhotoExists  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.PartSpecificPackingUOM:bool = obj["PartSpecificPackingUOM"]
      """  PartSpecificPackingUOM  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  CNSpecification  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  SyncToExternalCRM  """  
      self.ExternalCRMPartID:str = obj["ExternalCRMPartID"]
      """  ExternalCRMPartID  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  ExternalCRMLastSync  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  ExternalCRMSyncRequired  """  
      self.PESUNATTypeCode:str = obj["PESUNATTypeCode"]
      """  PESUNATTypeCode  """  
      self.PESUNATUOMCode:str = obj["PESUNATUOMCode"]
      """  PESUNATUOMCode  """  
      self.CNCodeVersion:str = obj["CNCodeVersion"]
      """  CNCodeVersion  """  
      self.CNTaxCategoryCode:str = obj["CNTaxCategoryCode"]
      """  CNTaxCategoryCode  """  
      self.CNHasPreferentialTreatment:bool = obj["CNHasPreferentialTreatment"]
      """  CNHasPreferentialTreatment  """  
      self.CNPreferentialTreatmentContent:str = obj["CNPreferentialTreatmentContent"]
      """  CNPreferentialTreatmentContent  """  
      self.CNZeroTaxRateMark:str = obj["CNZeroTaxRateMark"]
      """  CNZeroTaxRateMark  """  
      self.SubLevelCode:int = obj["SubLevelCode"]
      """  SubLevelCode  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User the part was created by  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date the part was created on  """  
      self.AttBatch:str = obj["AttBatch"]
      """  AttBatch  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  AttMfgBatch  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  AttMfgLot  """  
      self.AttHeat:str = obj["AttHeat"]
      """  AttHeat  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  AttFirmware  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  AttBeforeDt  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  AttMfgDt  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  AttCureDt  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  AttExpDt  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  DeferPurchaseReceipt  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  DeferJobReceipt  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  DeferInspection  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  DeferQtyAdjustment  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  DeferInventoryMove  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  DeferShipments  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  DeferInventoryCounts  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  DeferReturnMaterials  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date/Time when the Part record was last updated.  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  SendToFSA  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  ExternalMESSyncRequired  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  ExternalMESLastSync  """  
      self.FSAItem:bool = obj["FSAItem"]
      """  FSAItem  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  FSAEquipment  """  
      self.BOLClass:str = obj["BOLClass"]
      """  BOLClass  """  
      self.FairMarketValue:int = obj["FairMarketValue"]
      """  FairMarketValue  """  
      self.SAFTProdCategory:str = obj["SAFTProdCategory"]
      """  SAFTProdCategory  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  AttrClassID  """  
      self.LocationIDNumReq:bool = obj["LocationIDNumReq"]
      """  LocationIDNumReq  """  
      self.LocationTrackInv:bool = obj["LocationTrackInv"]
      """  LocationTrackInv  """  
      self.LocationMtlView:bool = obj["LocationMtlView"]
      """  LocationMtlView  """  
      self.LCNRVReporting:bool = obj["LCNRVReporting"]
      """  LCNRVReporting  """  
      self.LCNRVEstimatedUnitPrice:int = obj["LCNRVEstimatedUnitPrice"]
      """  LCNRVEstimatedUnitPrice  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.LocationFormatID:str = obj["LocationFormatID"]
      """  LocationFormatID  """  
      self.IsServices:bool = obj["IsServices"]
      """  IsServices  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PEDetrGoodServiceCode  """  
      self.PEProductServiceCode:str = obj["PEProductServiceCode"]
      """  PEProductServiceCode  """  
      self.DualUOMClassID:str = obj["DualUOMClassID"]
      """  DualUOMClassID  """  
      self.CNProductName:str = obj["CNProductName"]
      """  CNProductName  """  
      self.CNWeight:int = obj["CNWeight"]
      """  CNWeight  """  
      self.CNWeightUOM:str = obj["CNWeightUOM"]
      """  CNWeightUOM  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.ExternalID:str = obj["ExternalID"]
      """  ExternalID  """  
      self.CommoditySchemeID:str = obj["CommoditySchemeID"]
      """  CommoditySchemeID  """  
      self.CommoditySchemeVersion:str = obj["CommoditySchemeVersion"]
      """  CommoditySchemeVersion  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  TrackInventoryByRevision  """  
      self.PlanningByRevision:bool = obj["PlanningByRevision"]
      """  PlanningByRevision  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMPartType:int = obj["FSMPartType"]
      """  FSMPartType  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.LinkPartNum:str = obj["LinkPartNum"]
      self.UserDecimal3:int = obj["UserDecimal3"]
      """  UserDecimal3  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.UserDecimal4:int = obj["UserDecimal4"]
      """  UserDecimal4  """  
      self.StockPart:bool = obj["StockPart"]
      self.TypeCodeDescription:str = obj["TypeCodeDescription"]
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.DispPartNum:str = obj["DispPartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPartSearchTableset:
   def __init__(self, obj):
      self.GlbPart:list[Erp_Tablesets_GlbPartRow] = obj["GlbPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbPartSearchTableset:
   def __init__(self, obj):
      self.GlbPart:list[Erp_Tablesets_GlbPartRow] = obj["GlbPart"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbPartNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbPartNum:str = obj["glbPartNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPartSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPartListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbPart_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbPartSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPartSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbPart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbPart:str = obj["whereClauseGlbPart"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbPartSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGlbPartSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbPartSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbPartSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPartSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

