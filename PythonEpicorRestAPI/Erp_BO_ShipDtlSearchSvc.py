import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ShipDtlSearchSvc
# Description: Packing Slip Line Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_ShipDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipDtlSearches_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipDtlSearch item
   Description: Calls GetByID to retrieve the ShipDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipDtlSearches_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipDtlSearch for the service
   Description: Calls UpdateExt to update ShipDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipDtlSearches_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipDtlSearch item
   Description: Call UpdateExt to delete ShipDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/ShipDtlSearches(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShipDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseShipDtl=" + whereClauseShipDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(packNum, packLine, epicorHeaders = None):
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
   params += "packNum=" + packNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packLine=" + packLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListCase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCase
   Description: Calls the normal GetList method and then constructs a custom data set combining Hed/Dtl fields for the case entry.
   OperationID: GetListCase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the contact tracker.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then constructs a custom data set combining Hed/Dtl fields for the customer tracker.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipDtlRow] = obj["value"]
      pass

class Erp_Tablesets_ShipDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.RequestDate:str = obj["RequestDate"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.WhseList:str = obj["WhseList"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.PartCompany:str = obj["PartCompany"]
      self.PartPartNum:str = obj["PartPartNum"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.PONum:str = obj["PONum"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.LineTax:int = obj["LineTax"]
      self.DocLineTax:int = obj["DocLineTax"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.MFCustID:str = obj["MFCustID"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      """  Optional lot number description.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      """  Country name  """  
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
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
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      """  Description.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.AllowedOvers:int = obj["AllowedOvers"]
      """  AllowedOvers  """  
      self.AllowedUnders:int = obj["AllowedUnders"]
      """  AllowedUnders  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NotAllocatedQty:int = obj["NotAllocatedQty"]
      """  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.UseShipDtlInfo:bool = obj["UseShipDtlInfo"]
      """  For future use.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  PkgCodePartNum  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  CustContainerPartNum  """  
      self.LabelType:str = obj["LabelType"]
      """  LabelType  """  
      self.WarrantySendToFSA:bool = obj["WarrantySendToFSA"]
      """  Indicates that the warranty will be sent to FSA  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryNumberOfPieces:int = obj["InventoryNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurInventoryShipQty.  """  
      self.JobNumberOfPieces:int = obj["JobNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurJobShipQty.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.JobNotAllocatedQty:int = obj["JobNotAllocatedQty"]
      """  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  """  
      self.JobPickedAutoAllocatedQty:int = obj["JobPickedAutoAllocatedQty"]
      """  Quantity picked from manufacturing that was not manually allocated.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DocLineTax:int = obj["DocLineTax"]
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.EnableInvIDBtn:bool = obj["EnableInvIDBtn"]
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.EnableKitIDBtn:bool = obj["EnableKitIDBtn"]
      self.EnableMfgIDBtn:bool = obj["EnableMfgIDBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnableOBInvSerialBtn:bool = obj["EnableOBInvSerialBtn"]
      self.EnableOBMfgSerialBtn:bool = obj["EnableOBMfgSerialBtn"]
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      self.GetLocIDNum:bool = obj["GetLocIDNum"]
      """  Equal to true if opening Location ID Diaglog  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.LineTax:int = obj["LineTax"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartCompany:str = obj["PartCompany"]
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartPartNum:str = obj["PartPartNum"]
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.PONum:str = obj["PONum"]
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.RequestDate:str = obj["RequestDate"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.SelectedLocationIDQty:int = obj["SelectedLocationIDQty"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.TrackID:bool = obj["TrackID"]
      self.TranLocationIDQty:int = obj["TranLocationIDQty"]
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.WhseList:str = obj["WhseList"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      """  Mark For address formatted for kinetic.  """  
      self.DispInventoryNumberOfPieces:int = obj["DispInventoryNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispJobNumberOfPieces:int = obj["DispJobNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.KitRevisionNum:str = obj["KitRevisionNum"]
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OrderLineProdCode:str = obj["OrderLineProdCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumPSCurrCode:str = obj["OrderNumPSCurrCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PackNumUseOTS:bool = obj["PackNumUseOTS"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumWarrantyCode:str = obj["PartNumWarrantyCode"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarrantyCodeSendToFSA:bool = obj["WarrantyCodeSendToFSA"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PCID2_c:str = obj["PCID2_c"]
      self.PCID3_c:str = obj["PCID3_c"]
      self.PCID4_c:str = obj["PCID4_c"]
      self.PCID5_c:str = obj["PCID5_c"]
      self.PCIDType1_c:str = obj["PCIDType1_c"]
      self.PCIDType2_c:str = obj["PCIDType2_c"]
      self.PCIDType3_c:str = obj["PCIDType3_c"]
      self.PCIDType4_c:str = obj["PCIDType4_c"]
      self.PCIDType5_c:str = obj["PCIDType5_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ShipDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.RequestDate:str = obj["RequestDate"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.WhseList:str = obj["WhseList"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.PartCompany:str = obj["PartCompany"]
      self.PartPartNum:str = obj["PartPartNum"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.PONum:str = obj["PONum"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.LineTax:int = obj["LineTax"]
      self.DocLineTax:int = obj["DocLineTax"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.MFCustID:str = obj["MFCustID"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      """  Optional lot number description.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      """  Country name  """  
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
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
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      """  Description.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipDtlListTableset:
   def __init__(self, obj):
      self.ShipDtlList:list[Erp_Tablesets_ShipDtlListRow] = obj["ShipDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand.  This quantity is in the IUM unit of measure.  """  
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This quantity is in the IUM unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped. Defaulted from OrderRel.JobNum.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if this shipment line item will be invoiced for time and materials. This is not maintainable from within shipment entry. It is duplicated from the OrderDtl.TMBilling. The "Get Shipments" function of Invoice Entry uses this flag to automatically create invoices in a "On Hold" status. The idea is that these type of invoices need to be generated to act as a method of tracking invoice requirements, but they cannot yet be invoiced until all the costs are known. At which time the user will enter the appropriate charges, take it off "Hold" and complete the billing process.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  A flag which indicates "invoicing" status. This is a mirror image of ShipHead.Invoiced field. See ShipHead.Invoiced for further info.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is for Inventory Shipments.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates if the Packing Slip is complete and ready for invoicing.  This is a mirror image of ShipHead.ReadyToInvoice.  """  
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      """  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  """  
      self.SellingJobShipQty:int = obj["SellingJobShipQty"]
      """  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The packline of the kit parent  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      """  Unit of Measure of the quantity shipped from Inventory (OurInventoryShipQty). Must be a valid UOM. If Part is Multi-UOM tracking then only the Tracking UOMs are valid otherwise all UOM's of the Parts UOMClass are valid.  """  
      self.JobShipUOM:str = obj["JobShipUOM"]
      """  Unit of Measure of the quantity shipped from the Job (OurJobShipQty)  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates whether the ShipDtl.PartNum is serial tracked. Required as a db field rather than using the link to PartNumTrackSerialNum to allow validations based on the ShipDtl table rather than the ttShipDtl table. Default is No.  """  
      self.JobLotNum:str = obj["JobLotNum"]
      """  Lot Number is for Job Shipments.  """  
      self.BinType:str = obj["BinType"]
      """  Identifies the type of Bin is being used (valid values are 'Std', 'Cust', 'Supp').  Associated with field ShipDtl.BinNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Order.  This quantity is in the IUM unit of measure.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InDiscount:int = obj["InDiscount"]
      """  A flat discount amount for the line item includes taxes.  It can be zero.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  A flat discount amount for the line item includes taxes.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  The ShipTo ID to be used for this record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.AllowedOvers:int = obj["AllowedOvers"]
      """  AllowedOvers  """  
      self.AllowedUnders:int = obj["AllowedUnders"]
      """  AllowedUnders  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NotAllocatedQty:int = obj["NotAllocatedQty"]
      """  This is the quantity being shipped that was not already previously allocated, and could not be auto allocated.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.UseShipDtlInfo:bool = obj["UseShipDtlInfo"]
      """  For future use.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  PkgCodePartNum  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  CustContainerPartNum  """  
      self.LabelType:str = obj["LabelType"]
      """  LabelType  """  
      self.WarrantySendToFSA:bool = obj["WarrantySendToFSA"]
      """  Indicates that the warranty will be sent to FSA  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the shipment line is marked as "send as equipment", it will create an Installation in Epicor FSA.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryNumberOfPieces:int = obj["InventoryNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurInventoryShipQty.  """  
      self.JobNumberOfPieces:int = obj["JobNumberOfPieces"]
      """  Number of pieces for this attribute set based on OurJobShipQty.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.JobNotAllocatedQty:int = obj["JobNotAllocatedQty"]
      """  This is the quantity being shipped from manufacturing that was not already previously allocated, and could not be auto allocated.  """  
      self.JobPickedAutoAllocatedQty:int = obj["JobPickedAutoAllocatedQty"]
      """  Quantity picked from manufacturing that was not manually allocated.  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Flag to indicate if Order/Line/Rel is Buy To Order  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DimCodeList:str = obj["DimCodeList"]
      """  Delimited list of available Dimension codes for line  """  
      self.DisplayInvQty:int = obj["DisplayInvQty"]
      """  OurInventoryShipQty * DimConvFactor - update inplace of OurInventoryShipQty  """  
      self.DocLineTax:int = obj["DocLineTax"]
      self.DropShip:bool = obj["DropShip"]
      """  Is Drop Shipment.  """  
      self.DtlError:bool = obj["DtlError"]
      """  Indicates if a detail line has errors to be corrected before leaving packing slip  """  
      self.EnableInvIDBtn:bool = obj["EnableInvIDBtn"]
      self.EnableInvSerialBtn:bool = obj["EnableInvSerialBtn"]
      self.EnableJobFields:bool = obj["EnableJobFields"]
      """  Logical indicating if receipt to a job is allowed.  This is determined by either the xasyst.shipnojob field or whether or not the sales order is linked to a job.  """  
      self.EnableKitIDBtn:bool = obj["EnableKitIDBtn"]
      self.EnableMfgIDBtn:bool = obj["EnableMfgIDBtn"]
      self.EnableMfgSerialBtn:bool = obj["EnableMfgSerialBtn"]
      self.EnableOBInvSerialBtn:bool = obj["EnableOBInvSerialBtn"]
      self.EnableOBMfgSerialBtn:bool = obj["EnableOBMfgSerialBtn"]
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.ExtJobNum:str = obj["ExtJobNum"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      self.FSAInstallationOrderLine:int = obj["FSAInstallationOrderLine"]
      self.FSAInstallationOrderNum:int = obj["FSAInstallationOrderNum"]
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      self.GetLocIDNum:bool = obj["GetLocIDNum"]
      """  Equal to true if opening Location ID Diaglog  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      """  The invoice legal number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  External field to be used in the SalesOrder Tracker to show the user the InvoiceNum linked to the shipment.  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      self.KitBinNum:str = obj["KitBinNum"]
      self.KitCompIssue:bool = obj["KitCompIssue"]
      self.KitCompShipComplete:bool = obj["KitCompShipComplete"]
      self.KitDescription:str = obj["KitDescription"]
      self.KitFlag:str = obj["KitFlag"]
      """  Sales Kit flag.  C = 'Component'  P = 'Parent'.  """  
      self.KitIUM:str = obj["KitIUM"]
      self.KitLotNum:str = obj["KitLotNum"]
      self.KitMassIssue:bool = obj["KitMassIssue"]
      self.KitParentIssue:bool = obj["KitParentIssue"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.KitQtyFromInv:int = obj["KitQtyFromInv"]
      self.KitQtyFromInvEnabled:bool = obj["KitQtyFromInvEnabled"]
      self.KitSerialTracked:bool = obj["KitSerialTracked"]
      self.KitTrackLots:bool = obj["KitTrackLots"]
      self.KitWarehouse:str = obj["KitWarehouse"]
      self.KitWarehouseCodeDesc:str = obj["KitWarehouseCodeDesc"]
      self.KitWhseList:str = obj["KitWhseList"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.   This field comes directly from the table ShipHead.  """  
      self.LineContentValue:int = obj["LineContentValue"]
      """  Individual line content value that is used by the freight web service to calculate the total order value.  """  
      self.LineTax:int = obj["LineTax"]
      self.LinkMsg:str = obj["LinkMsg"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderHold:bool = obj["OrderHold"]
      """  Indicates if Order is on Hold  """  
      self.OrderRelOurReqQty:int = obj["OrderRelOurReqQty"]
      self.OurJobShipIUM:str = obj["OurJobShipIUM"]
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      self.OurRemainQty:int = obj["OurRemainQty"]
      self.OurRemainUM:str = obj["OurRemainUM"]
      self.OurReqQty:int = obj["OurReqQty"]
      self.OurReqUM:str = obj["OurReqUM"]
      self.OurShippedQty:int = obj["OurShippedQty"]
      self.OurShippedUM:str = obj["OurShippedUM"]
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      self.PackSlip:str = obj["PackSlip"]
      """  Packing slip for drop shipment.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by freight web service  """  
      self.PartCompany:str = obj["PartCompany"]
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freight web service  """  
      self.PartPartNum:str = obj["PartPartNum"]
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by freight web service  """  
      self.PONum:str = obj["PONum"]
      self.ProjectID:str = obj["ProjectID"]
      """  Project of the related Order Line  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.RequestDate:str = obj["RequestDate"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.SelectedLocationIDQty:int = obj["SelectedLocationIDQty"]
      self.SellingRemainQty:int = obj["SellingRemainQty"]
      self.SellingRemainUM:str = obj["SellingRemainUM"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.SellingReqUM:str = obj["SellingReqUM"]
      self.SellingShipmentQty:int = obj["SellingShipmentQty"]
      self.SellingShipmentUM:str = obj["SellingShipmentUM"]
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      self.SellingShippedUM:str = obj["SellingShippedUM"]
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  """  
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  This field comes directly from the ShipHead table.  """  
      self.StockPart:bool = obj["StockPart"]
      """  Indicates if Part is a stock Part  """  
      self.TrackID:bool = obj["TrackID"]
      self.TranLocationIDQty:int = obj["TranLocationIDQty"]
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.WhseList:str = obj["WhseList"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      """  Mark For address formatted for kinetic.  """  
      self.DispInventoryNumberOfPieces:int = obj["DispInventoryNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DispJobNumberOfPieces:int = obj["DispJobNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.KitRevisionNum:str = obj["KitRevisionNum"]
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumSendToFSA:bool = obj["CustNumSendToFSA"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DimensionDimCodeDescription:str = obj["DimensionDimCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.LotPartLotDescription:str = obj["LotPartLotDescription"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OrderLineProdCode:str = obj["OrderLineProdCode"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumPSCurrCode:str = obj["OrderNumPSCurrCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PackNumUseOTS:bool = obj["PackNumUseOTS"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSendToFSA:bool = obj["PartNumSendToFSA"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumWarrantyCode:str = obj["PartNumWarrantyCode"]
      self.PartNumFSAEquipment:bool = obj["PartNumFSAEquipment"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PlantName:str = obj["PlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WarrantyCodeSendToFSA:bool = obj["WarrantyCodeSendToFSA"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WIPWarehouseCodeDescription:str = obj["WIPWarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.PCID2_c:str = obj["PCID2_c"]
      self.PCID3_c:str = obj["PCID3_c"]
      self.PCID4_c:str = obj["PCID4_c"]
      self.PCID5_c:str = obj["PCID5_c"]
      self.PCIDType1_c:str = obj["PCIDType1_c"]
      self.PCIDType2_c:str = obj["PCIDType2_c"]
      self.PCIDType3_c:str = obj["PCIDType3_c"]
      self.PCIDType4_c:str = obj["PCIDType4_c"]
      self.PCIDType5_c:str = obj["PCIDType5_c"]
      pass

class Erp_Tablesets_ShipDtlSearchTableset:
   def __init__(self, obj):
      self.ShipDtl:list[Erp_Tablesets_ShipDtlRow] = obj["ShipDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtShipDtlSearchTableset:
   def __init__(self, obj):
      self.ShipDtl:list[Erp_Tablesets_ShipDtlRow] = obj["ShipDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
      pass

class GetListCase_input:
   """ Required : 
   whereClauseShipDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListCase_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipDtlListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewShipDtl_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseShipDtl
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.contactName:str = obj["contactName"]
      """  Contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseShipDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      """  Whereclause for ShipDtl table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShipDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipDtl:str = obj["whereClauseShipDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtShipDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShipDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

