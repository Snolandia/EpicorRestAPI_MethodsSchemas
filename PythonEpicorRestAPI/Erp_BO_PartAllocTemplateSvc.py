import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartAllocTemplateSvc
# Description: PartAllocationTemplate Entry
            A PartAllocTemplate record serves as an entry to define parameters used for the
            algorithm that searches for available inventory throughout the warehouse.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocTemplates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAllocTemplates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocTemplates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocTemplateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates",headers=creds) as resp:
           return await resp.json()

async def post_PartAllocTemplates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocTemplates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartAllocTemplates_Company_AllocTemplateID(Company, AllocTemplateID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAllocTemplate item
   Description: Calls GetByID to retrieve the PartAllocTemplate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocTemplate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocTemplateID: Desc: AllocTemplateID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartAllocTemplates_Company_AllocTemplateID(Company, AllocTemplateID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartAllocTemplate for the service
   Description: Calls UpdateExt to update PartAllocTemplate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocTemplate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocTemplateID: Desc: AllocTemplateID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocTemplateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartAllocTemplates_Company_AllocTemplateID(Company, AllocTemplateID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartAllocTemplate item
   Description: Call UpdateExt to delete PartAllocTemplate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocTemplate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocTemplateID: Desc: AllocTemplateID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/PartAllocTemplates(" + Company + "," + AllocTemplateID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocTemplateListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartAllocTemplate, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartAllocTemplate=" + whereClausePartAllocTemplate
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(allocTemplateID, epicorHeaders = None):
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
   params += "allocTemplateID=" + allocTemplateID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetWhseTeamUserList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWhseTeamUserList
   Description: Returns the list of all employees from Database Table WhseGroupEmp
   OperationID: GetWhseTeamUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhseTeamUserList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseTeamUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEmpID
   Description: Call this method when User Assignment is changed.
   OperationID: OnChangeEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseTeam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseTeam
   Description: Call this method when the user changes team whse group.
   OperationID: OnChangeWhseTeam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseTeam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseTeam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartalloctemplateCheckAllocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartalloctemplateCheckAllocType
   Description: Checks PartAllocType code entered
   OperationID: PartalloctemplateCheckAllocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartalloctemplateCheckAllocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartalloctemplateCheckAllocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartAllocTemplateCheckDemandType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartAllocTemplateCheckDemandType
   Description: Checks Part Alloc Demand Type code entered
   OperationID: PartAllocTemplateCheckDemandType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartAllocTemplateCheckDemandType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartAllocTemplateCheckDemandType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartAllocTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartAllocTemplate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocTemplateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocTemplateListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocTemplateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocTemplateRow] = obj["value"]
      pass

class Erp_Tablesets_PartAllocTemplateListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Part Allocation Template Identifier.  """  
      self.AllocTemplateDesc:str = obj["AllocTemplateDesc"]
      """  Part Allocation Template Description  """  
      self.AllocType:str = obj["AllocType"]
      """  Allocation Type.  Valid values:  Order or Wave.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.DemandType:str = obj["DemandType"]
      """  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.WarehouseCodeForwardStage:str = obj["WarehouseCodeForwardStage"]
      """  User defined warehouse destination.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Replenishable:bool = obj["Replenishable"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.WhseCodeFwdStageDescDescription:str = obj["WhseCodeFwdStageDescDescription"]
      """  Description.  """  
      self.WhseGroupWhseGroupDesc:str = obj["WhseGroupWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.WhseZoneZoneDesc:str = obj["WhseZoneZoneDesc"]
      """  Mandatory  """  
      self.WhseZoneFwdStageZoneDesc:str = obj["WhseZoneFwdStageZoneDesc"]
      """  Mandatory  """  
      self.WorkstationDescription:str = obj["WorkstationDescription"]
      """  Description of the station  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocTemplateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Part Allocation Template Identifier.  """  
      self.AllocTemplateDesc:str = obj["AllocTemplateDesc"]
      """  Part Allocation Template Description  """  
      self.AllocType:str = obj["AllocType"]
      """  Allocation Type.  Valid values:  Order or Wave.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.DemandType:str = obj["DemandType"]
      """  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.WarehouseCodeForwardStage:str = obj["WarehouseCodeForwardStage"]
      """  User defined warehouse destination.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WhseDestWarehouseCode:str = obj["WhseDestWarehouseCode"]
      """  Warehouse Destination for the allocated qty.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.Replenishable:bool = obj["Replenishable"]
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.WhseCodeFwdStageDescDescription:str = obj["WhseCodeFwdStageDescDescription"]
      self.WhseGroupWhseGroupDesc:str = obj["WhseGroupWhseGroupDesc"]
      self.WhseZoneZoneDesc:str = obj["WhseZoneZoneDesc"]
      self.WhseZoneFwdStageZoneDesc:str = obj["WhseZoneFwdStageZoneDesc"]
      self.WorkstationDescription:str = obj["WorkstationDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   allocTemplateID
   """  
   def __init__(self, obj):
      self.allocTemplateID:str = obj["allocTemplateID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartAllocTemplateListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Part Allocation Template Identifier.  """  
      self.AllocTemplateDesc:str = obj["AllocTemplateDesc"]
      """  Part Allocation Template Description  """  
      self.AllocType:str = obj["AllocType"]
      """  Allocation Type.  Valid values:  Order or Wave.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.DemandType:str = obj["DemandType"]
      """  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.WarehouseCodeForwardStage:str = obj["WarehouseCodeForwardStage"]
      """  User defined warehouse destination.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Replenishable:bool = obj["Replenishable"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.WhseCodeFwdStageDescDescription:str = obj["WhseCodeFwdStageDescDescription"]
      """  Description.  """  
      self.WhseGroupWhseGroupDesc:str = obj["WhseGroupWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.WhseZoneZoneDesc:str = obj["WhseZoneZoneDesc"]
      """  Mandatory  """  
      self.WhseZoneFwdStageZoneDesc:str = obj["WhseZoneFwdStageZoneDesc"]
      """  Mandatory  """  
      self.WorkstationDescription:str = obj["WorkstationDescription"]
      """  Description of the station  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocTemplateListTableset:
   def __init__(self, obj):
      self.PartAllocTemplateList:list[Erp_Tablesets_PartAllocTemplateListRow] = obj["PartAllocTemplateList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAllocTemplateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Part Allocation Template Identifier.  """  
      self.AllocTemplateDesc:str = obj["AllocTemplateDesc"]
      """  Part Allocation Template Description  """  
      self.AllocType:str = obj["AllocType"]
      """  Allocation Type.  Valid values:  Order or Wave.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.DemandType:str = obj["DemandType"]
      """  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  ID that uniquely Identifies a Zone within a warehouse.  """  
      self.SearchSort:str = obj["SearchSort"]
      """  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type.  Valid values:  Standard, Managed or Both.  """  
      self.BinNumFirstOption:str = obj["BinNumFirstOption"]
      """  The first option for the bin from which to select inventory within the warehouse.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.TransPriority:int = obj["TransPriority"]
      """  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  """  
      self.CrossDocking:bool = obj["CrossDocking"]
      """  True if Cross-Docking is enabled.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.MultiplePartsPerBin:bool = obj["MultiplePartsPerBin"]
      """  True if Multiple Parts Per Bin is allowed.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.BinNumProductionIn:str = obj["BinNumProductionIn"]
      """  The user defined Production In bin number within the warehouse.  """  
      self.ForwardStageGroup:str = obj["ForwardStageGroup"]
      """  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  """  
      self.WarehouseCodeForwardStage:str = obj["WarehouseCodeForwardStage"]
      """  User defined warehouse destination.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WhseDestWarehouseCode:str = obj["WhseDestWarehouseCode"]
      """  Warehouse Destination for the allocated qty.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.Replenishable:bool = obj["Replenishable"]
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.WhseCodeFwdStageDescDescription:str = obj["WhseCodeFwdStageDescDescription"]
      self.WhseGroupWhseGroupDesc:str = obj["WhseGroupWhseGroupDesc"]
      self.WhseZoneZoneDesc:str = obj["WhseZoneZoneDesc"]
      self.WhseZoneFwdStageZoneDesc:str = obj["WhseZoneFwdStageZoneDesc"]
      self.WorkstationDescription:str = obj["WorkstationDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocTemplateTableset:
   def __init__(self, obj):
      self.PartAllocTemplate:list[Erp_Tablesets_PartAllocTemplateRow] = obj["PartAllocTemplate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartAllocTemplateTableset:
   def __init__(self, obj):
      self.PartAllocTemplate:list[Erp_Tablesets_PartAllocTemplateRow] = obj["PartAllocTemplate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseTeamUserListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseTeamUserListTableset:
   def __init__(self, obj):
      self.WhseTeamUserList:list[Erp_Tablesets_WhseTeamUserListRow] = obj["WhseTeamUserList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   allocTemplateID
   """  
   def __init__(self, obj):
      self.allocTemplateID:str = obj["allocTemplateID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartAllocTemplateListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartAllocTemplate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class GetNewPartAllocTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartAllocTemplate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartAllocTemplate:str = obj["whereClausePartAllocTemplate"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetWhseTeamUserList_input:
   """ Required : 
   groupCode
   """  
   def __init__(self, obj):
      self.groupCode:str = obj["groupCode"]
      """  Warehouse Group Code.  """  
      pass

class GetWhseTeamUserList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseTeamUserListTableset] = obj["returnObj"]
      pass

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

class OnChangeEmpID_input:
   """ Required : 
   empID
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Proposed value for User Assignment.  """  
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class OnChangeEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseTeam_input:
   """ Required : 
   teamWhse
   ds
   """  
   def __init__(self, obj):
      self.teamWhse:str = obj["teamWhse"]
      """  Proposed value for team whse.  """  
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class OnChangeWhseTeam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PartAllocTemplateCheckDemandType_input:
   """ Required : 
   newPartAllocDemandType
   ds
   """  
   def __init__(self, obj):
      self.newPartAllocDemandType:str = obj["newPartAllocDemandType"]
      """  PartAllocDemandType code entered  """  
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class PartAllocTemplateCheckDemandType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PartalloctemplateCheckAllocType_input:
   """ Required : 
   newPartAllocType
   ds
   """  
   def __init__(self, obj):
      self.newPartAllocType:str = obj["newPartAllocType"]
      """  PartAllocType code entered  """  
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class PartalloctemplateCheckAllocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocTemplateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocTemplateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocTemplateTableset] = obj["ds"]
      pass

      """  output parameters  """  

