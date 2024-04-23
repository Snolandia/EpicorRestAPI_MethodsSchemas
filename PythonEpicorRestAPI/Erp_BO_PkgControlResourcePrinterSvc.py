import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlResourcePrinterSvc
# Description: BO logic for PkgControlResourcePrinter.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlResourcePrinters(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlResourcePrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlResourcePrinters
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlResourcePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlResourcePrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlResourcePrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlResourcePrinterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlResourcePrinterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlResourcePrinters_Company_ResourceID(Company, ResourceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlResourcePrinter item
   Description: Calls GetByID to retrieve the PkgControlResourcePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlResourcePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlResourcePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlResourcePrinters_Company_ResourceID(Company, ResourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlResourcePrinter for the service
   Description: Calls UpdateExt to update PkgControlResourcePrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlResourcePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlResourcePrinterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlResourcePrinters_Company_ResourceID(Company, ResourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlResourcePrinter item
   Description: Call UpdateExt to delete PkgControlResourcePrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlResourcePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlResourcePrinters_Company_ResourceID_PkgControlResourcePrinters(Company, ResourceID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PkgControlResourcePrinters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlResourcePrinters1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlResourcePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")/PkgControlResourcePrinters",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlResourcePrinters_Company_ResourceID_PkgControlResourcePrinters_Company_ResourceID(Company, ResourceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlResourcePrinter item
   Description: Calls GetByID to retrieve the PkgControlResourcePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlResourcePrinter1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlResourcePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")/PkgControlResourcePrinters(" + Company + "," + ResourceID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseResource, whereClausePkgControlResourcePrinter, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseResource=" + whereClauseResource
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlResourcePrinter=" + whereClausePkgControlResourcePrinter
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(resourceID, epicorHeaders = None):
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
   params += "resourceID=" + resourceID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePrinterID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePrinterID
   Description: Validates the change of PrinterID field.
   OperationID: OnChangePrinterID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePrinterID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrinterID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResource
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlResourcePrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlResourcePrinter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlResourcePrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlResourcePrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlResourcePrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlResourcePrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlResourcePrinterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlResourcePrinterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceListRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlResourcePrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Unique identifier for a resource.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Unique identifier for a printer.  """  
      self.IsDefaultPrinter:bool = obj["IsDefaultPrinter"]
      """  Indicates whether the printer is the default printer for this resource in this site.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  Indicates the display sequence of the printers for this resource in this site.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.SysPrinterNetworkPath:str = obj["SysPrinterNetworkPath"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Description:str = obj["Description"]
      """  Full description of Resource.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  """  
      self.NextMaintDate:str = obj["NextMaintDate"]
      """  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  """  
      self.TrackProdQty:bool = obj["TrackProdQty"]
      """  Indicates the production quantities produced by this Resource will be tracked.  """  
      self.LinkedPart:str = obj["LinkedPart"]
      """  Links this Resource to a Part, which must be valid in the Part table.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   resourceID
   """  
   def __init__(self, obj):
      self.resourceID:str = obj["resourceID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlResourcePrinterListTableset:
   def __init__(self, obj):
      self.ResourceList:list[Erp_Tablesets_ResourceListRow] = obj["ResourceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlResourcePrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Unique identifier for a resource.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Unique identifier for a printer.  """  
      self.IsDefaultPrinter:bool = obj["IsDefaultPrinter"]
      """  Indicates whether the printer is the default printer for this resource in this site.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  Indicates the display sequence of the printers for this resource in this site.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.SysPrinterNetworkPath:str = obj["SysPrinterNetworkPath"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlResourcePrinterTableset:
   def __init__(self, obj):
      self.Resource:list[Erp_Tablesets_ResourceRow] = obj["Resource"]
      self.PkgControlResourcePrinter:list[Erp_Tablesets_PkgControlResourcePrinterRow] = obj["PkgControlResourcePrinter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ResourceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Description:str = obj["Description"]
      """  Full description of Resource.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  """  
      self.NextMaintDate:str = obj["NextMaintDate"]
      """  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  """  
      self.TrackProdQty:bool = obj["TrackProdQty"]
      """  Indicates the production quantities produced by this Resource will be tracked.  """  
      self.LinkedPart:str = obj["LinkedPart"]
      """  Links this Resource to a Part, which must be valid in the Part table.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Description:str = obj["Description"]
      """  Full description of Resource.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  """  
      self.Finite:bool = obj["Finite"]
      """  If yes then this Resource is scheduled as though it has finite production capacity.  """  
      self.AllowManualOverride:bool = obj["AllowManualOverride"]
      """  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  """  
      self.NextMaintDate:str = obj["NextMaintDate"]
      """  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  """  
      self.BackflushWhse:str = obj["BackflushWhse"]
      """  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  """  
      self.BackflushBinNum:str = obj["BackflushBinNum"]
      """  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.InputBinNum:str = obj["InputBinNum"]
      """  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.TrackProdQty:bool = obj["TrackProdQty"]
      """  Indicates the production quantities produced by this Resource will be tracked.  """  
      self.LinkedPart:str = obj["LinkedPart"]
      """  Links this Resource to a Part, which must be valid in the Part table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Resource.  Links the Resource to a Fixed Asset.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  The labor rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Default labor rate for setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QProdLabRate:int = obj["QProdLabRate"]
      """   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupLabRate:int = obj["QSetupLabRate"]
      """   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QBurdenType:str = obj["QBurdenType"]
      """  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  """  
      self.GetDefaultBurdenFromGroup:bool = obj["GetDefaultBurdenFromGroup"]
      """  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  """  
      self.MoveHours:int = obj["MoveHours"]
      """  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  """  
      self.QueHours:int = obj["QueHours"]
      """  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  """  
      self.GetDefaultMQFromGroup:bool = obj["GetDefaultMQFromGroup"]
      """  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  """  
      self.InformOverload:bool = obj["InformOverload"]
      """  Indicates that the Resource is visible in Overload Informer.  """  
      self.MinOverloadPerc:int = obj["MinOverloadPerc"]
      """  The minimum overload threshold before a day shows up in the Overload Informer.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  """  
      self.GetDefaultLaborFromGroup:bool = obj["GetDefaultLaborFromGroup"]
      """  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.FiniteHorizon:int = obj["FiniteHorizon"]
      """  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  """  
      self.AutoMove:bool = obj["AutoMove"]
      """  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  """  
      self.SplitOperations:bool = obj["SplitOperations"]
      """  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.GetDefaultWhseFromGroup:bool = obj["GetDefaultWhseFromGroup"]
      """  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  """  
      self.URL:str = obj["URL"]
      """  URL  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NumCavs:int = obj["NumCavs"]
      """  NumCavs  """  
      self.RunnerWt:int = obj["RunnerWt"]
      """  RunnerWt  """  
      self.SetupTime:int = obj["SetupTime"]
      """  SetupTime  """  
      self.TearDownTime:int = obj["TearDownTime"]
      """  TearDownTime  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.Brand:str = obj["Brand"]
      """  Brand  """  
      self.LocID:str = obj["LocID"]
      """  LocID  """  
      self.PmMapNo:int = obj["PmMapNo"]
      """  PmMapNo  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MobileResource:bool = obj["MobileResource"]
      """  MobileResource  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.MESQueue:bool = obj["MESQueue"]
      """  MESQueue  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  """  
      self.EquipCreate:bool = obj["EquipCreate"]
      """  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  """  
      self.Plant:str = obj["Plant"]
      """  Plant from Resource Group  """  
      self.ReadOnlyFields:str = obj["ReadOnlyFields"]
      self.BitFlag:int = obj["BitFlag"]
      self.LinkedPartTrackLots:bool = obj["LinkedPartTrackLots"]
      self.LinkedPartPartDescription:str = obj["LinkedPartPartDescription"]
      self.LinkedPartIUM:str = obj["LinkedPartIUM"]
      self.LinkedPartTrackSerialNum:bool = obj["LinkedPartTrackSerialNum"]
      self.LinkedPartTrackDimension:bool = obj["LinkedPartTrackDimension"]
      self.LinkedPartSellingFactor:int = obj["LinkedPartSellingFactor"]
      self.LinkedPartSalesUM:str = obj["LinkedPartSalesUM"]
      self.LinkedPartPricePerCode:str = obj["LinkedPartPricePerCode"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ResourceTypeDescription:str = obj["ResourceTypeDescription"]
      self.ResourceTypeExternalMESType:str = obj["ResourceTypeExternalMESType"]
      self.WhseBackflushWhseDescDescription:str = obj["WhseBackflushWhseDescDescription"]
      self.WhseInputWhseDescDescription:str = obj["WhseInputWhseDescDescription"]
      self.WhseOutputWhseDescDescription:str = obj["WhseOutputWhseDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPkgControlResourcePrinterTableset:
   def __init__(self, obj):
      self.Resource:list[Erp_Tablesets_ResourceRow] = obj["Resource"]
      self.PkgControlResourcePrinter:list[Erp_Tablesets_PkgControlResourcePrinterRow] = obj["PkgControlResourcePrinter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   resourceID
   """  
   def __init__(self, obj):
      self.resourceID:str = obj["resourceID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlResourcePrinterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlResourcePrinter_input:
   """ Required : 
   ds
   plant
   resourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.resourceID:str = obj["resourceID"]
      pass

class GetNewPkgControlResourcePrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResource_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

class GetNewResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseResource
   whereClausePkgControlResourcePrinter
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseResource:str = obj["whereClauseResource"]
      self.whereClausePkgControlResourcePrinter:str = obj["whereClausePkgControlResourcePrinter"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["returnObj"]
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

class OnChangePrinterID_input:
   """ Required : 
   newValue
   ds
   """  
   def __init__(self, obj):
      self.newValue:str = obj["newValue"]
      """  Proposed value.  """  
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

class OnChangePrinterID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlResourcePrinterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlResourcePrinterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlResourcePrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

