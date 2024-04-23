import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendorPPSearchSvc
# Description: Vendor Purchase Points Search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendorPPSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorPPSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches",headers=creds) as resp:
           return await resp.json()

async def post_VendorPPSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorPPSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendorPPSearches_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendorPPSearch item
   Description: Calls GetByID to retrieve the VendorPPSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPPSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendorPPSearches_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendorPPSearch for the service
   Description: Calls UpdateExt to update VendorPPSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorPPSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendorPPSearches_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendorPPSearch item
   Description: Call UpdateExt to delete VendorPPSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorPPSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/VendorPPSearches(" + Company + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendorPP, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseVendorPP=" + whereClauseVendorPP
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListForActiveSuppliers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForActiveSuppliers
   Description: Called to retrieve Purchase Points for active vendors
   OperationID: GetListForActiveSuppliers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForActiveSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForActiveSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VendorPPListGetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VendorPPListGetList
   Description: Called to retrieve GetList with VendorID within the WhereClause.
   OperationID: VendorPPListGetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VendorPPListGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorPPListGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendorPP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorPPSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorPPListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorPPRow] = obj["value"]
      pass

class Erp_Tablesets_VendorPPListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.PhoneNum:str = obj["PhoneNum"]
      self.GroupCode:str = obj["GroupCode"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      """  Language Name Description  """  
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      """  Long Description of the tax authority code.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  INExciseDivision  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  INExciseRange  """  
      self.INCommissionarate:str = obj["INCommissionarate"]
      """  INCommissionarate  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INServiceTaxRegNum:str = obj["INServiceTaxRegNum"]
      """  INServiceTaxRegNum  """  
      self.INTaxRegionCode:str = obj["INTaxRegionCode"]
      """  INTaxRegionCode  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.GroupCode:str = obj["GroupCode"]
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.INTaxRegionCodeDescription:str = obj["INTaxRegionCodeDescription"]
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtVendorPPSearchTableset:
   def __init__(self, obj):
      self.VendorPP:list[Erp_Tablesets_VendorPPRow] = obj["VendorPP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendorPPListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.PhoneNum:str = obj["PhoneNum"]
      self.GroupCode:str = obj["GroupCode"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      """  Language Name Description  """  
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      """  Long Description of the tax authority code.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorPPListTableset:
   def __init__(self, obj):
      self.VendorPPList:list[Erp_Tablesets_VendorPPListRow] = obj["VendorPPList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  INExciseDivision  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  INExciseRange  """  
      self.INCommissionarate:str = obj["INCommissionarate"]
      """  INCommissionarate  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INServiceTaxRegNum:str = obj["INServiceTaxRegNum"]
      """  INServiceTaxRegNum  """  
      self.INTaxRegionCode:str = obj["INTaxRegionCode"]
      """  INTaxRegionCode  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.GroupCode:str = obj["GroupCode"]
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.INTaxRegionCodeDescription:str = obj["INTaxRegionCodeDescription"]
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorPPSearchTableset:
   def __init__(self, obj):
      self.VendorPP:list[Erp_Tablesets_VendorPPRow] = obj["VendorPP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorPPSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorPPSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorPPSearchTableset] = obj["returnObj"]
      pass

class GetListForActiveSuppliers_input:
   """ Required : 
   whereClauseVendorPP
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendorPP:str = obj["whereClauseVendorPP"]
      """  Whereclause for VendorPP table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListForActiveSuppliers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorPPListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorPPListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewVendorPP_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorPPSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorPPSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendorPP
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendorPP:str = obj["whereClauseVendorPP"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorPPSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtVendorPPSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendorPPSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorPPSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorPPSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VendorPPListGetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause for VendorPP table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class VendorPPListGetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorPPListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

