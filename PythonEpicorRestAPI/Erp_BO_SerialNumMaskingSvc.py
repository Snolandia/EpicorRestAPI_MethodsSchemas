import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialNumMaskingSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SerialNumMaskings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialNumMaskings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNumMaskings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings",headers=creds) as resp:
           return await resp.json()

async def post_SerialNumMaskings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNumMaskings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialNumMaskings_Company_SerialMaskID(Company, SerialMaskID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialNumMasking item
   Description: Calls GetByID to retrieve the SerialNumMasking item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNumMasking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SerialMaskID: Desc: SerialMaskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialNumMaskings_Company_SerialMaskID(Company, SerialMaskID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialNumMasking for the service
   Description: Calls UpdateExt to update SerialNumMasking. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNumMasking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SerialMaskID: Desc: SerialMaskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialNumMaskings_Company_SerialMaskID(Company, SerialMaskID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialNumMasking item
   Description: Call UpdateExt to delete SerialNumMasking item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNumMasking
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SerialMaskID: Desc: SerialMaskID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMaskListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSerialMask, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSerialMask=" + whereClauseSerialMask
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(serialMaskID, epicorHeaders = None):
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
   params += "serialMaskID=" + serialMaskID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCharactersUsed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCharactersUsed
   Description: Returns number of characters used in serial number.
   OperationID: UpdateCharactersUsed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCharactersUsed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCharactersUsed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfMask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfMask
   Description: TO BE CALLED ON CHANGE OF ttSerialMask.Mask
   OperationID: OnChangeOfMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConstructExampleString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConstructExampleString
   Description: TO BE CALLED ON CHANGE OF ttSerialMask.Mask
   OperationID: ConstructExampleString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConstructExampleString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConstructExampleString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSNLastUsedSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSNLastUsedSeq
   Description: NEEDS TO BE CALLED FOR GENERATE MASK TYPES
   OperationID: OnChangeSNLastUsedSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSNLastUsedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSNLastUsedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialMask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialMask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialMaskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialMaskRow] = obj["value"]
      pass

class Erp_Tablesets_SerialMaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SerialMaskID:str = obj["SerialMaskID"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.Description:str = obj["Description"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.Active:bool = obj["Active"]
      """   Determines if the serial mask can be used in part maintenance.
Default value is yes  """  
      self.MaskType:int = obj["MaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.Mask:str = obj["Mask"]
      """  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  """  
      self.Example:str = obj["Example"]
      """  BL-generated example of the serial number mask that has been defined.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters that serial numbers will use based on the mask entered.  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  """  
      self.GenerateSeqString:str = obj["GenerateSeqString"]
      """  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  """  
      self.GlobalSerialMask:bool = obj["GlobalSerialMask"]
      """  Marks this SerialMask as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  Indicates whether this mask is used in Part or SerialNo  """  
      self.WarnMsg:str = obj["WarnMsg"]
      self.MaskTypeDesc:str = obj["MaskTypeDesc"]
      """  Mask Type Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SerialMaskID:str = obj["SerialMaskID"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.Description:str = obj["Description"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.Active:bool = obj["Active"]
      """   Determines if the serial mask can be used in part maintenance.
Default value is yes  """  
      self.MaskType:int = obj["MaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.Mask:str = obj["Mask"]
      """  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  """  
      self.Example:str = obj["Example"]
      """  BL-generated example of the serial number mask that has been defined.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters that serial numbers will use based on the mask entered.  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  """  
      self.GenerateSeqString:str = obj["GenerateSeqString"]
      """  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  """  
      self.GlobalSerialMask:bool = obj["GlobalSerialMask"]
      """  Marks this SerialMask as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  Indicates whether this mask is used in Part or SerialNo  """  
      self.WarnMsg:str = obj["WarnMsg"]
      self.MaskTypeDesc:str = obj["MaskTypeDesc"]
      """  Mask Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ConstructExampleString_input:
   """ Required : 
   ipMask
   ipPart
   """  
   def __init__(self, obj):
      self.ipMask:str = obj["ipMask"]
      """  SerialMask.Mask  """  
      self.ipPart:str = obj["ipPart"]
      """  Part.PartNum  """  
      pass

class ConstructExampleString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opExampleStr:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   serialMaskID
   """  
   def __init__(self, obj):
      self.serialMaskID:str = obj["serialMaskID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SerialMaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SerialMaskID:str = obj["SerialMaskID"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.Description:str = obj["Description"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.Active:bool = obj["Active"]
      """   Determines if the serial mask can be used in part maintenance.
Default value is yes  """  
      self.MaskType:int = obj["MaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.Mask:str = obj["Mask"]
      """  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  """  
      self.Example:str = obj["Example"]
      """  BL-generated example of the serial number mask that has been defined.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters that serial numbers will use based on the mask entered.  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  """  
      self.GenerateSeqString:str = obj["GenerateSeqString"]
      """  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  """  
      self.GlobalSerialMask:bool = obj["GlobalSerialMask"]
      """  Marks this SerialMask as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  Indicates whether this mask is used in Part or SerialNo  """  
      self.WarnMsg:str = obj["WarnMsg"]
      self.MaskTypeDesc:str = obj["MaskTypeDesc"]
      """  Mask Type Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMaskListTableset:
   def __init__(self, obj):
      self.SerialMaskList:list[Erp_Tablesets_SerialMaskListRow] = obj["SerialMaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialMaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SerialMaskID:str = obj["SerialMaskID"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.Description:str = obj["Description"]
      """  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  """  
      self.Active:bool = obj["Active"]
      """   Determines if the serial mask can be used in part maintenance.
Default value is yes  """  
      self.MaskType:int = obj["MaskType"]
      """   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  """  
      self.Mask:str = obj["Mask"]
      """  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  """  
      self.Example:str = obj["Example"]
      """  BL-generated example of the serial number mask that has been defined.  """  
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters that serial numbers will use based on the mask entered.  """  
      self.PrefixLength:int = obj["PrefixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  """  
      self.SuffixLength:int = obj["SuffixLength"]
      """  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  """  
      self.GenerateSeqString:str = obj["GenerateSeqString"]
      """  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  """  
      self.GlobalSerialMask:bool = obj["GlobalSerialMask"]
      """  Marks this SerialMask as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsUsed:bool = obj["IsUsed"]
      """  Indicates whether this mask is used in Part or SerialNo  """  
      self.WarnMsg:str = obj["WarnMsg"]
      self.MaskTypeDesc:str = obj["MaskTypeDesc"]
      """  Mask Type Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNumMaskingTableset:
   def __init__(self, obj):
      self.SerialMask:list[Erp_Tablesets_SerialMaskRow] = obj["SerialMask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSerialNumMaskingTableset:
   def __init__(self, obj):
      self.SerialMask:list[Erp_Tablesets_SerialMaskRow] = obj["SerialMask"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   serialMaskID
   """  
   def __init__(self, obj):
      self.serialMaskID:str = obj["serialMaskID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialMaskListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSerialMask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

class GetNewSerialMask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSerialMask
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSerialMask:str = obj["whereClauseSerialMask"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["returnObj"]
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

class OnChangeOfMask_input:
   """ Required : 
   ipNewMask
   ipMaskType
   ds
   """  
   def __init__(self, obj):
      self.ipNewMask:str = obj["ipNewMask"]
      """  SerialMask.Mask  """  
      self.ipMaskType:int = obj["ipMaskType"]
      """  SerialMask.MaskType  """  
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

class OnChangeOfMask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarnMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSNLastUsedSeq_input:
   """ Required : 
   ipGenSeqStr
   ipLastUsedSeq
   """  
   def __init__(self, obj):
      self.ipGenSeqStr:str = obj["ipGenSeqStr"]
      """  SerialMask.GenerateSeqString  """  
      self.ipLastUsedSeq:str = obj["ipLastUsedSeq"]
      """  SerialMask.SNLastUsedSeq  """  
      pass

class OnChangeSNLastUsedSeq_output:
   def __init__(self, obj):
      pass

class UpdateCharactersUsed_input:
   """ Required : 
   iPrefixLength
   iSuffixLength
   example
   """  
   def __init__(self, obj):
      self.iPrefixLength:int = obj["iPrefixLength"]
      """  Length of the Prefix  """  
      self.iSuffixLength:int = obj["iSuffixLength"]
      """  Length of the Suffix  """  
      self.example:str = obj["example"]
      """  serial mask example  """  
      pass

class UpdateCharactersUsed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.charactersUsed:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSerialNumMaskingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSerialNumMaskingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumMaskingTableset] = obj["ds"]
      pass

      """  output parameters  """  

