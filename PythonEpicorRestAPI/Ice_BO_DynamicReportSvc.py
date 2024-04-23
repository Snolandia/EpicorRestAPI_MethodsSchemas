import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DynamicReportSvc
# Description: The BAQ Report service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynamicReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynamicReports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports",headers=creds) as resp:
           return await resp.json()

async def post_DynamicReports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynamicReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID(BAQRptID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynamicReport item
   Description: Calls GetByID to retrieve the DynamicReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynamicReport
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynamicReports_BAQRptID(BAQRptID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynamicReport for the service
   Description: Calls UpdateExt to update DynamicReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynamicReport
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynamicReports_BAQRptID(BAQRptID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynamicReport item
   Description: Call UpdateExt to delete DynamicReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynamicReport
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptOptionFlds(BAQRptID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQRptOptionFlds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptOptionFlds1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptOptionFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptOptionFlds",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptOptionFld item
   Description: Calls GetByID to retrieve the BAQRptOptionFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptOptionFld1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptFilters(BAQRptID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQRptFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptFilters1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptFilters",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptFilters_BAQRptID_Seq(BAQRptID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptFilter item
   Description: Calls GetByID to retrieve the BAQRptFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptFilter1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptFilters(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptSorts(BAQRptID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQRptSorts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptSorts1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptSorts",headers=creds) as resp:
           return await resp.json()

async def get_DynamicReports_BAQRptID_BAQRptSorts_BAQRptID_SortID(BAQRptID, SortID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptSort item
   Description: Calls GetByID to retrieve the BAQRptSort item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSort1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptSorts(" + BAQRptID + "," + SortID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptOptionFlds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQRptOptionFlds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptOptionFlds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptOptionFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds",headers=creds) as resp:
           return await resp.json()

async def post_BAQRptOptionFlds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptOptionFlds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptOptionFld item
   Description: Calls GetByID to retrieve the BAQRptOptionFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptOptionFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQRptOptionFld for the service
   Description: Calls UpdateExt to update BAQRptOptionFld. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptOptionFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQRptOptionFld item
   Description: Call UpdateExt to delete BAQRptOptionFld item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptOptionFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptFilters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQRptFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptFilters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters",headers=creds) as resp:
           return await resp.json()

async def post_BAQRptFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQRptFilters_BAQRptID_Seq(BAQRptID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptFilter item
   Description: Calls GetByID to retrieve the BAQRptFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptFilter
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQRptFilters_BAQRptID_Seq(BAQRptID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQRptFilter for the service
   Description: Calls UpdateExt to update BAQRptFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptFilter
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQRptFilters_BAQRptID_Seq(BAQRptID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQRptFilter item
   Description: Call UpdateExt to delete BAQRptFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptFilter
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSorts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQRptSorts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptSorts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts",headers=creds) as resp:
           return await resp.json()

async def post_BAQRptSorts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptSorts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSorts_BAQRptID_SortID(BAQRptID, SortID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptSort item
   Description: Calls GetByID to retrieve the BAQRptSort item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSort
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQRptSorts_BAQRptID_SortID(BAQRptID, SortID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQRptSort for the service
   Description: Calls UpdateExt to update BAQRptSort. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptSort
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQRptSorts_BAQRptID_SortID(BAQRptID, SortID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQRptSort item
   Description: Call UpdateExt to delete BAQRptSort item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptSort
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSorts_BAQRptID_SortID_BAQRptSortFlds(BAQRptID, SortID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BAQRptSortFlds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptSortFlds1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")/BAQRptSortFlds",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSorts_BAQRptID_SortID_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID, SortID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptSortFld item
   Description: Calls GetByID to retrieve the BAQRptSortFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSortFld1
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSortFlds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BAQRptSortFlds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptSortFlds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds",headers=creds) as resp:
           return await resp.json()

async def post_BAQRptSortFlds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptSortFlds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID, SortID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BAQRptSortFld item
   Description: Calls GetByID to retrieve the BAQRptSortFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSortFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID, SortID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BAQRptSortFld for the service
   Description: Calls UpdateExt to update BAQRptSortFld. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptSortFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID, SortID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BAQRptSortFld item
   Description: Call UpdateExt to delete BAQRptSortFld item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptSortFld
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param SortID: Desc: SortID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBAQReport, whereClauseBAQRptOptionFld, whereClauseBAQRptFilter, whereClauseBAQRptSort, whereClauseBAQRptSortFld, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseBAQReport=" + whereClauseBAQReport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQRptOptionFld=" + whereClauseBAQRptOptionFld
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQRptFilter=" + whereClauseBAQRptFilter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQRptSort=" + whereClauseBAQRptSort
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBAQRptSortFld=" + whereClauseBAQRptSortFld
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(baQRptID, epicorHeaders = None):
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
   params += "baQRptID=" + baQRptID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CopyReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyReport
   Description: This method makes a copy of an existing DynamicReport
   OperationID: CopyReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForBAQ
   Description: This method returns a list of reports that use a given BAQ
   OperationID: GetListForBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportDynamicReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportDynamicReport
   Description: This method imports a DynamicReport from the passed in dataset.
   OperationID: ImportDynamicReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDynamicReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDynamicReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableFields
   Description: Gets the available query fields with the default report parameter columns.
Check01...10, Character01..05, Number01..05 and Date01..05.
   OperationID: GetAvailableFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportFile
   Description: Reads an imported BAQ report definition (as XML) from a shared folder.
   OperationID: ImportReportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportToFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportToFile
   Description: Exports the BAQ Report definition to an XML file.
   OperationID: ExportToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSsrsConfigurationInformation(epicorHeaders = None):
   """  
   Summary: Invoke method GetSsrsConfigurationInformation
   Description: Gets the SSRS configuration information.
   OperationID: GetSsrsConfigurationInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSsrsConfigurationInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CreateReportFromTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateReportFromTemplate
   Description: Creates the report based on the template.
   OperationID: CreateReportFromTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateReportFromTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateReportFromTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSsrsReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSsrsReport
   Description: Updates the report columns from the BAQ.
   OperationID: UpdateSsrsReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSsrsReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSsrsReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQRptOptionFld(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQRptOptionFld
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptOptionFld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptOptionFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptOptionFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQRptFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQRptFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQRptSort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQRptSort
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBAQRptSortFld(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBAQRptSortFld
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptSortFld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptSortFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptSortFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQReportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQRptFilterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQRptOptionFldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQRptSortFldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BAQRptSortRow] = obj["value"]
      pass

class Ice_Tablesets_BAQReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title for this report  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates the report is a system deliver report.  """  
      self.GlobalReport:bool = obj["GlobalReport"]
      """  true if this report is available to all companies  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title for this report  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Title for the report form  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates the report is a system deliver report.  """  
      self.Completed:bool = obj["Completed"]
      """  true if this report is completed, false if work in process  """  
      self.GlobalReport:bool = obj["GlobalReport"]
      """  true if this report is available to all companies  """  
      self.IsCrystalReport:bool = obj["IsCrystalReport"]
      """  Indicates it is a crystal report.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID.  """  
      self.CrystalReportName:str = obj["CrystalReportName"]
      """  Crystal Report Name  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SSRSReportName:str = obj["SSRSReportName"]
      """  SSRSReportName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.AdapterName:str = obj["AdapterName"]
      """  Adapter Name of the business object  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the Filter  """  
      self.LookupField:str = obj["LookupField"]
      """  The code field for a combobox.  """  
      self.FilterLabel:str = obj["FilterLabel"]
      """  Label of the filter.  """  
      self.TabLabel:str = obj["TabLabel"]
      """  Label that used on the filter panel.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name of the filter  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  GUID of the UI object  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  Indicates if the filter is visible on the UI.  """  
      self.FilterField:str = obj["FilterField"]
      """  Field holding the filter value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the filter is a system delivered filter.  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order number  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.FilterValue:str = obj["FilterValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptOptionFldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the option  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default value for the option.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Option field label.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display Name of the option  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field format  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  GUID of the UI object  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  Indicates if the option is visible on the UI.  """  
      self.DataType:str = obj["DataType"]
      """  Data type of the option field.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the option is a system delivered option.  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order of the option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptSortFldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.SortID:str = obj["SortID"]
      """  The ID for this sort by  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the sort field is a system delivered sort field.  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the Sort Field  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.IsAscending:bool = obj["IsAscending"]
      """  Indicates Ascending sort order when true  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order of the sort field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptSortRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.SortID:str = obj["SortID"]
      """  The ID for this sort by  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the sort is a system delivered sort.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  true if this sort by is the default  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CopyReport_input:
   """ Required : 
   pcSourceRptID
   pcDestRptID
   """  
   def __init__(self, obj):
      self.pcSourceRptID:str = obj["pcSourceRptID"]
      """  The source Report ID  """  
      self.pcDestRptID:str = obj["pcDestRptID"]
      """  The target Report ID  """  
      pass

class CopyReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pbSucceed:bool = obj["pbSucceed"]
      pass

      """  output parameters  """  

class CreateReportFromTemplate_input:
   """ Required : 
   baqRptID
   """  
   def __init__(self, obj):
      self.baqRptID:str = obj["baqRptID"]
      """  The BAQRptID value.  """  
      pass

class CreateReportFromTemplate_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   baQRptID
   """  
   def __init__(self, obj):
      self.baQRptID:str = obj["baQRptID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ExportToFile_input:
   """ Required : 
   baqRptID
   newBaqRptID
   fileName
   """  
   def __init__(self, obj):
      self.baqRptID:str = obj["baqRptID"]
      """  The BAQ Report ID to export.  """  
      self.newBaqRptID:str = obj["newBaqRptID"]
      """  The new BAQ Report ID (or empty if the existing ID is used).  """  
      self.fileName:str = obj["fileName"]
      """  the fileName (relative path in UserData special folder)  """  
      pass

class ExportToFile_output:
   def __init__(self, obj):
      pass

class GetAvailableFields_input:
   """ Required : 
   queryID
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  the  """  
      pass

class GetAvailableFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicQueryTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   baQRptID
   """  
   def __init__(self, obj):
      self.baQRptID:str = obj["baQRptID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DynamicReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_DynamicReportTableset] = obj["returnObj"]
      pass

class GetListForBAQ_input:
   """ Required : 
   pcBAQID
   """  
   def __init__(self, obj):
      self.pcBAQID:str = obj["pcBAQID"]
      """  The BAQ ID  """  
      pass

class GetListForBAQ_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BAQReportListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BAQReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBAQReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

class GetNewBAQReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQRptFilter_input:
   """ Required : 
   ds
   baQRptID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      self.baQRptID:str = obj["baQRptID"]
      pass

class GetNewBAQRptFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQRptOptionFld_input:
   """ Required : 
   ds
   baQRptID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      self.baQRptID:str = obj["baQRptID"]
      pass

class GetNewBAQRptOptionFld_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQRptSortFld_input:
   """ Required : 
   ds
   baQRptID
   sortID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      self.baQRptID:str = obj["baQRptID"]
      self.sortID:str = obj["sortID"]
      pass

class GetNewBAQRptSortFld_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBAQRptSort_input:
   """ Required : 
   ds
   baQRptID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      self.baQRptID:str = obj["baQRptID"]
      pass

class GetNewBAQRptSort_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBAQReport
   whereClauseBAQRptOptionFld
   whereClauseBAQRptFilter
   whereClauseBAQRptSort
   whereClauseBAQRptSortFld
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBAQReport:str = obj["whereClauseBAQReport"]
      self.whereClauseBAQRptOptionFld:str = obj["whereClauseBAQRptOptionFld"]
      self.whereClauseBAQRptFilter:str = obj["whereClauseBAQRptFilter"]
      self.whereClauseBAQRptSort:str = obj["whereClauseBAQRptSort"]
      self.whereClauseBAQRptSortFld:str = obj["whereClauseBAQRptSortFld"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DynamicReportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSsrsConfigurationInformation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ssrsBaseUrl:str = obj["parameters"]
      self.rootFolder:str = obj["parameters"]
      self.webPortalUrl:str = obj["parameters"]
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

class Ice_Tablesets_BAQReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title for this report  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates the report is a system deliver report.  """  
      self.GlobalReport:bool = obj["GlobalReport"]
      """  true if this report is available to all companies  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQReportListTableset:
   def __init__(self, obj):
      self.BAQReportList:list[Ice_Tablesets_BAQReportListRow] = obj["BAQReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BAQReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title for this report  """  
      self.FormTitle:str = obj["FormTitle"]
      """  Title for the report form  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates the report is a system deliver report.  """  
      self.Completed:bool = obj["Completed"]
      """  true if this report is completed, false if work in process  """  
      self.GlobalReport:bool = obj["GlobalReport"]
      """  true if this report is available to all companies  """  
      self.IsCrystalReport:bool = obj["IsCrystalReport"]
      """  Indicates it is a crystal report.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID.  """  
      self.CrystalReportName:str = obj["CrystalReportName"]
      """  Crystal Report Name  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SSRSReportName:str = obj["SSRSReportName"]
      """  SSRSReportName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.AdapterName:str = obj["AdapterName"]
      """  Adapter Name of the business object  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the Filter  """  
      self.LookupField:str = obj["LookupField"]
      """  The code field for a combobox.  """  
      self.FilterLabel:str = obj["FilterLabel"]
      """  Label of the filter.  """  
      self.TabLabel:str = obj["TabLabel"]
      """  Label that used on the filter panel.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name of the filter  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  GUID of the UI object  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  Indicates if the filter is visible on the UI.  """  
      self.FilterField:str = obj["FilterField"]
      """  Field holding the filter value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the filter is a system delivered filter.  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order number  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.FilterValue:str = obj["FilterValue"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptOptionFldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the option  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  Default value for the option.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Option field label.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display Name of the option  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field format  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  GUID of the UI object  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  Indicates if the option is visible on the UI.  """  
      self.DataType:str = obj["DataType"]
      """  Data type of the option field.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the option is a system delivered option.  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order of the option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptSortFldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.SortID:str = obj["SortID"]
      """  The ID for this sort by  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the sort field is a system delivered sort field.  """  
      self.DataTableID:str = obj["DataTableID"]
      """  BAQ Data Table  """  
      self.Seq:int = obj["Seq"]
      """  Sequence of the Sort Field  """  
      self.FieldName:str = obj["FieldName"]
      """  BAQ Field Name  """  
      self.IsAscending:bool = obj["IsAscending"]
      """  Indicates Ascending sort order when true  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DispOrder:int = obj["DispOrder"]
      """  Display order of the sort field  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQRptSortRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.SortID:str = obj["SortID"]
      """  The ID for this sort by  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates if the sort is a system delivered sort.  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  true if this sort by is the default  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TempRowID:str = obj["TempRowID"]
      """  Temp Row ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DynamicQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.AuthorID:str = obj["AuthorID"]
      self.Description:str = obj["Description"]
      self.DisplayPhrase:str = obj["DisplayPhrase"]
      self.IsShared:bool = obj["IsShared"]
      self.Version:str = obj["Version"]
      self.CGCCode:str = obj["CGCCode"]
      self.XCompany:bool = obj["XCompany"]
      self.GlbCompany:str = obj["GlbCompany"]
      self.Updatable:bool = obj["Updatable"]
      self.ExtQuery:bool = obj["ExtQuery"]
      self.ExtDatasourceName:str = obj["ExtDatasourceName"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.Extension:str = obj["Extension"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.SecCode:str = obj["SecCode"]
      self.AllCompanies:bool = obj["AllCompanies"]
      self.UseLiveDB:bool = obj["UseLiveDB"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_DynamicQueryTableset:
   def __init__(self, obj):
      self.DynamicQuery:list[Ice_Tablesets_DynamicQueryRow] = obj["DynamicQuery"]
      self.QueryCtrl:list[Ice_Tablesets_QueryCtrlRow] = obj["QueryCtrl"]
      self.QueryCtrlValues:list[Ice_Tablesets_QueryCtrlValuesRow] = obj["QueryCtrlValues"]
      self.QueryCustomAction:list[Ice_Tablesets_QueryCustomActionRow] = obj["QueryCustomAction"]
      self.QueryExecuteSetting:list[Ice_Tablesets_QueryExecuteSettingRow] = obj["QueryExecuteSetting"]
      self.QueryParameter:list[Ice_Tablesets_QueryParameterRow] = obj["QueryParameter"]
      self.QueryReference:list[Ice_Tablesets_QueryReferenceRow] = obj["QueryReference"]
      self.QueryParameterBinding:list[Ice_Tablesets_QueryParameterBindingRow] = obj["QueryParameterBinding"]
      self.QuerySubQuery:list[Ice_Tablesets_QuerySubQueryRow] = obj["QuerySubQuery"]
      self.QueryRelation:list[Ice_Tablesets_QueryRelationRow] = obj["QueryRelation"]
      self.QueryRelationField:list[Ice_Tablesets_QueryRelationFieldRow] = obj["QueryRelationField"]
      self.QuerySortBy:list[Ice_Tablesets_QuerySortByRow] = obj["QuerySortBy"]
      self.QueryWhereItem:list[Ice_Tablesets_QueryWhereItemRow] = obj["QueryWhereItem"]
      self.QueryGroupBy:list[Ice_Tablesets_QueryGroupByRow] = obj["QueryGroupBy"]
      self.QueryTable:list[Ice_Tablesets_QueryTableRow] = obj["QueryTable"]
      self.QueryField:list[Ice_Tablesets_QueryFieldRow] = obj["QueryField"]
      self.QueryFieldAttribute:list[Ice_Tablesets_QueryFieldAttributeRow] = obj["QueryFieldAttribute"]
      self.QueryFunctionCall:list[Ice_Tablesets_QueryFunctionCallRow] = obj["QueryFunctionCall"]
      self.QueryUpdateField:list[Ice_Tablesets_QueryUpdateFieldRow] = obj["QueryUpdateField"]
      self.QueryUpdateSettings:list[Ice_Tablesets_QueryUpdateSettingsRow] = obj["QueryUpdateSettings"]
      self.QueryValueSetItems:list[Ice_Tablesets_QueryValueSetItemsRow] = obj["QueryValueSetItems"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DynamicReportTableset:
   def __init__(self, obj):
      self.BAQReport:list[Ice_Tablesets_BAQReportRow] = obj["BAQReport"]
      self.BAQRptOptionFld:list[Ice_Tablesets_BAQRptOptionFldRow] = obj["BAQRptOptionFld"]
      self.BAQRptFilter:list[Ice_Tablesets_BAQRptFilterRow] = obj["BAQRptFilter"]
      self.BAQRptSort:list[Ice_Tablesets_BAQRptSortRow] = obj["BAQRptSort"]
      self.BAQRptSortFld:list[Ice_Tablesets_BAQRptSortFldRow] = obj["BAQRptSortFld"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QueryCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ControlID:str = obj["ControlID"]
      self.DataSource:str = obj["DataSource"]
      self.DataType:str = obj["DataType"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.IsMandatory:bool = obj["IsMandatory"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.ControlType:str = obj["ControlType"]
      self.SourceType:int = obj["SourceType"]
      self.ListSource:str = obj["ListSource"]
      self.DisplayColumn:str = obj["DisplayColumn"]
      self.ValueColumn:str = obj["ValueColumn"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.Seq:int = obj["Seq"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryCtrlValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ControlID:str = obj["ControlID"]
      self.ID:str = obj["ID"]
      self.Val:str = obj["Val"]
      self.Seq:int = obj["Seq"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryCustomActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ActionID:str = obj["ActionID"]
      self.ActionLabel:str = obj["ActionLabel"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryExecuteSettingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SettingID:str = obj["SettingID"]
      self.SettingValue:str = obj["SettingValue"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryFieldAttributeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.TableID:str = obj["TableID"]
      self.FieldName:str = obj["FieldName"]
      self.AttributeName:str = obj["AttributeName"]
      self.Value:str = obj["Value"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.IsOverriden:bool = obj["IsOverriden"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.TableID:str = obj["TableID"]
      self.FieldName:str = obj["FieldName"]
      self.Seq:int = obj["Seq"]
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.DataType:str = obj["DataType"]
      self.Description:str = obj["Description"]
      self.External:bool = obj["External"]
      self.IsCalculated:bool = obj["IsCalculated"]
      self.Formula:str = obj["Formula"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldSeq:int = obj["LikeDataFieldSeq"]
      self.Aggregation:str = obj["Aggregation"]
      self.IsGroupBy:bool = obj["IsGroupBy"]
      self.UseLike:bool = obj["UseLike"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.Updatable:bool = obj["Updatable"]
      self.RaiseEvent:bool = obj["RaiseEvent"]
      self.QuickSearchID:str = obj["QuickSearchID"]
      self.DropDown:bool = obj["DropDown"]
      self.UpdInitExpression:str = obj["UpdInitExpression"]
      self.Alias:str = obj["Alias"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.DisplayName:str = obj["DisplayName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryFunctionCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.FunctionID:str = obj["FunctionID"]
      self.ParameterName:str = obj["ParameterName"]
      self.Seq:int = obj["Seq"]
      self.Value:str = obj["Value"]
      self.DataType:str = obj["DataType"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryGroupByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.GroupByID:str = obj["GroupByID"]
      self.Expression:str = obj["Expression"]
      self.Seq:int = obj["Seq"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryParameterBindingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ReferenceID:str = obj["ReferenceID"]
      self.ParameterID:str = obj["ParameterID"]
      self.MappingType:str = obj["MappingType"]
      self.MappingValue:str = obj["MappingValue"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryParameterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ParameterID:str = obj["ParameterID"]
      self.ParameterType:str = obj["ParameterType"]
      self.ParameterLabel:str = obj["ParameterLabel"]
      self.SkipIfEmpty:bool = obj["SkipIfEmpty"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryReferenceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ReferenceID:str = obj["ReferenceID"]
      self.ReferenceName:str = obj["ReferenceName"]
      self.RefQueryID:str = obj["RefQueryID"]
      self.ExecType:str = obj["ExecType"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryRelationFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.RelationID:str = obj["RelationID"]
      self.Seq:int = obj["Seq"]
      self.ParentFieldName:str = obj["ParentFieldName"]
      self.ParentFieldDataType:str = obj["ParentFieldDataType"]
      self.ParentFieldIsExpr:bool = obj["ParentFieldIsExpr"]
      self.ChildFieldName:str = obj["ChildFieldName"]
      self.ChildFieldDataType:str = obj["ChildFieldDataType"]
      self.ChildFieldIsExpr:bool = obj["ChildFieldIsExpr"]
      self.AndOr:str = obj["AndOr"]
      self.Neg:bool = obj["Neg"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.CompOp:str = obj["CompOp"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryRelationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.RelationID:str = obj["RelationID"]
      self.IsFK:bool = obj["IsFK"]
      self.ParentTableID:str = obj["ParentTableID"]
      self.ChildTableID:str = obj["ChildTableID"]
      self.JoinType:str = obj["JoinType"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.OuterJoin:bool = obj["OuterJoin"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QuerySortByRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.TableID:str = obj["TableID"]
      self.FieldName:str = obj["FieldName"]
      self.Seq:int = obj["Seq"]
      self.IsAsc:bool = obj["IsAsc"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.DisplayName:str = obj["DisplayName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QuerySubQueryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.Name:str = obj["Name"]
      self.Type:str = obj["Type"]
      self.Seq:int = obj["Seq"]
      self.IsUnion:bool = obj["IsUnion"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.SelectListClause:str = obj["SelectListClause"]
      self.TopRowExpr:int = obj["TopRowExpr"]
      self.TopInPercent:bool = obj["TopInPercent"]
      self.TopWithTies:bool = obj["TopWithTies"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.OrderByOffSet:str = obj["OrderByOffSet"]
      self.OrderByFetch:str = obj["OrderByFetch"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.TableID:str = obj["TableID"]
      self.Seq:int = obj["Seq"]
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.DBTableName:str = obj["DBTableName"]
      self.TableType:str = obj["TableType"]
      self.IsSummaryTable:bool = obj["IsSummaryTable"]
      self.IsVisibleInDesigner:bool = obj["IsVisibleInDesigner"]
      self.Modifiers:str = obj["Modifiers"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.PivotFunction:str = obj["PivotFunction"]
      self.PivotDataType:str = obj["PivotDataType"]
      self.PivotFieldFormat:str = obj["PivotFieldFormat"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryUpdateFieldRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.MapTableName:str = obj["MapTableName"]
      self.MapFieldName:str = obj["MapFieldName"]
      self.Direction:bool = obj["Direction"]
      self.Expression:str = obj["Expression"]
      self.IsKeyField:bool = obj["IsKeyField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.NetDataType:str = obj["NetDataType"]
      self.DataType:str = obj["DataType"]
      self.QualifiedName:str = obj["QualifiedName"]
      self.Required:bool = obj["Required"]
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryUpdateSettingsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.AllowAddNew:bool = obj["AllowAddNew"]
      self.AddNewLabel:str = obj["AddNewLabel"]
      self.SupportMDR:bool = obj["SupportMDR"]
      self.UpdatableType:str = obj["UpdatableType"]
      self.UpdatableBO:str = obj["UpdatableBO"]
      self.BOSystemCode:str = obj["BOSystemCode"]
      self.UpdateMethod:str = obj["UpdateMethod"]
      self.SCUrl:str = obj["SCUrl"]
      self.SCWorkflow:str = obj["SCWorkflow"]
      self.SCCtxUser:str = obj["SCCtxUser"]
      self.SCCtxPwd:str = obj["SCCtxPwd"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.SCUserID:str = obj["SCUserID"]
      self.SCPassword:str = obj["SCPassword"]
      self.SCCtxUrl:str = obj["SCCtxUrl"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryValueSetItemsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.ValueSetID:str = obj["ValueSetID"]
      self.ItemValue:str = obj["ItemValue"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_QueryWhereItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QueryID:str = obj["QueryID"]
      self.SubQueryID:str = obj["SubQueryID"]
      self.TableID:str = obj["TableID"]
      self.CriteriaID:str = obj["CriteriaID"]
      self.Seq:int = obj["Seq"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.CompOp:str = obj["CompOp"]
      self.AndOr:str = obj["AndOr"]
      self.Neg:bool = obj["Neg"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.IsConst:bool = obj["IsConst"]
      self.CriteriaType:int = obj["CriteriaType"]
      self.ToTableID:str = obj["ToTableID"]
      self.ToFieldName:str = obj["ToFieldName"]
      self.ToDataType:str = obj["ToDataType"]
      self.RValue:str = obj["RValue"]
      self.ExtSecurity:bool = obj["ExtSecurity"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_Tablesets_UpdExtDynamicReportTableset:
   def __init__(self, obj):
      self.BAQReport:list[Ice_Tablesets_BAQReportRow] = obj["BAQReport"]
      self.BAQRptOptionFld:list[Ice_Tablesets_BAQRptOptionFldRow] = obj["BAQRptOptionFld"]
      self.BAQRptFilter:list[Ice_Tablesets_BAQRptFilterRow] = obj["BAQRptFilter"]
      self.BAQRptSort:list[Ice_Tablesets_BAQRptSortRow] = obj["BAQRptSort"]
      self.BAQRptSortFld:list[Ice_Tablesets_BAQRptSortFldRow] = obj["BAQRptSortFld"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportDynamicReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

class ImportDynamicReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      self.bOK:bool = obj["bOK"]
      pass

      """  output parameters  """  

class ImportReportFile_input:
   """ Required : 
   fileName
   baqRptID
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  the server filename (in UserData special folder).  """  
      self.baqRptID:str = obj["baqRptID"]
      """  the BAQ Report ID (overrides the file).  """  
      pass

class ImportReportFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The BAQ Report ID.  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDynamicReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDynamicReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateSsrsReport_input:
   """ Required : 
   baqRptID
   """  
   def __init__(self, obj):
      self.baqRptID:str = obj["baqRptID"]
      """  The BAQRptID value.  """  
      pass

class UpdateSsrsReport_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DynamicReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

