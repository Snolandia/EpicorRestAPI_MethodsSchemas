import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlantTranSearchSvc
# Description: This BO was created to retrieve the information stored from the
           PartTran table. Uses this BO to retrieve the transactions between plants
           for one or more specified parts.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlantTranSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantTranSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches",headers=creds) as resp:
           return await resp.json()

async def post_PlantTranSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantTranSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantTranSearches_Company_TranNum(Company, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantTranSearch item
   Description: Calls GetByID to retrieve the PlantTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantTranSearches_Company_TranNum(Company, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantTranSearch for the service
   Description: Calls UpdateExt to update PlantTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantTranSearches_Company_TranNum(Company, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantTranSearch item
   Description: Call UpdateExt to delete PlantTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/PlantTranSearches(" + Company + "," + TranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlantTran, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePlantTran=" + whereClausePlantTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantTranRow] = obj["value"]
      pass

class Erp_Tablesets_PlantTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  PCID to receive from  """  
      self.ToPCID:str = obj["ToPCID"]
      """  PCID to receive to  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ParentFromPCID:str = obj["ParentFromPCID"]
      """  Parent PCID to the FromPCID field.  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tranNum
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PlantTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantTranListTableset:
   def __init__(self, obj):
      self.PlantTranList:list[Erp_Tablesets_PlantTranListRow] = obj["PlantTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  PCID to receive from  """  
      self.ToPCID:str = obj["ToPCID"]
      """  PCID to receive to  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ParentFromPCID:str = obj["ParentFromPCID"]
      """  Parent PCID to the FromPCID field.  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantTranSearchTableset:
   def __init__(self, obj):
      self.PlantTran:list[Erp_Tablesets_PlantTranRow] = obj["PlantTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPlantTranSearchTableset:
   def __init__(self, obj):
      self.PlantTran:list[Erp_Tablesets_PlantTranRow] = obj["PlantTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tranNum
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlantTran_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantTranSearchTableset] = obj["ds"]
      pass

class GetNewPlantTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePlantTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlantTran:str = obj["whereClausePlantTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantTranSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPlantTranSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlantTranSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantTranSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

