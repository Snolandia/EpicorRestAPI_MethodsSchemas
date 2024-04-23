import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.PlantSvc
# Description: Site Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Plants(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Plants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Plants
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/Plants",headers=creds) as resp:
           return await resp.json()

async def post_Plants(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Plants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/Plants", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Plants_Company_Plant1(Company, Plant1, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Plant item
   Description: Calls GetByID to retrieve the Plant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Plant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant1: Desc: Plant1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Plants_Company_Plant1(Company, Plant1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Plant for the service
   Description: Calls UpdateExt to update Plant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Plant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant1: Desc: Plant1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Plants_Company_Plant1(Company, Plant1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Plant item
   Description: Call UpdateExt to delete Plant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Plant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant1: Desc: Plant1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/Plants(" + Company + "," + Plant1 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlant, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePlant=" + whereClausePlant
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, epicorHeaders = None):
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
   params += "plant=" + plant

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailablePlants(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailablePlants
   Description: Gets a list of the available sites for a specific company. This includes unauthorized sites.
   OperationID: GetAvailablePlants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailablePlants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailablePlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsAuthorizedForPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAuthorizedForPlant
   Description: Determines whether the current user is allowed to access a specific site.
   OperationID: IsAuthorizedForPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAuthorizedForPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAuthorizedForPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadLogoImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadLogoImage
   Description: Upload logo image
   OperationID: UploadLogoImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLogoImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLogoImage
   Description: Update logo image in database
   OperationID: UpdateLogoImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.PlantSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PlantListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PlantRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PlantRow] = obj["value"]
      pass

class Ice_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant1:str = obj["Plant1"]
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.KineticColor:str = obj["KineticColor"]
      """  KineticColor  """  
      self.LogoFileName:str = obj["LogoFileName"]
      self.LogoImageContent:str = obj["LogoImageContent"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetAvailablePlants_input:
   """ Required : 
   companyId
   """  
   def __init__(self, obj):
      self.companyId:str = obj["companyId"]
      """  The company to retrieve sites for.  """  
      pass

class GetAvailablePlants_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PlantListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_PlantListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlant_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

class GetNewPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePlant
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlant:str = obj["whereClausePlant"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_PlantTableset] = obj["returnObj"]
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

class Ice_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PlantListTableset:
   def __init__(self, obj):
      self.PlantList:list[Ice_Tablesets_PlantListRow] = obj["PlantList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_PlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.KineticColor:str = obj["KineticColor"]
      """  KineticColor  """  
      self.LogoFileName:str = obj["LogoFileName"]
      self.LogoImageContent:str = obj["LogoImageContent"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PlantTableset:
   def __init__(self, obj):
      self.Plant:list[Ice_Tablesets_PlantRow] = obj["Plant"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtPlantTableset:
   def __init__(self, obj):
      self.Plant:list[Ice_Tablesets_PlantRow] = obj["Plant"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class IsAuthorizedForPlant_input:
   """ Required : 
   siteID
   """  
   def __init__(self, obj):
      self.siteID:str = obj["siteID"]
      """  The site identifier.  """  
      pass

class IsAuthorizedForPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPlantTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtPlantTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLogoImage_input:
   """ Required : 
   plant
   fileName
   fileContents
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.fileName:str = obj["fileName"]
      self.fileContents:str = obj["fileContents"]
      pass

class UpdateLogoImage_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadLogoImage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

class UploadLogoImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

