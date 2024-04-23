import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SkipLotCtlSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SkipLotCtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SkipLotCtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SkipLotCtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SkipLotCtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/SkipLotCtls",headers=creds) as resp:
           return await resp.json()

async def post_SkipLotCtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SkipLotCtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SkipLotCtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SkipLotCtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/SkipLotCtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SkipLotCtls_Company_SkipCode(Company, SkipCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SkipLotCtl item
   Description: Calls GetByID to retrieve the SkipLotCtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SkipLotCtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SkipCode: Desc: SkipCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SkipLotCtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/SkipLotCtls(" + Company + "," + SkipCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SkipLotCtls_Company_SkipCode(Company, SkipCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SkipLotCtl for the service
   Description: Calls UpdateExt to update SkipLotCtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SkipLotCtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SkipCode: Desc: SkipCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SkipLotCtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/SkipLotCtls(" + Company + "," + SkipCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SkipLotCtls_Company_SkipCode(Company, SkipCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SkipLotCtl item
   Description: Call UpdateExt to delete SkipLotCtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SkipLotCtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SkipCode: Desc: SkipCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/SkipLotCtls(" + Company + "," + SkipCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SkipLotCtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSkipLotCtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSkipLotCtl=" + whereClauseSkipLotCtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(skipCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "skipCode=" + skipCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSkipLotCtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSkipLotCtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSkipLotCtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSkipLotCtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSkipLotCtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SkipLotCtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SkipLotCtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SkipLotCtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SkipLotCtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SkipLotCtlRow] = obj["value"]
      pass

class Erp_Tablesets_SkipLotCtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SkipCode:str = obj["SkipCode"]
      """  This is a unique code for the skip lot control information.  """  
      self.Description:str = obj["Description"]
      """  The description of the skip lot code.  """  
      self.InspectLot:int = obj["InspectLot"]
      """  This is the number of lots (receipts) that are to be inspected. The default is 1 and the entry cannot be less than 1.  """  
      self.SkipLots:int = obj["SkipLots"]
      """  This is the number of lots (receipts) that will be skipped, this indicates that receipt does not require to be inspected and can be moved directly to stock.  """  
      self.RepeatLots:int = obj["RepeatLots"]
      """  This is the number of cycles that the system will process before moving to the next pre-determined skip code.  """  
      self.MinCycles:int = obj["MinCycles"]
      """  This is the number of minimum cycles that must have been completed before the skip lot code can move to a cycle that does not inspect as many lots. This field can be set to zero which will force the system to ignore the check.  """  
      self.MaxRejects:int = obj["MaxRejects"]
      """  This is the number of rejects which when reached will force the part to move to a more restrictive inspection cycle. This field can be set to zero which will force the system to ignore the check.  """  
      self.RejectCntBy:str = obj["RejectCntBy"]
      """  Valid options are By Skip Lot or Quantity. The default will be Skip Lot. This field will control the value of what is added to the Reject Count field. If it is set to Skip Lot then the Reject Count will be increased by 1 if the lot being inspected has a rejected quantity, if it is set to quantity then the field will be increased by the total failed quantity.  """  
      self.OnPassSkipCd:str = obj["OnPassSkipCd"]
      """   This is the skip code that the parts will start to used if the number of cycles has been reached or the number of rejects is less than or equal to the Maximum rejects.
If this field is blank then the current cycle will start over again.  """  
      self.OnFailSkipCd:str = obj["OnFailSkipCd"]
      """   This is the skip code that the parts will be moved to if the Maximum number of rejects has been exceeded or the number of cycles is greater than the Minimum Cycle.
If this field is blank then the current cycle will start over again.  """  
      self.UseMaxRejects:bool = obj["UseMaxRejects"]
      """  Indicates whether the MaxRejects value is to be used to determine when a part moves to a less restrivtive inspection. This is required so that MaxRejects = 0 will ensure that 0 failures are required.  """  
      self.GlobalSkipLotCtl:bool = obj["GlobalSkipLotCtl"]
      """  Marks this SkipLotCtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SkipLotCtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SkipCode:str = obj["SkipCode"]
      """  This is a unique code for the skip lot control information.  """  
      self.Description:str = obj["Description"]
      """  The description of the skip lot code.  """  
      self.InspectLot:int = obj["InspectLot"]
      """  This is the number of lots (receipts) that are to be inspected. The default is 1 and the entry cannot be less than 1.  """  
      self.SkipLots:int = obj["SkipLots"]
      """  This is the number of lots (receipts) that will be skipped, this indicates that receipt does not require to be inspected and can be moved directly to stock.  """  
      self.RepeatLots:int = obj["RepeatLots"]
      """  This is the number of cycles that the system will process before moving to the next pre-determined skip code.  """  
      self.MinCycles:int = obj["MinCycles"]
      """  This is the number of minimum cycles that must have been completed before the skip lot code can move to a cycle that does not inspect as many lots. This field can be set to zero which will force the system to ignore the check.  """  
      self.MaxRejects:int = obj["MaxRejects"]
      """  This is the number of rejects which when reached will force the part to move to a more restrictive inspection cycle. This field can be set to zero which will force the system to ignore the check.  """  
      self.RejectCntBy:str = obj["RejectCntBy"]
      """  Valid options are By Skip Lot or Quantity. The default will be Skip Lot. This field will control the value of what is added to the Reject Count field. If it is set to Skip Lot then the Reject Count will be increased by 1 if the lot being inspected has a rejected quantity, if it is set to quantity then the field will be increased by the total failed quantity.  """  
      self.OnPassSkipCd:str = obj["OnPassSkipCd"]
      """   This is the skip code that the parts will start to used if the number of cycles has been reached or the number of rejects is less than or equal to the Maximum rejects.
If this field is blank then the current cycle will start over again.  """  
      self.OnFailSkipCd:str = obj["OnFailSkipCd"]
      """   This is the skip code that the parts will be moved to if the Maximum number of rejects has been exceeded or the number of cycles is greater than the Minimum Cycle.
If this field is blank then the current cycle will start over again.  """  
      self.UseMaxRejects:bool = obj["UseMaxRejects"]
      """  Indicates whether the MaxRejects value is to be used to determine when a part moves to a less restrivtive inspection. This is required so that MaxRejects = 0 will ensure that 0 failures are required.  """  
      self.GlobalSkipLotCtl:bool = obj["GlobalSkipLotCtl"]
      """  Marks this SkipLotCtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
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
   skipCode
   """  
   def __init__(self, obj):
      self.skipCode:str = obj["skipCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SkipLotCtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SkipCode:str = obj["SkipCode"]
      """  This is a unique code for the skip lot control information.  """  
      self.Description:str = obj["Description"]
      """  The description of the skip lot code.  """  
      self.InspectLot:int = obj["InspectLot"]
      """  This is the number of lots (receipts) that are to be inspected. The default is 1 and the entry cannot be less than 1.  """  
      self.SkipLots:int = obj["SkipLots"]
      """  This is the number of lots (receipts) that will be skipped, this indicates that receipt does not require to be inspected and can be moved directly to stock.  """  
      self.RepeatLots:int = obj["RepeatLots"]
      """  This is the number of cycles that the system will process before moving to the next pre-determined skip code.  """  
      self.MinCycles:int = obj["MinCycles"]
      """  This is the number of minimum cycles that must have been completed before the skip lot code can move to a cycle that does not inspect as many lots. This field can be set to zero which will force the system to ignore the check.  """  
      self.MaxRejects:int = obj["MaxRejects"]
      """  This is the number of rejects which when reached will force the part to move to a more restrictive inspection cycle. This field can be set to zero which will force the system to ignore the check.  """  
      self.RejectCntBy:str = obj["RejectCntBy"]
      """  Valid options are By Skip Lot or Quantity. The default will be Skip Lot. This field will control the value of what is added to the Reject Count field. If it is set to Skip Lot then the Reject Count will be increased by 1 if the lot being inspected has a rejected quantity, if it is set to quantity then the field will be increased by the total failed quantity.  """  
      self.OnPassSkipCd:str = obj["OnPassSkipCd"]
      """   This is the skip code that the parts will start to used if the number of cycles has been reached or the number of rejects is less than or equal to the Maximum rejects.
If this field is blank then the current cycle will start over again.  """  
      self.OnFailSkipCd:str = obj["OnFailSkipCd"]
      """   This is the skip code that the parts will be moved to if the Maximum number of rejects has been exceeded or the number of cycles is greater than the Minimum Cycle.
If this field is blank then the current cycle will start over again.  """  
      self.UseMaxRejects:bool = obj["UseMaxRejects"]
      """  Indicates whether the MaxRejects value is to be used to determine when a part moves to a less restrivtive inspection. This is required so that MaxRejects = 0 will ensure that 0 failures are required.  """  
      self.GlobalSkipLotCtl:bool = obj["GlobalSkipLotCtl"]
      """  Marks this SkipLotCtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SkipLotCtlListTableset:
   def __init__(self, obj):
      self.SkipLotCtlList:list[Erp_Tablesets_SkipLotCtlListRow] = obj["SkipLotCtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SkipLotCtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SkipCode:str = obj["SkipCode"]
      """  This is a unique code for the skip lot control information.  """  
      self.Description:str = obj["Description"]
      """  The description of the skip lot code.  """  
      self.InspectLot:int = obj["InspectLot"]
      """  This is the number of lots (receipts) that are to be inspected. The default is 1 and the entry cannot be less than 1.  """  
      self.SkipLots:int = obj["SkipLots"]
      """  This is the number of lots (receipts) that will be skipped, this indicates that receipt does not require to be inspected and can be moved directly to stock.  """  
      self.RepeatLots:int = obj["RepeatLots"]
      """  This is the number of cycles that the system will process before moving to the next pre-determined skip code.  """  
      self.MinCycles:int = obj["MinCycles"]
      """  This is the number of minimum cycles that must have been completed before the skip lot code can move to a cycle that does not inspect as many lots. This field can be set to zero which will force the system to ignore the check.  """  
      self.MaxRejects:int = obj["MaxRejects"]
      """  This is the number of rejects which when reached will force the part to move to a more restrictive inspection cycle. This field can be set to zero which will force the system to ignore the check.  """  
      self.RejectCntBy:str = obj["RejectCntBy"]
      """  Valid options are By Skip Lot or Quantity. The default will be Skip Lot. This field will control the value of what is added to the Reject Count field. If it is set to Skip Lot then the Reject Count will be increased by 1 if the lot being inspected has a rejected quantity, if it is set to quantity then the field will be increased by the total failed quantity.  """  
      self.OnPassSkipCd:str = obj["OnPassSkipCd"]
      """   This is the skip code that the parts will start to used if the number of cycles has been reached or the number of rejects is less than or equal to the Maximum rejects.
If this field is blank then the current cycle will start over again.  """  
      self.OnFailSkipCd:str = obj["OnFailSkipCd"]
      """   This is the skip code that the parts will be moved to if the Maximum number of rejects has been exceeded or the number of cycles is greater than the Minimum Cycle.
If this field is blank then the current cycle will start over again.  """  
      self.UseMaxRejects:bool = obj["UseMaxRejects"]
      """  Indicates whether the MaxRejects value is to be used to determine when a part moves to a less restrivtive inspection. This is required so that MaxRejects = 0 will ensure that 0 failures are required.  """  
      self.GlobalSkipLotCtl:bool = obj["GlobalSkipLotCtl"]
      """  Marks this SkipLotCtl as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SkipLotCtlTableset:
   def __init__(self, obj):
      self.SkipLotCtl:list[Erp_Tablesets_SkipLotCtlRow] = obj["SkipLotCtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSkipLotCtlTableset:
   def __init__(self, obj):
      self.SkipLotCtl:list[Erp_Tablesets_SkipLotCtlRow] = obj["SkipLotCtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   skipCode
   """  
   def __init__(self, obj):
      self.skipCode:str = obj["skipCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SkipLotCtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SkipLotCtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SkipLotCtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SkipLotCtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSkipLotCtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SkipLotCtlTableset] = obj["ds"]
      pass

class GetNewSkipLotCtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SkipLotCtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSkipLotCtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSkipLotCtl:str = obj["whereClauseSkipLotCtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SkipLotCtlTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtSkipLotCtlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSkipLotCtlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SkipLotCtlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SkipLotCtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

