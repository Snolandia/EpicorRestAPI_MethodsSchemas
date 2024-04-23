import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.IPFormCustomSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IPFormCustoms(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IPFormCustoms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IPFormCustoms
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XXXDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/IPFormCustoms",headers=creds) as resp:
           return await resp.json()

async def post_IPFormCustoms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IPFormCustoms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/IPFormCustoms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IPFormCustoms_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company, ProductID, TypeCode, CGCCode, Key1, Key2, Key3, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IPFormCustom item
   Description: Calls GetByID to retrieve the IPFormCustom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IPFormCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/IPFormCustoms(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IPFormCustoms_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company, ProductID, TypeCode, CGCCode, Key1, Key2, Key3, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IPFormCustom for the service
   Description: Calls UpdateExt to update IPFormCustom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IPFormCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.XXXDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/IPFormCustoms(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IPFormCustoms_Company_ProductID_TypeCode_CGCCode_Key1_Key2_Key3(Company, ProductID, TypeCode, CGCCode, Key1, Key2, Key3, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IPFormCustom item
   Description: Call UpdateExt to delete IPFormCustom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IPFormCustom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param CGCCode: Desc: CGCCode   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/IPFormCustoms(" + Company + "," + ProductID + "," + TypeCode + "," + CGCCode + "," + Key1 + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XXXDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseXXXDef, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseXXXDef=" + whereClauseXXXDef
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(productID, typeCode, cgCCode, key1, key2, key3, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "productID=" + productID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "typeCode=" + typeCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "cgCCode=" + cgCCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewXXXDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewXXXDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXXXDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXXXDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXXXDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IPFormCustomSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XXXDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XXXDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XXXDefRow] = obj["value"]
      pass

class Ice_Tablesets_XXXDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Date Last Updated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Updated By  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.SysCharacter01:str = obj["SysCharacter01"]
      """  SysCharacter01  """  
      self.SysCharacter02:str = obj["SysCharacter02"]
      """  SysCharacter02  """  
      self.SysCharacter03:str = obj["SysCharacter03"]
      """  SysCharacter03  """  
      self.SysCharacter04:str = obj["SysCharacter04"]
      """  SysCharacter04  """  
      self.SysCharacter05:str = obj["SysCharacter05"]
      """  SysCharacter05  """  
      self.SysNumber01:int = obj["SysNumber01"]
      """  SysNumber01  """  
      self.SysNumber02:int = obj["SysNumber02"]
      """  SysNumber02  """  
      self.SysNumber03:int = obj["SysNumber03"]
      """  SysNumber03  """  
      self.SysNumber04:int = obj["SysNumber04"]
      """  SysNumber04  """  
      self.SysNumber05:int = obj["SysNumber05"]
      """  SysNumber05  """  
      self.SysDate01:str = obj["SysDate01"]
      """  SysDate01  """  
      self.SysDate02:str = obj["SysDate02"]
      """  SysDate02  """  
      self.SysDate03:str = obj["SysDate03"]
      """  SysDate03  """  
      self.SysDate04:str = obj["SysDate04"]
      """  SysDate04  """  
      self.SysDate05:str = obj["SysDate05"]
      """  SysDate05  """  
      self.SysCheckBox01:bool = obj["SysCheckBox01"]
      """  SysCheckBox01  """  
      self.SysCheckBox02:bool = obj["SysCheckBox02"]
      """  SysCheckBox02  """  
      self.SysCheckBox03:bool = obj["SysCheckBox03"]
      """  SysCheckBox03  """  
      self.SysCheckBox04:bool = obj["SysCheckBox04"]
      """  SysCheckBox04  """  
      self.SysCheckBox05:bool = obj["SysCheckBox05"]
      """  SysCheckBox05  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the GenX.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysCheckBox06:bool = obj["SysCheckBox06"]
      """  SysCheckBox06  """  
      self.SysCheckBox07:bool = obj["SysCheckBox07"]
      """  SysCheckBox07  """  
      self.OnMenu:bool = obj["OnMenu"]
      """  OnMenu  """  
      self.Duplicate:bool = obj["Duplicate"]
      """  Duplicate  """  
      self.Cosmetic:bool = obj["Cosmetic"]
      """  Cosmetic  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XXXDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Date Last Updated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Updated By  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.SysCharacter01:str = obj["SysCharacter01"]
      """  SysCharacter01  """  
      self.SysCharacter02:str = obj["SysCharacter02"]
      """  SysCharacter02  """  
      self.SysCharacter03:str = obj["SysCharacter03"]
      """  SysCharacter03  """  
      self.SysCharacter04:str = obj["SysCharacter04"]
      """  SysCharacter04  """  
      self.SysCharacter05:str = obj["SysCharacter05"]
      """  SysCharacter05  """  
      self.SysNumber01:int = obj["SysNumber01"]
      """  SysNumber01  """  
      self.SysNumber02:int = obj["SysNumber02"]
      """  SysNumber02  """  
      self.SysNumber03:int = obj["SysNumber03"]
      """  SysNumber03  """  
      self.SysNumber04:int = obj["SysNumber04"]
      """  SysNumber04  """  
      self.SysNumber05:int = obj["SysNumber05"]
      """  SysNumber05  """  
      self.SysDate01:str = obj["SysDate01"]
      """  SysDate01  """  
      self.SysDate02:str = obj["SysDate02"]
      """  SysDate02  """  
      self.SysDate03:str = obj["SysDate03"]
      """  SysDate03  """  
      self.SysDate04:str = obj["SysDate04"]
      """  SysDate04  """  
      self.SysDate05:str = obj["SysDate05"]
      """  SysDate05  """  
      self.SysCheckBox01:bool = obj["SysCheckBox01"]
      """  SysCheckBox01  """  
      self.SysCheckBox02:bool = obj["SysCheckBox02"]
      """  SysCheckBox02  """  
      self.SysCheckBox03:bool = obj["SysCheckBox03"]
      """  SysCheckBox03  """  
      self.SysCheckBox04:bool = obj["SysCheckBox04"]
      """  SysCheckBox04  """  
      self.SysCheckBox05:bool = obj["SysCheckBox05"]
      """  SysCheckBox05  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the GenX.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysCheckBox06:bool = obj["SysCheckBox06"]
      """  SysCheckBox06  """  
      self.SysCheckBox07:bool = obj["SysCheckBox07"]
      """  SysCheckBox07  """  
      self.OnMenu:bool = obj["OnMenu"]
      """  OnMenu  """  
      self.Duplicate:bool = obj["Duplicate"]
      """  Duplicate  """  
      self.Cosmetic:bool = obj["Cosmetic"]
      """  Cosmetic  """  
      self.Content:str = obj["Content"]
      """  Content  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   productID
   typeCode
   cgCCode
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.productID:str = obj["productID"]
      self.typeCode:str = obj["typeCode"]
      self.cgCCode:str = obj["cgCCode"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   productID
   typeCode
   cgCCode
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.productID:str = obj["productID"]
      self.typeCode:str = obj["typeCode"]
      self.cgCCode:str = obj["cgCCode"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_GenXDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_GenXDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_GenXDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_XXXDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewXXXDef_input:
   """ Required : 
   ds
   productID
   typeCode
   cgCCode
   key1
   key2
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_GenXDataTableset] = obj["ds"]
      self.productID:str = obj["productID"]
      self.typeCode:str = obj["typeCode"]
      self.cgCCode:str = obj["cgCCode"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      pass

class GetNewXXXDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_GenXDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseXXXDef
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseXXXDef:str = obj["whereClauseXXXDef"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_GenXDataTableset] = obj["returnObj"]
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

class Ice_Tablesets_GenXDataTableset:
   def __init__(self, obj):
      self.XXXDef:list[Ice_Tablesets_XXXDefRow] = obj["XXXDef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtGenXDataTableset:
   def __init__(self, obj):
      self.XXXDef:list[Ice_Tablesets_XXXDefRow] = obj["XXXDef"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XXXDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Date Last Updated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Updated By  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.SysCharacter01:str = obj["SysCharacter01"]
      """  SysCharacter01  """  
      self.SysCharacter02:str = obj["SysCharacter02"]
      """  SysCharacter02  """  
      self.SysCharacter03:str = obj["SysCharacter03"]
      """  SysCharacter03  """  
      self.SysCharacter04:str = obj["SysCharacter04"]
      """  SysCharacter04  """  
      self.SysCharacter05:str = obj["SysCharacter05"]
      """  SysCharacter05  """  
      self.SysNumber01:int = obj["SysNumber01"]
      """  SysNumber01  """  
      self.SysNumber02:int = obj["SysNumber02"]
      """  SysNumber02  """  
      self.SysNumber03:int = obj["SysNumber03"]
      """  SysNumber03  """  
      self.SysNumber04:int = obj["SysNumber04"]
      """  SysNumber04  """  
      self.SysNumber05:int = obj["SysNumber05"]
      """  SysNumber05  """  
      self.SysDate01:str = obj["SysDate01"]
      """  SysDate01  """  
      self.SysDate02:str = obj["SysDate02"]
      """  SysDate02  """  
      self.SysDate03:str = obj["SysDate03"]
      """  SysDate03  """  
      self.SysDate04:str = obj["SysDate04"]
      """  SysDate04  """  
      self.SysDate05:str = obj["SysDate05"]
      """  SysDate05  """  
      self.SysCheckBox01:bool = obj["SysCheckBox01"]
      """  SysCheckBox01  """  
      self.SysCheckBox02:bool = obj["SysCheckBox02"]
      """  SysCheckBox02  """  
      self.SysCheckBox03:bool = obj["SysCheckBox03"]
      """  SysCheckBox03  """  
      self.SysCheckBox04:bool = obj["SysCheckBox04"]
      """  SysCheckBox04  """  
      self.SysCheckBox05:bool = obj["SysCheckBox05"]
      """  SysCheckBox05  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the GenX.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysCheckBox06:bool = obj["SysCheckBox06"]
      """  SysCheckBox06  """  
      self.SysCheckBox07:bool = obj["SysCheckBox07"]
      """  SysCheckBox07  """  
      self.OnMenu:bool = obj["OnMenu"]
      """  OnMenu  """  
      self.Duplicate:bool = obj["Duplicate"]
      """  Duplicate  """  
      self.Cosmetic:bool = obj["Cosmetic"]
      """  Cosmetic  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XXXDefListTableset:
   def __init__(self, obj):
      self.XXXDefList:list[Ice_Tablesets_XXXDefListRow] = obj["XXXDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XXXDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  Valid values:  BE - Base Extention, EX - Express, ST - Standard, EP - Enterprise  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  Date Last Updated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  Last Updated By  """  
      self.Version:str = obj["Version"]
      """  Version  """  
      self.DataBaseVersion:int = obj["DataBaseVersion"]
      """  Database Version  """  
      self.SysCharacter01:str = obj["SysCharacter01"]
      """  SysCharacter01  """  
      self.SysCharacter02:str = obj["SysCharacter02"]
      """  SysCharacter02  """  
      self.SysCharacter03:str = obj["SysCharacter03"]
      """  SysCharacter03  """  
      self.SysCharacter04:str = obj["SysCharacter04"]
      """  SysCharacter04  """  
      self.SysCharacter05:str = obj["SysCharacter05"]
      """  SysCharacter05  """  
      self.SysNumber01:int = obj["SysNumber01"]
      """  SysNumber01  """  
      self.SysNumber02:int = obj["SysNumber02"]
      """  SysNumber02  """  
      self.SysNumber03:int = obj["SysNumber03"]
      """  SysNumber03  """  
      self.SysNumber04:int = obj["SysNumber04"]
      """  SysNumber04  """  
      self.SysNumber05:int = obj["SysNumber05"]
      """  SysNumber05  """  
      self.SysDate01:str = obj["SysDate01"]
      """  SysDate01  """  
      self.SysDate02:str = obj["SysDate02"]
      """  SysDate02  """  
      self.SysDate03:str = obj["SysDate03"]
      """  SysDate03  """  
      self.SysDate04:str = obj["SysDate04"]
      """  SysDate04  """  
      self.SysDate05:str = obj["SysDate05"]
      """  SysDate05  """  
      self.SysCheckBox01:bool = obj["SysCheckBox01"]
      """  SysCheckBox01  """  
      self.SysCheckBox02:bool = obj["SysCheckBox02"]
      """  SysCheckBox02  """  
      self.SysCheckBox03:bool = obj["SysCheckBox03"]
      """  SysCheckBox03  """  
      self.SysCheckBox04:bool = obj["SysCheckBox04"]
      """  SysCheckBox04  """  
      self.SysCheckBox05:bool = obj["SysCheckBox05"]
      """  SysCheckBox05  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the GenX.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysCheckBox06:bool = obj["SysCheckBox06"]
      """  SysCheckBox06  """  
      self.SysCheckBox07:bool = obj["SysCheckBox07"]
      """  SysCheckBox07  """  
      self.OnMenu:bool = obj["OnMenu"]
      """  OnMenu  """  
      self.Duplicate:bool = obj["Duplicate"]
      """  Duplicate  """  
      self.Cosmetic:bool = obj["Cosmetic"]
      """  Cosmetic  """  
      self.Content:str = obj["Content"]
      """  Content  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtGenXDataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtGenXDataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_GenXDataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_GenXDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

