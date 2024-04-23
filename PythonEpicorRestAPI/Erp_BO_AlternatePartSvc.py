import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AlternatePartSvc
# Description: Substitute or Complement Part for another one
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AlternateParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlternateParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSubsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/AlternateParts",headers=creds) as resp:
           return await resp.json()

async def post_AlternateParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/AlternateParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlternateParts_Company_PartNum_SubPart(Company, PartNum, SubPart, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternatePart item
   Description: Calls GetByID to retrieve the AlternatePart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternatePart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/AlternateParts(" + Company + "," + PartNum + "," + SubPart + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlternateParts_Company_PartNum_SubPart(Company, PartNum, SubPart, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlternatePart for the service
   Description: Calls UpdateExt to update AlternatePart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternatePart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartSubsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/AlternateParts(" + Company + "," + PartNum + "," + SubPart + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlternateParts_Company_PartNum_SubPart(Company, PartNum, SubPart, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlternatePart item
   Description: Call UpdateExt to delete AlternatePart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternatePart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SubPart: Desc: SubPart   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/AlternateParts(" + Company + "," + PartNum + "," + SubPart + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartSubsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartSubs, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartSubs=" + whereClausePartSubs
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, subPart, epicorHeaders = None):
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
   params += "subPart=" + subPart

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListAlternateParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAlternateParts
   Description: This method returns a list Alternate part with some calculated columns added.
   OperationID: GetListAlternateParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAlternateParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAlternateParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListAlternatePartsForSO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAlternatePartsForSO
   Description: This method returns a list Alternate part with some calculated columns added.
   OperationID: GetListAlternatePartsForSO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAlternatePartsForSO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAlternatePartsForSO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSubs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSubs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlternatePartSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSubsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartSubsRow] = obj["value"]
      pass

class Erp_Tablesets_PartSubsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
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
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      """  Describes the Part.  """  
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.SubPartIUM:str = obj["SubPartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
      self.SugOrderQty:int = obj["SugOrderQty"]
      """  Suggested Quantity for Order Qty in Quote Detail  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      self.SubPartIUM:str = obj["SubPartIUM"]
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   subPart
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.subPart:str = obj["subPart"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AlternatePartTableset:
   def __init__(self, obj):
      self.PartSubs:list[Erp_Tablesets_PartSubsRow] = obj["PartSubs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSubsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
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
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      """  Describes the Part.  """  
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.SubPartIUM:str = obj["SubPartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartSubsListTableset:
   def __init__(self, obj):
      self.PartSubsList:list[Erp_Tablesets_PartSubsListRow] = obj["PartSubsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartSubsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part number that this substitute Part is for.  """  
      self.SubPart:str = obj["SubPart"]
      """  Substitute Part  """  
      self.RecType:str = obj["RecType"]
      """  Indicates the record type. "S" = Substitute, "C" = Compliment  """  
      self.SubType:str = obj["SubType"]
      """  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  """  
      self.QtyPer:int = obj["QtyPer"]
      """   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  """  
      self.Comment:str = obj["Comment"]
      """  Optional Comment  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultSub:bool = obj["DefaultSub"]
      self.Price:int = obj["Price"]
      """  Price for the Suggested Quantity  """  
      self.SuggestedQty:int = obj["SuggestedQty"]
      """  Suggested Quantity  """  
      self.Selected:bool = obj["Selected"]
      """  Selected Row  """  
      self.SugOrderQty:int = obj["SugOrderQty"]
      """  Suggested Quantity for Order Qty in Quote Detail  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.SubPartSellingFactor:int = obj["SubPartSellingFactor"]
      self.SubPartTrackSerialNum:bool = obj["SubPartTrackSerialNum"]
      self.SubPartTrackDimension:bool = obj["SubPartTrackDimension"]
      self.SubPartPartDescription:str = obj["SubPartPartDescription"]
      self.SubPartIUM:str = obj["SubPartIUM"]
      self.SubPartSalesUM:str = obj["SubPartSalesUM"]
      self.SubPartTrackLots:bool = obj["SubPartTrackLots"]
      self.SubPartPricePerCode:str = obj["SubPartPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAlternatePartTableset:
   def __init__(self, obj):
      self.PartSubs:list[Erp_Tablesets_PartSubsRow] = obj["PartSubs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   subPart
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.subPart:str = obj["subPart"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
      pass

class GetListAlternatePartsForSO_input:
   """ Required : 
   whereClause
   custNum
   shipToNum
   orderDate
   currencyCode
   orderQuantity
   sellingQuantity
   sellingUOM
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.custNum:int = obj["custNum"]
      """  Filter by this CustNum  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Num  """  
      self.orderDate:str = obj["orderDate"]
      """  Order Date  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code  """  
      self.orderQuantity:int = obj["orderQuantity"]
      """  Order Qty  """  
      self.sellingQuantity:int = obj["sellingQuantity"]
      """  Selling Qty  """  
      self.sellingUOM:str = obj["sellingUOM"]
      """  Selling Unit of Measure  """  
      pass

class GetListAlternatePartsForSO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
      pass

class GetListAlternateParts_input:
   """ Required : 
   whereClause
   custNum
   shipToNum
   orderDate
   currencyCode
   orderQuantity
   sellingQuantity
   sellingUOM
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.custNum:int = obj["custNum"]
      """  Filter by this CustNum  """  
      self.shipToNum:str = obj["shipToNum"]
      """  Ship To Num  """  
      self.orderDate:str = obj["orderDate"]
      """  Order Date  """  
      self.currencyCode:str = obj["currencyCode"]
      """  Currency Code  """  
      self.orderQuantity:int = obj["orderQuantity"]
      """  Order Qty  """  
      self.sellingQuantity:int = obj["sellingQuantity"]
      """  Selling Qty  """  
      self.sellingUOM:str = obj["sellingUOM"]
      """  Selling Unit of Measure  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListAlternateParts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_PartSubsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartSubs_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlternatePartTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartSubs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlternatePartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartSubs
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartSubs:str = obj["whereClausePartSubs"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlternatePartTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtAlternatePartTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlternatePartTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlternatePartTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlternatePartTableset] = obj["ds"]
      pass

      """  output parameters  """  

