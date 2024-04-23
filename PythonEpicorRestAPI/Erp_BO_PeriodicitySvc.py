import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PeriodicitySvc
# Description: Periodicity Code Maintenance - for maintaining Periodicity information for
Purchase Scheduling and Sales Scheduling
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Periodicities(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Periodicities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Periodicities
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities",headers=creds) as resp:
           return await resp.json()

async def post_Periodicities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Periodicities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company, Plant, VendorNum, PurPoint, CustNum, ShipToNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Periodicity item
   Description: Calls GetByID to retrieve the Periodicity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Periodicity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company, Plant, VendorNum, PurPoint, CustNum, ShipToNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Periodicity for the service
   Description: Calls UpdateExt to update Periodicity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Periodicity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company, Plant, VendorNum, PurPoint, CustNum, ShipToNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Periodicity item
   Description: Call UpdateExt to delete Periodicity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Periodicity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicityListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePeriodicity, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePeriodicity=" + whereClausePeriodicity
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, vendorNum, purPoint, custNum, shipToNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Existplant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Existplant
   OperationID: Existplant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Existplant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Existplant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindCustNum
   Description: Returns the CustNum and Customer Name.
   OperationID: FindCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindVendorNum
   OperationID: FindVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPeriodicity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPeriodicity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPeriodicity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPeriodicity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPeriodicity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PeriodicityListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PeriodicityRow] = obj["value"]
      pass

