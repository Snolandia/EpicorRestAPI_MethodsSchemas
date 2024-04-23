import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MICRPrinterSvc
# Description: Initializes a new class of "MICRPrinterSvc" />.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MICRPrinters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MICRPrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MICRPrinters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MICRPrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters",headers=creds) as resp:
           return await resp.json()

async def post_MICRPrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MICRPrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MICRPrinters_Company_MICRPrinterID(Company, MICRPrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MICRPrinter item
   Description: Calls GetByID to retrieve the MICRPrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MICRPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MICRPrinterID: Desc: MICRPrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MICRPrinters_Company_MICRPrinterID(Company, MICRPrinterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MICRPrinter for the service
   Description: Calls UpdateExt to update MICRPrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MICRPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MICRPrinterID: Desc: MICRPrinterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MICRPrinters_Company_MICRPrinterID(Company, MICRPrinterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MICRPrinter item
   Description: Call UpdateExt to delete MICRPrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MICRPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MICRPrinterID: Desc: MICRPrinterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MICRPrinterListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMICRPrinter, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMICRPrinter=" + whereClauseMICRPrinter
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(miCRPrinterID, epicorHeaders = None):
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
   params += "miCRPrinterID=" + miCRPrinterID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ExistsDefaultCompanyMICRPrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsDefaultCompanyMICRPrinter
   Description: Check if already exists a default MICR printer to print checks.
   OperationID: ExistsDefaultCompanyMICRPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsDefaultCompanyMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsDefaultCompanyMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsClientDefaultCompanyMICRPrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsClientDefaultCompanyMICRPrinter
   Description: Check if the default MICR printer is Client or Server printer.
   OperationID: IsClientDefaultCompanyMICRPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsClientDefaultCompanyMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsClientDefaultCompanyMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsPrinterID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsPrinterID
   Description: Validates if Printer exists
   OperationID: ExistsPrinterID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsPrinterID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPrinterID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsOtherDefaultMICRPrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsOtherDefaultMICRPrinter
   Description: Validates other MICR Printer is set as default
   OperationID: ExistsOtherDefaultMICRPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsOtherDefaultMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsOtherDefaultMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSignatureImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSignatureImage
   Description: Get Signature image with line overlaid.
   OperationID: GetSignatureImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSignatureImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSignatureImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMICRPrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMICRPrinter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMICRPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MICRPrinterListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MICRPrinterRow] = obj["value"]
      pass

class Erp_Tablesets_MICRPrinterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MICRPrinterID:str = obj["MICRPrinterID"]
      """  ID for MICR Printer.  """  
      self.DefaultPrinter:bool = obj["DefaultPrinter"]
      """  Defines if the MICR Printer is the default or not.  """  
      self.OnUsSymbol:str = obj["OnUsSymbol"]
      """  Tells the reader or sorter that next section of the MICR line represents the account number.  """  
      self.TransitSymbol:str = obj["TransitSymbol"]
      """  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  """  
      self.DashSymbol:str = obj["DashSymbol"]
      """  The dash symbol is sometimes used as a separator within the On Us field.  """  
      self.MICRFont:str = obj["MICRFont"]
      """  Font used to print MICR checks.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  ID for Printer used to print MICR cheks.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores I when is Image and T when is text.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  ImageID for the image used as signature.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores I when is Image and T when is text.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  ImageID for the image used as logo.  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MICRPrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MICRPrinterID:str = obj["MICRPrinterID"]
      """  ID for MICR Printer.  """  
      self.DefaultPrinter:bool = obj["DefaultPrinter"]
      """  Defines if the MICR Printer is the default or not.  """  
      self.OnUsSymbol:str = obj["OnUsSymbol"]
      """  Tells the reader or sorter that next section of the MICR line represents the account number.  """  
      self.TransitSymbol:str = obj["TransitSymbol"]
      """  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  """  
      self.DashSymbol:str = obj["DashSymbol"]
      """  The dash symbol is sometimes used as a separator within the On Us field.  """  
      self.MICRFont:str = obj["MICRFont"]
      """  Font used to print MICR checks.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  ID for Printer used to print MICR cheks.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores I when is Image and T when is text.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  ImageID for the image used as signature.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores I when is Image and T when is text.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  ImageID for the image used as logo.  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.IsClient:bool = obj["IsClient"]
      """  Defines whether is a client printer or server printer.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
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
   miCRPrinterID
   """  
   def __init__(self, obj):
      self.miCRPrinterID:str = obj["miCRPrinterID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MICRPrinterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MICRPrinterID:str = obj["MICRPrinterID"]
      """  ID for MICR Printer.  """  
      self.DefaultPrinter:bool = obj["DefaultPrinter"]
      """  Defines if the MICR Printer is the default or not.  """  
      self.OnUsSymbol:str = obj["OnUsSymbol"]
      """  Tells the reader or sorter that next section of the MICR line represents the account number.  """  
      self.TransitSymbol:str = obj["TransitSymbol"]
      """  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  """  
      self.DashSymbol:str = obj["DashSymbol"]
      """  The dash symbol is sometimes used as a separator within the On Us field.  """  
      self.MICRFont:str = obj["MICRFont"]
      """  Font used to print MICR checks.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  ID for Printer used to print MICR cheks.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores I when is Image and T when is text.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  ImageID for the image used as signature.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores I when is Image and T when is text.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  ImageID for the image used as logo.  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MICRPrinterListTableset:
   def __init__(self, obj):
      self.MICRPrinterList:list[Erp_Tablesets_MICRPrinterListRow] = obj["MICRPrinterList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MICRPrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MICRPrinterID:str = obj["MICRPrinterID"]
      """  ID for MICR Printer.  """  
      self.DefaultPrinter:bool = obj["DefaultPrinter"]
      """  Defines if the MICR Printer is the default or not.  """  
      self.OnUsSymbol:str = obj["OnUsSymbol"]
      """  Tells the reader or sorter that next section of the MICR line represents the account number.  """  
      self.TransitSymbol:str = obj["TransitSymbol"]
      """  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  """  
      self.DashSymbol:str = obj["DashSymbol"]
      """  The dash symbol is sometimes used as a separator within the On Us field.  """  
      self.MICRFont:str = obj["MICRFont"]
      """  Font used to print MICR checks.  """  
      self.PrinterID:str = obj["PrinterID"]
      """  ID for Printer used to print MICR cheks.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores I when is Image and T when is text.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  ImageID for the image used as signature.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores I when is Image and T when is text.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  ImageID for the image used as logo.  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.IsClient:bool = obj["IsClient"]
      """  Defines whether is a client printer or server printer.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MICRPrinterTableset:
   def __init__(self, obj):
      self.MICRPrinter:list[Erp_Tablesets_MICRPrinterRow] = obj["MICRPrinter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMICRPrinterTableset:
   def __init__(self, obj):
      self.MICRPrinter:list[Erp_Tablesets_MICRPrinterRow] = obj["MICRPrinter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsDefaultCompanyMICRPrinter_input:
   """ Required : 
   currentCompany
   """  
   def __init__(self, obj):
      self.currentCompany:str = obj["currentCompany"]
      """  Session Company.  """  
      pass

class ExistsDefaultCompanyMICRPrinter_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsOtherDefaultMICRPrinter_input:
   """ Required : 
   MICRPrinterID
   """  
   def __init__(self, obj):
      self.MICRPrinterID:str = obj["MICRPrinterID"]
      """  MICRPrinterID  """  
      pass

class ExistsOtherDefaultMICRPrinter_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ExistsPrinterID_input:
   """ Required : 
   PrinterID
   """  
   def __init__(self, obj):
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID  """  
      pass

class ExistsPrinterID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   miCRPrinterID
   """  
   def __init__(self, obj):
      self.miCRPrinterID:str = obj["miCRPrinterID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MICRPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MICRPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MICRPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MICRPrinterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMICRPrinter_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MICRPrinterTableset] = obj["ds"]
      pass

class GetNewMICRPrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MICRPrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMICRPrinter
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMICRPrinter:str = obj["whereClauseMICRPrinter"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MICRPrinterTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSignatureImage_input:
   """ Required : 
   imageID
   """  
   def __init__(self, obj):
      self.imageID:str = obj["imageID"]
      pass

class GetSignatureImage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class IsClientDefaultCompanyMICRPrinter_input:
   """ Required : 
   currentCompany
   """  
   def __init__(self, obj):
      self.currentCompany:str = obj["currentCompany"]
      """  Session Company.  """  
      pass

class IsClientDefaultCompanyMICRPrinter_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMICRPrinterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMICRPrinterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MICRPrinterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MICRPrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

