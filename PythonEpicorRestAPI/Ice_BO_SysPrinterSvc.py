import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysPrinterSvc
# Description: The system printer service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysPrinters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysPrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysPrinters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysPrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/SysPrinters",headers=creds) as resp:
           return await resp.json()

async def post_SysPrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysPrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysPrinterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysPrinterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/SysPrinters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysPrinters_Company_PrinterID(Company, PrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysPrinter item
   Description: Calls GetByID to retrieve the SysPrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysPrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/SysPrinters(" + Company + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysPrinters_Company_PrinterID(Company, PrinterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysPrinter for the service
   Description: Calls UpdateExt to update SysPrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysPrinterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/SysPrinters(" + Company + "," + PrinterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysPrinters_Company_PrinterID(Company, PrinterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysPrinter item
   Description: Call UpdateExt to delete SysPrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysPrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/SysPrinters(" + Company + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PaperSizes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PaperSizes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaperSizes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PaperSizeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSizes",headers=creds) as resp:
           return await resp.json()

async def post_PaperSizes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaperSizes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PaperSizeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PaperSizeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSizes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PaperSizes_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PaperSize item
   Description: Calls GetByID to retrieve the PaperSize item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaperSize
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PaperSizeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSizes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PaperSizes_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PaperSize for the service
   Description: Calls UpdateExt to update PaperSize. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaperSize
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PaperSizeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSizes(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PaperSizes_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PaperSize item
   Description: Call UpdateExt to delete PaperSize item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaperSize
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSizes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PaperSources(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PaperSources items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaperSources
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.PaperSourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSources",headers=creds) as resp:
           return await resp.json()

async def post_PaperSources(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaperSources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.PaperSourceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.PaperSourceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSources", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PaperSources_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PaperSource item
   Description: Calls GetByID to retrieve the PaperSource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaperSource
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.PaperSourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSources(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PaperSources_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PaperSource for the service
   Description: Calls UpdateExt to update PaperSource. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaperSource
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.PaperSourceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSources(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PaperSources_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PaperSource item
   Description: Call UpdateExt to delete PaperSource item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaperSource
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/PaperSources(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysPrinterListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysPrinter, whereClausePaperSize, whereClausePaperSource, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseSysPrinter=" + whereClauseSysPrinter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePaperSize=" + whereClausePaperSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePaperSource=" + whereClausePaperSource
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(printerID, epicorHeaders = None):
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
   params += "printerID=" + printerID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_EdgePrintingAvailable(epicorHeaders = None):
   """  
   Summary: Invoke method EdgePrintingAvailable
   Description: Indicates whether or not the Edge Message Hub is running and agents have subscribe to it.
   OperationID: EdgePrintingAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EdgePrintingAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetPrintersFromEdgeAgents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrintersFromEdgeAgents
   Description: Gets the list of available printers from the specified Edge Agent
   OperationID: GetPrintersFromEdgeAgents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrintersFromEdgeAgents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrintersFromEdgeAgents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllPrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllPrinters
   Description: Gets a list of available printers.
   OperationID: GetAllPrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllPrinters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllPrinters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintTestDocument(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintTestDocument
   Description: Prints a pre-defined test document using the supplied info.
   OperationID: PrintTestDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintTestDocument_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintTestDocument_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetPaperSourcesAndSizes(epicorHeaders = None):
   """  
   Summary: Invoke method GetPaperSourcesAndSizes
   Description: Gets the supported paper sources and sizes.
   OperationID: Get_GetPaperSourcesAndSizes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaperSourcesAndSizes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysPrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysPrinter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysPrinterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PaperSizeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PaperSizeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_PaperSourceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_PaperSourceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysPrinterListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysPrinterListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysPrinterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysPrinterRow] = obj["value"]
      pass

class Ice_Tablesets_PaperSizeRow:
   def __init__(self, obj):
      self.Value:str = obj["Value"]
      """  Paper size value.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PaperSourceRow:
   def __init__(self, obj):
      self.Value:str = obj["Value"]
      """  Paper source value.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysPrinterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. (PK)  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.Description:str = obj["Description"]
      """  Printer description  """  
      self.NetworkPath:str = obj["NetworkPath"]
      """  UNC Path of the printer, which must be shared on the network.  """  
      self.PrintCollate:bool = obj["PrintCollate"]
      """  Indicates if the printed document is collated.  """  
      self.PageColor:bool = obj["PageColor"]
      """  Indicates if the page should be printed in color.  """  
      self.PageLandscape:bool = obj["PageLandscape"]
      """  Indicates if the page is printed in landscape or portrait orientation.  """  
      self.PageLeftMargin:int = obj["PageLeftMargin"]
      """  Left margin (in hundredths of an inch) for the page.  """  
      self.PageRightMargin:int = obj["PageRightMargin"]
      """  Right margin (in hundredths of an inch) for the page.  """  
      self.PageTopMargin:int = obj["PageTopMargin"]
      """  Top margin (in hundredths of an inch) for the page.  """  
      self.PageBottomMargin:int = obj["PageBottomMargin"]
      """  Bottom margin (in hundredths of an inch) for the page.  """  
      self.PagePaperSizeKind:str = obj["PagePaperSizeKind"]
      """  Paper Kind.  """  
      self.PagePaperHeight:int = obj["PagePaperHeight"]
      """  Paper Height.  """  
      self.PagePaperWidth:int = obj["PagePaperWidth"]
      """  Paper Width.  """  
      self.PagePaperSourceKind:str = obj["PagePaperSourceKind"]
      """  Specifies the source of the paper.  """  
      self.PagePrinterResolutionX:int = obj["PagePrinterResolutionX"]
      """  Horizontal printer resolution, in dots per inch.  """  
      self.PagePrinterResolutionY:int = obj["PagePrinterResolutionY"]
      """  Vertical printer resolution, in dots per inch.  """  
      self.SRSPrinter:bool = obj["SRSPrinter"]
      """  Flag to indicate printer can be used for SRS printing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysPrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. (PK)  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.Description:str = obj["Description"]
      """  Printer description  """  
      self.NetworkPath:str = obj["NetworkPath"]
      """  UNC Path of the printer, which must be shared on the network.  """  
      self.PrintCollate:bool = obj["PrintCollate"]
      """  Indicates if the printed document is collated.  """  
      self.PageColor:bool = obj["PageColor"]
      """  Indicates if the page should be printed in color.  """  
      self.PageLandscape:bool = obj["PageLandscape"]
      """  Indicates if the page is printed in landscape or portrait orientation.  """  
      self.PageLeftMargin:int = obj["PageLeftMargin"]
      """  Left margin (in hundredths of an inch) for the page.  """  
      self.PageRightMargin:int = obj["PageRightMargin"]
      """  Right margin (in hundredths of an inch) for the page.  """  
      self.PageTopMargin:int = obj["PageTopMargin"]
      """  Top margin (in hundredths of an inch) for the page.  """  
      self.PageBottomMargin:int = obj["PageBottomMargin"]
      """  Bottom margin (in hundredths of an inch) for the page.  """  
      self.PagePaperSizeKind:str = obj["PagePaperSizeKind"]
      """  Paper Kind.  """  
      self.PagePaperHeight:int = obj["PagePaperHeight"]
      """  Paper Height.  """  
      self.PagePaperWidth:int = obj["PagePaperWidth"]
      """  Paper Width.  """  
      self.PagePaperSourceKind:str = obj["PagePaperSourceKind"]
      """  Specifies the source of the paper.  """  
      self.PagePrinterResolutionX:int = obj["PagePrinterResolutionX"]
      """  Horizontal printer resolution, in dots per inch.  """  
      self.PagePrinterResolutionY:int = obj["PagePrinterResolutionY"]
      """  Vertical printer resolution, in dots per inch.  """  
      self.SRSPrinter:bool = obj["SRSPrinter"]
      """  Flag to indicate printer can be used for SRS printing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.EdgePrinter:bool = obj["EdgePrinter"]
      """  EdgePrinter  """  
      self.CanDuplex:bool = obj["CanDuplex"]
      """  CanDuplex  """  
      self.PrinterSetup:bool = obj["PrinterSetup"]
      """  Temp field to indicate printer is setup  """  
      self.PrinterValid:bool = obj["PrinterValid"]
      """  Temp field to indicate printer is valid  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  All Companies Flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   printerID
   """  
   def __init__(self, obj):
      self.printerID:str = obj["printerID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EdgePrintingAvailable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetAllPrinters_input:
   """ Required : 
   whereClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      pass

class GetAllPrinters_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   printerID
   """  
   def __init__(self, obj):
      self.printerID:str = obj["printerID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysPrinterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysPrinter_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysPrinterTableset] = obj["ds"]
      pass

class GetNewSysPrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysPrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPaperSourcesAndSizes_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
      pass

class GetPrintersFromEdgeAgents_input:
   """ Required : 
   agentID
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      """  The agent ID.  Typically in the format of '<serverName>-EdgeAgent'</serverName>  """  
      pass

class GetPrintersFromEdgeAgents_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_EdgePrinterListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseSysPrinter
   whereClausePaperSize
   whereClausePaperSource
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysPrinter:str = obj["whereClauseSysPrinter"]
      self.whereClausePaperSize:str = obj["whereClausePaperSize"]
      self.whereClausePaperSource:str = obj["whereClausePaperSource"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysPrinterTableset] = obj["returnObj"]
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

class Ice_Tablesets_EdgePrinterListTableset:
   def __init__(self, obj):
      self.EdgePrinter:list[Ice_Tablesets_EdgePrinterRow] = obj["EdgePrinter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_EdgePrinterRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  The printer name.  """  
      self.Driver:str = obj["Driver"]
      """  The driver being used for the printer.  """  
      self.Default:bool = obj["Default"]
      """  Is this the default printer for the machine the edge agent is running on.  """  
      self.Trays:str = obj["Trays"]
      """  Comma delimited list of trays supported by this printer.  """  
      self.Density:int = obj["Density"]
      """  The DPI the printer supports.  """  
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PaperSizeRow:
   def __init__(self, obj):
      self.Value:str = obj["Value"]
      """  Paper size value.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PaperSourceRow:
   def __init__(self, obj):
      self.Value:str = obj["Value"]
      """  Paper source value.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysPrinterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. (PK)  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.Description:str = obj["Description"]
      """  Printer description  """  
      self.NetworkPath:str = obj["NetworkPath"]
      """  UNC Path of the printer, which must be shared on the network.  """  
      self.PrintCollate:bool = obj["PrintCollate"]
      """  Indicates if the printed document is collated.  """  
      self.PageColor:bool = obj["PageColor"]
      """  Indicates if the page should be printed in color.  """  
      self.PageLandscape:bool = obj["PageLandscape"]
      """  Indicates if the page is printed in landscape or portrait orientation.  """  
      self.PageLeftMargin:int = obj["PageLeftMargin"]
      """  Left margin (in hundredths of an inch) for the page.  """  
      self.PageRightMargin:int = obj["PageRightMargin"]
      """  Right margin (in hundredths of an inch) for the page.  """  
      self.PageTopMargin:int = obj["PageTopMargin"]
      """  Top margin (in hundredths of an inch) for the page.  """  
      self.PageBottomMargin:int = obj["PageBottomMargin"]
      """  Bottom margin (in hundredths of an inch) for the page.  """  
      self.PagePaperSizeKind:str = obj["PagePaperSizeKind"]
      """  Paper Kind.  """  
      self.PagePaperHeight:int = obj["PagePaperHeight"]
      """  Paper Height.  """  
      self.PagePaperWidth:int = obj["PagePaperWidth"]
      """  Paper Width.  """  
      self.PagePaperSourceKind:str = obj["PagePaperSourceKind"]
      """  Specifies the source of the paper.  """  
      self.PagePrinterResolutionX:int = obj["PagePrinterResolutionX"]
      """  Horizontal printer resolution, in dots per inch.  """  
      self.PagePrinterResolutionY:int = obj["PagePrinterResolutionY"]
      """  Vertical printer resolution, in dots per inch.  """  
      self.SRSPrinter:bool = obj["SRSPrinter"]
      """  Flag to indicate printer can be used for SRS printing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysPrinterListTableset:
   def __init__(self, obj):
      self.SysPrinterList:list[Ice_Tablesets_SysPrinterListRow] = obj["SysPrinterList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysPrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. (PK)  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.Description:str = obj["Description"]
      """  Printer description  """  
      self.NetworkPath:str = obj["NetworkPath"]
      """  UNC Path of the printer, which must be shared on the network.  """  
      self.PrintCollate:bool = obj["PrintCollate"]
      """  Indicates if the printed document is collated.  """  
      self.PageColor:bool = obj["PageColor"]
      """  Indicates if the page should be printed in color.  """  
      self.PageLandscape:bool = obj["PageLandscape"]
      """  Indicates if the page is printed in landscape or portrait orientation.  """  
      self.PageLeftMargin:int = obj["PageLeftMargin"]
      """  Left margin (in hundredths of an inch) for the page.  """  
      self.PageRightMargin:int = obj["PageRightMargin"]
      """  Right margin (in hundredths of an inch) for the page.  """  
      self.PageTopMargin:int = obj["PageTopMargin"]
      """  Top margin (in hundredths of an inch) for the page.  """  
      self.PageBottomMargin:int = obj["PageBottomMargin"]
      """  Bottom margin (in hundredths of an inch) for the page.  """  
      self.PagePaperSizeKind:str = obj["PagePaperSizeKind"]
      """  Paper Kind.  """  
      self.PagePaperHeight:int = obj["PagePaperHeight"]
      """  Paper Height.  """  
      self.PagePaperWidth:int = obj["PagePaperWidth"]
      """  Paper Width.  """  
      self.PagePaperSourceKind:str = obj["PagePaperSourceKind"]
      """  Specifies the source of the paper.  """  
      self.PagePrinterResolutionX:int = obj["PagePrinterResolutionX"]
      """  Horizontal printer resolution, in dots per inch.  """  
      self.PagePrinterResolutionY:int = obj["PagePrinterResolutionY"]
      """  Vertical printer resolution, in dots per inch.  """  
      self.SRSPrinter:bool = obj["SRSPrinter"]
      """  Flag to indicate printer can be used for SRS printing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.EdgePrinter:bool = obj["EdgePrinter"]
      """  EdgePrinter  """  
      self.CanDuplex:bool = obj["CanDuplex"]
      """  CanDuplex  """  
      self.PrinterSetup:bool = obj["PrinterSetup"]
      """  Temp field to indicate printer is setup  """  
      self.PrinterValid:bool = obj["PrinterValid"]
      """  Temp field to indicate printer is valid  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      """  All Companies Flag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysPrinterTableset:
   def __init__(self, obj):
      self.SysPrinter:list[Ice_Tablesets_SysPrinterRow] = obj["SysPrinter"]
      self.PaperSize:list[Ice_Tablesets_PaperSizeRow] = obj["PaperSize"]
      self.PaperSource:list[Ice_Tablesets_PaperSourceRow] = obj["PaperSource"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtSysPrinterTableset:
   def __init__(self, obj):
      self.SysPrinter:list[Ice_Tablesets_SysPrinterRow] = obj["SysPrinter"]
      self.PaperSize:list[Ice_Tablesets_PaperSizeRow] = obj["PaperSize"]
      self.PaperSource:list[Ice_Tablesets_PaperSourceRow] = obj["PaperSource"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class PrintTestDocument_input:
   """ Required : 
   printerID
   isEdgePrinter
   """  
   def __init__(self, obj):
      self.printerID:str = obj["printerID"]
      """  the printer ID  """  
      self.isEdgePrinter:bool = obj["isEdgePrinter"]
      """  if it is an Edge printer  """  
      pass

class PrintTestDocument_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysPrinterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysPrinterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysPrinterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysPrinterTableset] = obj["ds"]
      pass

      """  output parameters  """  