class Erp_Tablesets_PeriodicityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Code1Rules:bool = obj["Code1Rules"]
      """  Code 1 = Semi-Weekly  """  
      self.Code1DeliveryDay1:int = obj["Code1DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code1DeliveryDay2:int = obj["Code1DeliveryDay2"]
      """  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code2Rules:bool = obj["Code2Rules"]
      """  Code 2 = Daily  """  
      self.Code2IncludeSatSun:bool = obj["Code2IncludeSatSun"]
      """  Are deliveries required on Saturday and Sunday?  """  
      self.Code3Rules:bool = obj["Code3Rules"]
      """  Code 3 = Monthly Forward  """  
      self.Code3DeliveryDay1:int = obj["Code3DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code3WeekNumberInMonth:int = obj["Code3WeekNumberInMonth"]
      """  The week number in the month that the delivery is required.  Valid values are 1-5.  """  
      self.Code4Rules:bool = obj["Code4Rules"]
      """  Code 4 = Weekly Forward  """  
      self.Code4DeliveryDayInWeek:int = obj["Code4DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code5Rules:bool = obj["Code5Rules"]
      """  Code 5 = Weekly Not Last Week of the Month  """  
      self.Code5DeliveryDayInWeek:int = obj["Code5DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code6Rules:bool = obj["Code6Rules"]
      """  Code 6 = Nth Day of the Month  """  
      self.Code6DeliveryDayInMonth:int = obj["Code6DeliveryDayInMonth"]
      """  The day of the month for the delivery.  Valid values are 1-31.  """  
      self.Code7Rules:bool = obj["Code7Rules"]
      """  Code 7 = Shipment Day of Week.  """  
      self.Code7ShipmentDayInWeek:int = obj["Code7ShipmentDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PlantNameName:str = obj["PlantNameName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Code1Rules:bool = obj["Code1Rules"]
      """  Code 1 = Semi-Weekly  """  
      self.Code1DeliveryDay1:int = obj["Code1DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code1DeliveryDay2:int = obj["Code1DeliveryDay2"]
      """  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code2Rules:bool = obj["Code2Rules"]
      """  Code 2 = Daily  """  
      self.Code2IncludeSatSun:bool = obj["Code2IncludeSatSun"]
      """  Are deliveries required on Saturday and Sunday?  """  
      self.Code3Rules:bool = obj["Code3Rules"]
      """  Code 3 = Monthly Forward  """  
      self.Code3DeliveryDay1:int = obj["Code3DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code3WeekNumberInMonth:int = obj["Code3WeekNumberInMonth"]
      """  The week number in the month that the delivery is required.  Valid values are 1-5.  """  
      self.Code4Rules:bool = obj["Code4Rules"]
      """  Code 4 = Weekly Forward  """  
      self.Code4DeliveryDayInWeek:int = obj["Code4DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code5Rules:bool = obj["Code5Rules"]
      """  Code 5 = Weekly Not Last Week of the Month  """  
      self.Code5DeliveryDayInWeek:int = obj["Code5DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code6Rules:bool = obj["Code6Rules"]
      """  Code 6 = Nth Day of the Month  """  
      self.Code6DeliveryDayInMonth:int = obj["Code6DeliveryDayInMonth"]
      """  The day of the month for the delivery.  Valid values are 1-31.  """  
      self.Code7Rules:bool = obj["Code7Rules"]
      """  Code 7 = Shipment Day of Week.  """  
      self.Code7ShipmentDayInWeek:int = obj["Code7ShipmentDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PlantNameName:str = obj["PlantNameName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   vendorNum
   purPoint
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PeriodicityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Code1Rules:bool = obj["Code1Rules"]
      """  Code 1 = Semi-Weekly  """  
      self.Code1DeliveryDay1:int = obj["Code1DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code1DeliveryDay2:int = obj["Code1DeliveryDay2"]
      """  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code2Rules:bool = obj["Code2Rules"]
      """  Code 2 = Daily  """  
      self.Code2IncludeSatSun:bool = obj["Code2IncludeSatSun"]
      """  Are deliveries required on Saturday and Sunday?  """  
      self.Code3Rules:bool = obj["Code3Rules"]
      """  Code 3 = Monthly Forward  """  
      self.Code3DeliveryDay1:int = obj["Code3DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code3WeekNumberInMonth:int = obj["Code3WeekNumberInMonth"]
      """  The week number in the month that the delivery is required.  Valid values are 1-5.  """  
      self.Code4Rules:bool = obj["Code4Rules"]
      """  Code 4 = Weekly Forward  """  
      self.Code4DeliveryDayInWeek:int = obj["Code4DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code5Rules:bool = obj["Code5Rules"]
      """  Code 5 = Weekly Not Last Week of the Month  """  
      self.Code5DeliveryDayInWeek:int = obj["Code5DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code6Rules:bool = obj["Code6Rules"]
      """  Code 6 = Nth Day of the Month  """  
      self.Code6DeliveryDayInMonth:int = obj["Code6DeliveryDayInMonth"]
      """  The day of the month for the delivery.  Valid values are 1-31.  """  
      self.Code7Rules:bool = obj["Code7Rules"]
      """  Code 7 = Shipment Day of Week.  """  
      self.Code7ShipmentDayInWeek:int = obj["Code7ShipmentDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PlantNameName:str = obj["PlantNameName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicityListTableset:
   def __init__(self, obj):
      self.PeriodicityList:list[Erp_Tablesets_PeriodicityListRow] = obj["PeriodicityList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PeriodicityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Code1Rules:bool = obj["Code1Rules"]
      """  Code 1 = Semi-Weekly  """  
      self.Code1DeliveryDay1:int = obj["Code1DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code1DeliveryDay2:int = obj["Code1DeliveryDay2"]
      """  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code2Rules:bool = obj["Code2Rules"]
      """  Code 2 = Daily  """  
      self.Code2IncludeSatSun:bool = obj["Code2IncludeSatSun"]
      """  Are deliveries required on Saturday and Sunday?  """  
      self.Code3Rules:bool = obj["Code3Rules"]
      """  Code 3 = Monthly Forward  """  
      self.Code3DeliveryDay1:int = obj["Code3DeliveryDay1"]
      """  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code3WeekNumberInMonth:int = obj["Code3WeekNumberInMonth"]
      """  The week number in the month that the delivery is required.  Valid values are 1-5.  """  
      self.Code4Rules:bool = obj["Code4Rules"]
      """  Code 4 = Weekly Forward  """  
      self.Code4DeliveryDayInWeek:int = obj["Code4DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code5Rules:bool = obj["Code5Rules"]
      """  Code 5 = Weekly Not Last Week of the Month  """  
      self.Code5DeliveryDayInWeek:int = obj["Code5DeliveryDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.Code6Rules:bool = obj["Code6Rules"]
      """  Code 6 = Nth Day of the Month  """  
      self.Code6DeliveryDayInMonth:int = obj["Code6DeliveryDayInMonth"]
      """  The day of the month for the delivery.  Valid values are 1-31.  """  
      self.Code7Rules:bool = obj["Code7Rules"]
      """  Code 7 = Shipment Day of Week.  """  
      self.Code7ShipmentDayInWeek:int = obj["Code7ShipmentDayInWeek"]
      """  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PlantNameName:str = obj["PlantNameName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicityTableset:
   def __init__(self, obj):
      self.Periodicity:list[Erp_Tablesets_PeriodicityRow] = obj["Periodicity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPeriodicityTableset:
   def __init__(self, obj):
      self.Periodicity:list[Erp_Tablesets_PeriodicityRow] = obj["Periodicity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Existplant_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class Existplant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.exist:bool = obj["exist"]
      pass

      """  output parameters  """  

class FindCustNum_input:
   """ Required : 
   inCustID
   """  
   def __init__(self, obj):
      self.inCustID:str = obj["inCustID"]
      """  The CustID to get the CustNum for  """  
      pass

class FindCustNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outCustNum:int = obj["parameters"]
      self.outCustName:str = obj["parameters"]
      pass

      """  output parameters  """  

class FindVendorNum_input:
   """ Required : 
   VendorID
   """  
   def __init__(self, obj):
      self.VendorID:str = obj["VendorID"]
      pass

class FindVendorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.VendorNum:int = obj["parameters"]
      self.Vendorname:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   plant
   vendorNum
   purPoint
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeriodicityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicityTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicityListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPeriodicity_input:
   """ Required : 
   ds
   plant
   vendorNum
   purPoint
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicityTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewPeriodicity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePeriodicity
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePeriodicity:str = obj["whereClausePeriodicity"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeriodicityTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPeriodicityTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPeriodicityTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicityTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicityTableset] = obj["ds"]
      pass

      """  output parameters  """  

