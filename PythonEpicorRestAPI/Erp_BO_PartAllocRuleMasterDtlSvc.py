import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartAllocRuleMasterDtlSvc
# Description: PartAllocRuleMasterDtlSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleMasterDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAllocRuleMasterDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleMasterDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleMasterDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls",headers=creds) as resp:
           return await resp.json()

async def post_PartAllocRuleMasterDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleMasterDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleMasterDtls_Company_MasterRuleID(Company, MasterRuleID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAllocRuleMasterDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleMasterDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MasterRuleID: Desc: MasterRuleID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartAllocRuleMasterDtls_Company_MasterRuleID(Company, MasterRuleID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartAllocRuleMasterDtl for the service
   Description: Calls UpdateExt to update PartAllocRuleMasterDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MasterRuleID: Desc: MasterRuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleMasterDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartAllocRuleMasterDtls_Company_MasterRuleID(Company, MasterRuleID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartAllocRuleMasterDtl item
   Description: Call UpdateExt to delete PartAllocRuleMasterDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleMasterDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MasterRuleID: Desc: MasterRuleID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/PartAllocRuleMasterDtls(" + Company + "," + MasterRuleID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleMasterDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartAllocRuleMasterDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartAllocRuleMasterDtl=" + whereClausePartAllocRuleMasterDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(masterRuleID, epicorHeaders = None):
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
   params += "masterRuleID=" + masterRuleID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CopyPartAllocRuleMasterDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyPartAllocRuleMasterDtl
   Description: Copies the Master Rule to a new record
   OperationID: CopyPartAllocRuleMasterDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyPartAllocRuleMasterDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyPartAllocRuleMasterDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAction
   Description: Invoked when Action is changed.
   OperationID: OnChangeAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAllocTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAllocTemplate
   Description: Invoked when AllocTemplateID is changed.
   OperationID: OnChangeAllocTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllocTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllocTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQueryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQueryID
   Description: Invoked when QueryID is changed.  Query must have PartAllocQueueInfo as its first table.
   OperationID: OnChangeQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartAllocRuleMasterDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartAllocRuleMasterDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleMasterDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleMasterDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleMasterDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleMasterDtlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocRuleMasterDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleMasterDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocRuleMasterDtlRow] = obj["value"]
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Unique ID of Master Rule.  """  
      self.Description:str = obj["Description"]
      """  Description of the rule.  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Unique ID of Master Rule.  """  
      self.Description:str = obj["Description"]
      """  Description of the rule.  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule.  """  
      self.RuleCalcFulfillOnSearch:bool = obj["RuleCalcFulfillOnSearch"]
      """  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  """  
      self.RuleUseDemandWhseOnly:bool = obj["RuleUseDemandWhseOnly"]
      """  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  """  
      self.RuleLimitedRefresh:bool = obj["RuleLimitedRefresh"]
      """  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  DevCharacter01  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  DevDecimal01  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  DevBoolean01  """  
      self.DevDate01:str = obj["DevDate01"]
      """  DevDate01  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocDemandType:str = obj["AllocDemandType"]
      """  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  """  
      self.EnableAllocTemplateID:bool = obj["EnableAllocTemplateID"]
      """  Indicates if the AllocationTemplate field should be enabled  """  
      self.EnableFormula:bool = obj["EnableFormula"]
      """  Indicates if the user is able to enter a formula  """  
      self.EnableQueryID:bool = obj["EnableQueryID"]
      """  Indicates if the QueryID field should be enabled  """  
      self.RuleInUse:bool = obj["RuleInUse"]
      """  Flag indicating if there are any synchronized rules linked to this master rule  """  
      self.ActiveSysTaskExists:bool = obj["ActiveSysTaskExists"]
      """  Indicates if an Active SysTask exists for this rule class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartAllocTemplateAllocTemplateDesc:str = obj["PartAllocTemplateAllocTemplateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CopyPartAllocRuleMasterDtl_input:
   """ Required : 
   masterRuleID
   ds
   """  
   def __init__(self, obj):
      self.masterRuleID:str = obj["masterRuleID"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class CopyPartAllocRuleMasterDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   masterRuleID
   """  
   def __init__(self, obj):
      self.masterRuleID:str = obj["masterRuleID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Unique ID of Master Rule.  """  
      self.Description:str = obj["Description"]
      """  Description of the rule.  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlListTableset:
   def __init__(self, obj):
      self.PartAllocRuleMasterDtlList:list[Erp_Tablesets_PartAllocRuleMasterDtlListRow] = obj["PartAllocRuleMasterDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Unique ID of Master Rule.  """  
      self.Description:str = obj["Description"]
      """  Description of the rule.  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo.  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule.  """  
      self.RuleCalcFulfillOnSearch:bool = obj["RuleCalcFulfillOnSearch"]
      """  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  """  
      self.RuleUseDemandWhseOnly:bool = obj["RuleUseDemandWhseOnly"]
      """  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  """  
      self.RuleLimitedRefresh:bool = obj["RuleLimitedRefresh"]
      """  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  DevCharacter01  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  DevDecimal01  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  DevBoolean01  """  
      self.DevDate01:str = obj["DevDate01"]
      """  DevDate01  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocDemandType:str = obj["AllocDemandType"]
      """  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  """  
      self.EnableAllocTemplateID:bool = obj["EnableAllocTemplateID"]
      """  Indicates if the AllocationTemplate field should be enabled  """  
      self.EnableFormula:bool = obj["EnableFormula"]
      """  Indicates if the user is able to enter a formula  """  
      self.EnableQueryID:bool = obj["EnableQueryID"]
      """  Indicates if the QueryID field should be enabled  """  
      self.RuleInUse:bool = obj["RuleInUse"]
      """  Flag indicating if there are any synchronized rules linked to this master rule  """  
      self.ActiveSysTaskExists:bool = obj["ActiveSysTaskExists"]
      """  Indicates if an Active SysTask exists for this rule class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartAllocTemplateAllocTemplateDesc:str = obj["PartAllocTemplateAllocTemplateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleMasterDtlTableset:
   def __init__(self, obj):
      self.PartAllocRuleMasterDtl:list[Erp_Tablesets_PartAllocRuleMasterDtlRow] = obj["PartAllocRuleMasterDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset:
   def __init__(self, obj):
      self.PartAllocRuleMasterDtl:list[Erp_Tablesets_PartAllocRuleMasterDtlRow] = obj["PartAllocRuleMasterDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   masterRuleID
   """  
   def __init__(self, obj):
      self.masterRuleID:str = obj["masterRuleID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocRuleMasterDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartAllocRuleMasterDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class GetNewPartAllocRuleMasterDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartAllocRuleMasterDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartAllocRuleMasterDtl:str = obj["whereClausePartAllocRuleMasterDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["returnObj"]
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

class OnChangeAction_input:
   """ Required : 
   newAction
   checkForWarnings
   ds
   """  
   def __init__(self, obj):
      self.newAction:str = obj["newAction"]
      self.checkForWarnings:bool = obj["checkForWarnings"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class OnChangeAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAllocTemplate_input:
   """ Required : 
   newAllocTemplateID
   ds
   """  
   def __init__(self, obj):
      self.newAllocTemplateID:str = obj["newAllocTemplateID"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class OnChangeAllocTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQueryID_input:
   """ Required : 
   newQueryID
   checkForWarnings
   ds
   """  
   def __init__(self, obj):
      self.newQueryID:str = obj["newQueryID"]
      self.checkForWarnings:bool = obj["checkForWarnings"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class OnChangeQueryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocRuleMasterDtlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleMasterDtlTableset] = obj["ds"]
      pass

      """  output parameters  """  

