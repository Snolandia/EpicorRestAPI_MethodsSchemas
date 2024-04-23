import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxExemptSearchSvc
# Description: Search object against TaxExempt table
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxExemptSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxExemptSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxExemptSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/TaxExemptSearches",headers=creds) as resp:
           return await resp.json()

async def post_TaxExemptSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxExemptSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/TaxExemptSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxExemptSearches_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxExemptSearch item
   Description: Calls GetByID to retrieve the TaxExemptSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxExemptSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/TaxExemptSearches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxExemptSearches_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxExemptSearch for the service
   Description: Calls UpdateExt to update TaxExemptSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxExemptSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/TaxExemptSearches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxExemptSearches_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxExemptSearch item
   Description: Call UpdateExt to delete TaxExemptSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxExemptSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/TaxExemptSearches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxExempt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTaxExempt=" + whereClauseTaxExempt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToFile, key1, key2, taxCode, rateCode, effectiveFrom, epicorHeaders = None):
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
   params += "relatedToFile=" + relatedToFile
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
   params += "taxCode=" + taxCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rateCode=" + rateCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "effectiveFrom=" + effectiveFrom

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTypeOnEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTypeOnEntity
   Description: Method to call to retrieve the Tax Type description for an entity.
This method is called when adding types to entities to validate the type
does not already exist for the entity and to return the description
for display purposes.
   OperationID: ChangeTypeOnEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTypeOnEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTypeOnEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPercentDefault(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPercentDefault
   OperationID: GetPercentDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPercentDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPercentDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxExempt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxExempt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxExemptSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxExemptListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxExemptRow] = obj["value"]
      pass

class Erp_Tablesets_TaxExemptListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      """  Full description for a  Sales Tax master.  """  
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      """  Description  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxExemptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeTypeOnEntity_input:
   """ Required : 
   inTaxCode
   inRelatedToFile
   inKey1
   inKey2
   inRateCode
   inEffectiveFrom
   """  
   def __init__(self, obj):
      self.inTaxCode:str = obj["inTaxCode"]
      """  Tax Type  """  
      self.inRelatedToFile:str = obj["inRelatedToFile"]
      """  Related To File  """  
      self.inKey1:str = obj["inKey1"]
      """  Key1  """  
      self.inKey2:str = obj["inKey2"]
      """  Key2  """  
      self.inRateCode:str = obj["inRateCode"]
      """  Rate Code  """  
      self.inEffectiveFrom:str = obj["inEffectiveFrom"]
      """  Effective From Date  """  
      pass

class ChangeTypeOnEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxExemptListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      """  Full description for a  Sales Tax master.  """  
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      """  Description  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxExemptListTableset:
   def __init__(self, obj):
      self.TaxExemptList:list[Erp_Tablesets_TaxExemptListRow] = obj["TaxExemptList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxExemptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxExemptSearchTableset:
   def __init__(self, obj):
      self.TaxExempt:list[Erp_Tablesets_TaxExemptRow] = obj["TaxExempt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaxExemptSearchTableset:
   def __init__(self, obj):
      self.TaxExempt:list[Erp_Tablesets_TaxExemptRow] = obj["TaxExempt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   taxCode
   rateCode
   effectiveFrom
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      self.effectiveFrom:str = obj["effectiveFrom"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxExemptListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxExempt_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewTaxExempt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPercentDefault_input:
   """ Required : 
   pExemptType
   """  
   def __init__(self, obj):
      self.pExemptType:int = obj["pExemptType"]
      pass

class GetPercentDefault_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pPercent:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxExempt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxExempt:str = obj["whereClauseTaxExempt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtTaxExemptSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxExemptSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxExemptSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

