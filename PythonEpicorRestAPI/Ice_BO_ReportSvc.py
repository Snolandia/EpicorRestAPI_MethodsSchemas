import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ReportSvc
# Description: Business Logic for the Report Object.
Report Object establishes the existence of a report.
The following tables comprise a report object
Report, ReportStyle, ReportDefaultStyle.
ReportDefaultStyle is not exposed to the UI. Instead a logical table ReportComp is created.
ReportComp represents if a style is valid for a company and if it's the default for the company.
There is no GetNew methods for ReportComp, all companies are set in the dataset.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Reports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Reports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Reports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports",headers=creds) as resp:
           return await resp.json()

async def post_Reports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Reports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Reports_ReportID(ReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Report item
   Description: Calls GetByID to retrieve the Report item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Report
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Reports_ReportID(ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Report for the service
   Description: Calls UpdateExt to update Report. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Report
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Reports_ReportID(ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Report item
   Description: Call UpdateExt to delete Report item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Report
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Reports_ReportID_ReportStyles(ReportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReportStyles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyles1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")/ReportStyles",headers=creds) as resp:
           return await resp.json()

async def get_Reports_ReportID_ReportStyles_ReportID_StyleNum(ReportID, StyleNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyle item
   Description: Calls GetByID to retrieve the ReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyle1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")/ReportStyles(" + ReportID + "," + StyleNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReportStyles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles",headers=creds) as resp:
           return await resp.json()

async def post_ReportStyles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum(ReportID, StyleNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyle item
   Description: Calls GetByID to retrieve the ReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyle
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReportStyles_ReportID_StyleNum(ReportID, StyleNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReportStyle for the service
   Description: Calls UpdateExt to update ReportStyle. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyle
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReportStyles_ReportID_StyleNum(ReportID, StyleNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReportStyle item
   Description: Call UpdateExt to delete ReportStyle item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyle
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_RptStylePrinters(ReportID, StyleNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptStylePrinters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStylePrinters1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStylePrintersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/RptStylePrinters",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(ReportID, StyleNum, Company, PrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStylePrinter item
   Description: Calls GetByID to retrieve the RptStylePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStylePrinter1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_ReportStyleImages(ReportID, StyleNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReportStyleImages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyleImages1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleImages",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID, StyleNum, ReportStyleImageName, ImageCompany, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyleImage item
   Description: Calls GetByID to retrieve the ReportStyleImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleImage1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param ReportStyleImageName: Desc: ReportStyleImageName   Required: True   Allow empty value : True
      :param ImageCompany: Desc: ImageCompany   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_ReportStyleRules(ReportID, StyleNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReportStyleRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyleRules1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleRules",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyles_ReportID_StyleNum_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID, StyleNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyleRule item
   Description: Calls GetByID to retrieve the ReportStyleRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleRule1
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptStylePrinters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptStylePrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStylePrinters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStylePrintersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters",headers=creds) as resp:
           return await resp.json()

async def post_RptStylePrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStylePrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company, ReportID, StyleNum, PrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptStylePrinter item
   Description: Calls GetByID to retrieve the RptStylePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStylePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company, ReportID, StyleNum, PrinterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptStylePrinter for the service
   Description: Calls UpdateExt to update RptStylePrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStylePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company, ReportID, StyleNum, PrinterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptStylePrinter item
   Description: Call UpdateExt to delete RptStylePrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStylePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyleImages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReportStyleImages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyleImages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages",headers=creds) as resp:
           return await resp.json()

async def post_ReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID, StyleNum, ReportStyleImageName, ImageCompany, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyleImage item
   Description: Calls GetByID to retrieve the ReportStyleImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleImage
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param ReportStyleImageName: Desc: ReportStyleImageName   Required: True   Allow empty value : True
      :param ImageCompany: Desc: ImageCompany   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID, StyleNum, ReportStyleImageName, ImageCompany, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReportStyleImage for the service
   Description: Calls UpdateExt to update ReportStyleImage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyleImage
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param ReportStyleImageName: Desc: ReportStyleImageName   Required: True   Allow empty value : True
      :param ImageCompany: Desc: ImageCompany   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID, StyleNum, ReportStyleImageName, ImageCompany, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReportStyleImage item
   Description: Call UpdateExt to delete ReportStyleImage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyleImage
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param ReportStyleImageName: Desc: ReportStyleImageName   Required: True   Allow empty value : True
      :param ImageCompany: Desc: ImageCompany   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportStyleRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReportStyleRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyleRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules",headers=creds) as resp:
           return await resp.json()

async def post_ReportStyleRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyleRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID, StyleNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportStyleRule item
   Description: Calls GetByID to retrieve the ReportStyleRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleRule
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID, StyleNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReportStyleRule for the service
   Description: Calls UpdateExt to update ReportStyleRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyleRule
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID, StyleNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReportStyleRule item
   Description: Call UpdateExt to delete ReportStyleRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyleRule
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReportComps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReportComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportComps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps",headers=creds) as resp:
           return await resp.json()

async def post_ReportComps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ReportCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReportComps_ReportID_StyleNum_Company(ReportID, StyleNum, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportComp item
   Description: Calls GetByID to retrieve the ReportComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportComp
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ReportCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReportComps_ReportID_StyleNum_Company(ReportID, StyleNum, Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReportComp for the service
   Description: Calls UpdateExt to update ReportComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportComp
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReportComps_ReportID_StyleNum_Company(ReportID, StyleNum, Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReportComp item
   Description: Call UpdateExt to delete ReportComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportComp
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseReport, whereClauseReportStyle, whereClauseRptStylePrinters, whereClauseReportStyleImage, whereClauseReportStyleRule, whereClauseReportComp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseReport=" + whereClauseReport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReportStyle=" + whereClauseReportStyle
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptStylePrinters=" + whereClauseRptStylePrinters
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReportStyleImage=" + whereClauseReportStyleImage
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReportStyleRule=" + whereClauseReportStyleRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReportComp=" + whereClauseReportComp
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_VerifyCertCanBeUsedForReportSigning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyCertCanBeUsedForReportSigning
   Description: Verifies that the specified cert can be used to digitally sign a report PDF.
Cert must have both public and private keys and be flagged as exportable.
   OperationID: VerifyCertCanBeUsedForReportSigning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyCertCanBeUsedForReportSigning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyCertCanBeUsedForReportSigning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOutputEDI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOutputEDI
   Description: Set Default OutputEDI after change RptTypeID
   OperationID: OnChangeOutputEDI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOutputEDI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOutputEDI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultOutputEDI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultOutputEDI
   Description: Get default value for OutputEDI
   OperationID: GetDefaultOutputEDI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultOutputEDI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultOutputEDI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyRptDataDefHasBQAOrEI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyRptDataDefHasBQAOrEI
   Description: Verifies the report data definition has a data source with BAQ or EI.
   OperationID: VerifyRptDataDefHasBQAOrEI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyRptDataDefHasBQAOrEI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyRptDataDefHasBQAOrEI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AnalyzeRptDataDefForBAQandEI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AnalyzeRptDataDefForBAQandEI
   Description: Checks the report data definition has data source with BAQ or EI and that it's only BAQ report definition
   OperationID: AnalyzeRptDataDefForBAQandEI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeRptDataDefForBAQandEI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeRptDataDefForBAQandEI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetReportTypeList
   Description: Use to get a sub delimited list of ReportType.RptTypeID and ReportType.RptTypeDescription.
The Code/Description pairs are delimited by the ~ character.
The Code/Description element is sub delimited by the ` character.
   OperationID: GetReportTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExportReportStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportStyle
   Description: Exports the report style for use by Solution Workbench.
   OperationID: ExportReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasReportStyleImages
   Description: Checks whether report images exist.
   OperationID: HasReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReportStyleBySysRowId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportStyleBySysRowId
   Description: Exports the report style by report style SysRowID for use by Solution Workbench.
   OperationID: ExportReportStyleBySysRowId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportStyleBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyleBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportStylesBySysRowIds(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportStylesBySysRowIds
   Description: Get report styles by report style SysRowIDs for use by Solution Workbench.
   OperationID: GetReportStylesBySysRowIds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStylesBySysRowIds_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStylesBySysRowIds_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportStyle
   Description: Imports the report style.
   OperationID: ImportReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateReportParamsScreen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateReportParamsScreen
   Description: Generate report parameters screen
   OperationID: GenerateReportParamsScreen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateReportParamsScreen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateReportParamsScreen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportStyleImages
   Description: Exports the report style images. This is used by Solution Workbench to export images for a report.
   OperationID: ExportReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportStyleImages
   Description: Imports the specified previously exported data set.
   OperationID: ImportReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableDocumentTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableDocumentTypes
   Description: Gets the available document types for each kind of action.
   OperationID: GetAvailableDocumentTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableDocumentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSsrsReportPageSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSsrsReportPageSettings
   Description: Gets the page settings defined in the SSRS report.
   OperationID: GetSsrsReportPageSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSsrsReportPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSsrsReportPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportsThatDefaultToEmfRenderFormat(epicorHeaders = None):
   """  
   Summary: Invoke method GetReportsThatDefaultToEmfRenderFormat
   Description: Gets the reports that default to EMF render format.
   OperationID: GetReportsThatDefaultToEmfRenderFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportsThatDefaultToEmfRenderFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportSsrsRdl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportSsrsRdl
   Description: Imports the SSRS RDL.
   OperationID: ImportSsrsRdl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportSsrsReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportSsrsReports
   Description: Imports the SSRS reports.
   OperationID: ImportSsrsReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSsrsRdl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSsrsRdl
   Description: Exports the SSRS RDL.
   OperationID: ExportSsrsRdl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadSsrsRdl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadSsrsRdl
   Description: Exports the SSRS RDL.
   OperationID: LoadSsrsRdl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSsrsReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSsrsReports
   Description: Exports the SSRS reports.
   OperationID: ExportSsrsReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrepareZipWithSsrsReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrepareZipWithSsrsReports
   Description: Collect SSRS reports, prepare ZIP file with it and returns server path (in user directory) to zip file
   OperationID: PrepareZipWithSsrsReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareZipWithSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareZipWithSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteZip(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteZip
   Description: Deletes temporary zip file and folder after downloading
   OperationID: DeleteZip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExtractAndUploadReportsZip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExtractAndUploadReportsZip
   Description: Extracts report from uploaded zip file and uploads it to SSRS
   OperationID: ExtractAndUploadReportsZip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExtractAndUploadReportsZip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtractAndUploadReportsZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportStyleRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportStyleRules
   Description: Returns a list of style numbers that have routing rules for the report
   OperationID: GetReportStyleRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStyleRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopySsrsStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopySsrsStyle
   Description: Copies the SSRS report style.
   OperationID: CopySsrsStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopySsrsStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopySsrsStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyBartenderStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyBartenderStyle
   Description: Copies the Bartender report style record.
   OperationID: CopyBartenderStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyBartenderStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyBartenderStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CollectReportsForCopyAndCheckForDuplicates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CollectReportsForCopyAndCheckForDuplicates
   Description: Retrieves the reports that the user wants to copy from SSRS. Also, retrieves any reports that already
exist in the custom folder. If the reports already exist and have been modified, returns the report with the IsDuplicate flag set.
   OperationID: CollectReportsForCopyAndCheckForDuplicates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CollectReportsForCopyAndCheckForDuplicates2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CollectReportsForCopyAndCheckForDuplicates2
   Description: Retrieves the reports that the user wants to copy from SSRS. Also, retrieves any reports that already
exist in the custom folder. If the reports already exist and have been modified, returns the report with the IsDuplicate flag set.
   OperationID: CollectReportsForCopyAndCheckForDuplicates2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSsrsReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSsrsReport
   Description: Creates the SSRS report and adds it to the SSRS reports.
   OperationID: CreateSsrsReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSsrsReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSsrsReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SynchronizeDataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SynchronizeDataset
   Description: Synchronize fields and tables between report definition and SSRS *.rdl file
   OperationID: SynchronizeDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SynchronizeDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SynchronizeDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrinterPageInformation(epicorHeaders = None):
   """  
   Summary: Invoke method GetPrinterPageInformation
   Description: Gets the printer page information for PaperSource and PaperKind. The lists are built
from the .NET enums `System.Drawing.Printing.PaperKind` and
`System.Drawing.Printing.PaperSourceKind`.
   OperationID: GetPrinterPageInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrinterPageInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AnalyzeReportStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AnalyzeReportStyle
   Description: Analyze Report Style and Include Missing Report Data Definition Elements
   OperationID: AnalyzeReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AnalyzeReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyReportStyleRdls(epicorHeaders = None):
   """  
   Summary: Invoke method VerifyReportStyleRdls
   Description: Gets a list of the RDLs missing from all report styles in all the companies in the database.
   OperationID: VerifyReportStyleRdls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyReportStyleRdls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetReportStyleHealthCheckStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportStyleHealthCheckStatus
   Description: Gets the report health check status.
   OperationID: GetReportStyleHealthCheckStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStyleHealthCheckStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleHealthCheckStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCopiedReportFolders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCopiedReportFolders
   Description: Returns the display path for the copied reports. Display path might be different from the actual path
in case of multi-tenancy because the actual path has the tenant identifier in it, while the display path doesn't.
   OperationID: GetCopiedReportFolders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCopiedReportFolders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCopiedReportFolders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDisplayPathWithUpdatedFolderName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDisplayPathWithUpdatedFolderName
   Description: Updates folder name in report paths
   OperationID: GetDisplayPathWithUpdatedFolderName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDisplayPathWithUpdatedFolderName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayPathWithUpdatedFolderName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFolderName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFolderName
   Description: Validates the custom target folder name that the user entered on the UI. Empty string
and special characters are not allowed.
   OperationID: ValidateFolderName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFolderName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFolderName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAutoProgramList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAutoProgramList
   Description: Get list of auto programs installed on the server
   OperationID: GetAutoProgramList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAutoProgramList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultEDIDefinitionFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultEDIDefinitionFileName
   Description: Generate default name for EDI definition file
   OperationID: GetDefaultEDIDefinitionFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultEDIDefinitionFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEDIDefinitionFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateEDIDefinitionFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateEDIDefinitionFile
   Description: Generate EDI Definition file
   OperationID: GenerateEDIDefinitionFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateEDIDefinitionFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateEDIDefinitionFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasMarkupInDirectoryName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasMarkupInDirectoryName
   Description: Checks if the sequence markup is present within the folder names
of the file path.
   OperationID: HasMarkupInDirectoryName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasMarkupInDirectoryName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasMarkupInDirectoryName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAsymmetricCryptoAlgorithmList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAsymmetricCryptoAlgorithmList
   Description: Get the Asymmetric Encryption algorithm list separated by Ice.Constants.ListSeparator.
   OperationID: GetAsymmetricCryptoAlgorithmList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsymmetricCryptoAlgorithmList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportZippedReports(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportZippedReports
   Description: Imports the zipped reports to the SSRS server.
   OperationID: ImportZippedReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportZippedReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportZippedReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReportStyle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReportStyle
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptStylePrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptStylePrinters
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStylePrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptStylePrinters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStylePrinters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReportStyleImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReportStyleImage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyleImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReportStyleImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyleImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReportStyleRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReportStyleRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyleRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReportStyleRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyleRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveReportStyleImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveReportStyleImages
   Description: Retrieves the Ice.Services.BO.ReportSvc.ReportStyleImage rows for the specified report style and synchronizes with the
SSRS *.rdl files to make sure each named image has a row and no extra rows exist.
   OperationID: RetrieveReportStyleImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportCompRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportStyleImageRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportStyleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ReportStyleRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptStylePrintersRow] = obj["value"]
      pass

class Ice_Tablesets_ReportCompRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      self.StyleNum:int = obj["StyleNum"]
      self.Company:str = obj["Company"]
      self.ValidStyle:bool = obj["ValidStyle"]
      self.IsDefault:bool = obj["IsDefault"]
      self.CompanyName:str = obj["CompanyName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportListRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanAutoPrint:bool = obj["CanAutoPrint"]
      """  Indicates if the current report can be auto-printed  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.CanAutoPrint:bool = obj["CanAutoPrint"]
      """  Indicates if the current report can be auto-printed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.ReportStyleImageName:str = obj["ReportStyleImageName"]
      """  ReportStyleImageName  """  
      self.ImageCompany:str = obj["ImageCompany"]
      """  ImageCompany  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ImageContent:str = obj["ImageContent"]
      self.ImageType:str = obj["ImageType"]
      self.CategoryID:str = obj["CategoryID"]
      self.SubcategoryID:str = obj["SubcategoryID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Report Style Description  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Foreign Key to RptDef table.  """  
      self.CompanyList:str = obj["CompanyList"]
      """   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  """  
      self.ServerNum:int = obj["ServerNum"]
      """  This is a Crystal Server Num that is defined in CrystalServer table.  """  
      self.OutputLocation:str = obj["OutputLocation"]
      """   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.StructuredOutputEnabled:bool = obj["StructuredOutputEnabled"]
      """  StructuredOutputEnabled  """  
      self.RequireSubmissionID:bool = obj["RequireSubmissionID"]
      """  RequireSubmissionID  """  
      self.AllowResetAfterSubmit:bool = obj["AllowResetAfterSubmit"]
      """  AllowResetAfterSubmit  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language  """  
      self.FormatCulture:str = obj["FormatCulture"]
      """  Culture Format  """  
      self.StructuredOutputCertificateID:str = obj["StructuredOutputCertificateID"]
      """  StructuredOutputCertificateID  """  
      self.StructuredOutputAlgorithm:str = obj["StructuredOutputAlgorithm"]
      """  StructuredOutputAlgorithm  """  
      self.HasBAQOrEI:bool = obj["HasBAQOrEI"]
      """  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  """  
      self.RoutingRuleEnabled:bool = obj["RoutingRuleEnabled"]
      """  Flag to indicate if this report style record has an enabled routing rule.  """  
      self.CertificateIsAllComp:bool = obj["CertificateIsAllComp"]
      """  Digital cert for signing is an All Company cert.  """  
      self.CertificateIsSystem:bool = obj["CertificateIsSystem"]
      """  Indicates the certificate is a system cert.  """  
      self.CertExpiration:str = obj["CertExpiration"]
      """  Certificate expiration date.  """  
      self.Status:int = obj["Status"]
      """  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  """  
      self.StatusMessage:str = obj["StatusMessage"]
      """  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  """  
      self.RptDefSystemFlag:bool = obj["RptDefSystemFlag"]
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.IsBAQReport:bool = obj["IsBAQReport"]
      self.StructuredOutputCertificateIsAllComp:bool = obj["StructuredOutputCertificateIsAllComp"]
      self.StructuredOutputCertificateIsSystem:bool = obj["StructuredOutputCertificateIsSystem"]
      self.StructuredOutputCertificateExpirationDate:str = obj["StructuredOutputCertificateExpirationDate"]
      self.AllowGenerateEDI:bool = obj["AllowGenerateEDI"]
      self.BitFlag:int = obj["BitFlag"]
      self.ReportRptDescription:str = obj["ReportRptDescription"]
      self.RptDefRptDescription:str = obj["RptDefRptDescription"]
      self.RptTypeRptTypeDescription:str = obj["RptTypeRptTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  ZDataTableID  """  
      self.RuleBody:str = obj["RuleBody"]
      """  RuleBody  """  
      self.Thumbnail:str = obj["Thumbnail"]
      """  Thumbnail  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ReportDataDefinitionRptDescription:str = obj["ReportDataDefinitionRptDescription"]
      self.ReportStyleStyleDescription:str = obj["ReportStyleStyleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptStylePrintersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report  ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
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
class AnalyzeReportStyle_input:
   """ Required : 
   reportID
   styleNum
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  The report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  The style number.  """  
      pass

class AnalyzeReportStyle_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The list of changes that were made.  """  
      pass

class AnalyzeRptDataDefForBAQandEI_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  Report Data Definition Id  """  
      pass

class AnalyzeRptDataDefForBAQandEI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.hasBAQorEI:bool = obj["hasBAQorEI"]
      self.isBAQReport:bool = obj["isBAQReport"]
      pass

      """  output parameters  """  

class CollectReportsForCopyAndCheckForDuplicates2_input:
   """ Required : 
   reportID
   styleNum
   printProgram
   ds
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report identifier  """  
      self.styleNum:int = obj["styleNum"]
      """  Report Style  """  
      self.printProgram:str = obj["printProgram"]
      """  ReportStyle.PrintProgram  """  
      self.ds:list[Ice_Tablesets_CopiedReportFoldersTableset] = obj["ds"]
      pass

class CollectReportsForCopyAndCheckForDuplicates2_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  DataSet with the reports that will be copied. A flag indicates if a report already exists in the target folder  """  
      pass

class CollectReportsForCopyAndCheckForDuplicates_input:
   """ Required : 
   reportID
   styleNum
   userEnteredReportLocation
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report identifier  """  
      self.styleNum:int = obj["styleNum"]
      """  Report Style  """  
      self.userEnteredReportLocation      #schema had no properties on an object.
      """  Custom folder path that the user selected on the UI  """  
      pass

class CollectReportsForCopyAndCheckForDuplicates_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  DataSet with the reports that will be copied. A flag indicates if a report already exists in the target folder  """  
      pass

class CopyBartenderStyle_input:
   """ Required : 
   reportID
   styleNum
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  The report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  the style number.  """  
      pass

class CopyBartenderStyle_output:
   def __init__(self, obj):
      pass

class CopySsrsStyle_input:
   """ Required : 
   reportID
   styleNum
   ds
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  The report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  The style number.  """  
      self.ds      #schema had no properties on an object.
      """  The location of the custom reports entered by the user  """  
      pass

class CopySsrsStyle_output:
   def __init__(self, obj):
      pass

class CreateSsrsReport_input:
   """ Required : 
   company
   reportId
   styleNum
   forceOverwrite
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company.  """  
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNum:int = obj["styleNum"]
      """  The style number.  """  
      self.forceOverwrite:bool = obj["forceOverwrite"]
      """  `true` to force overwrite.  """  
      pass

class CreateSsrsReport_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if a new report was created or if report already existed.  """  
      pass

class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteZip_output:
   def __init__(self, obj):
      pass

class ExportReportStyleBySysRowId_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  The report style SysRowID.  """  
      pass

class ExportReportStyleBySysRowId_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

class ExportReportStyleImages_input:
   """ Required : 
   reportId
   styleNumber
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNumber:int = obj["styleNumber"]
      """  The style number.  """  
      pass

class ExportReportStyleImages_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The image information for the specified report style.  """  
      pass

class ExportReportStyle_input:
   """ Required : 
   reportId
   styleNumber
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNumber:int = obj["styleNumber"]
      """  The style number.  """  
      pass

class ExportReportStyle_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

class ExportSsrsRdl_input:
   """ Required : 
   reportPath
   """  
   def __init__(self, obj):
      self.reportPath:str = obj["reportPath"]
      """  The report path.  """  
      pass

class ExportSsrsRdl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The SSRS RDL bytes.  """  
      pass

class ExportSsrsReports_input:
   """ Required : 
   locations
   """  
   def __init__(self, obj):
      self.locations:str = obj["locations"]
      """  The report locations.  """  
      pass

class ExportSsrsReports_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The reports and any sub-reports associated with them.  """  
      pass

class ExtractAndUploadReportsZip_input:
   """ Required : 
   printProgram
   """  
   def __init__(self, obj):
      self.printProgram:str = obj["printProgram"]
      pass

class ExtractAndUploadReportsZip_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of uploaded reports (for display message)  """  
      pass

class GenerateEDIDefinitionFile_input:
   """ Required : 
   reportDefinitionId
   ediDefinitionName
   """  
   def __init__(self, obj):
      self.reportDefinitionId:str = obj["reportDefinitionId"]
      """  Report definition Id  """  
      self.ediDefinitionName:str = obj["ediDefinitionName"]
      """  File name  """  
      pass

class GenerateEDIDefinitionFile_output:
   def __init__(self, obj):
      pass

class GenerateReportParamsScreen_input:
   """ Required : 
   reportID
   cgcCode
   company
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      self.cgcCode:str = obj["cgcCode"]
      self.company:str = obj["company"]
      pass

class GenerateReportParamsScreen_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.warningText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAsymmetricCryptoAlgorithmList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of  Asymmetric Encryption algorithms separated by Ice.Constants.ListSeparator.  """  
      pass

class GetAutoProgramList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  list of auto programs  """  
      pass

class GetAvailableDocumentTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.previewTypes:list = obj[any]
      self.printTypes:list = obj[any]
      self.saveTypes:list = obj[any]
      self.emailTypes:list = obj[any]
      self.electronicComplianceTypes:list = obj[any]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

class GetCopiedReportFolders_input:
   """ Required : 
   printProgram
   """  
   def __init__(self, obj):
      self.printProgram:str = obj["printProgram"]
      """  The reports that are listed on the Report Location field for the report style that is being copied  """  
      pass

class GetCopiedReportFolders_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CopiedReportFoldersTableset] = obj["returnObj"]
      pass

class GetDefaultEDIDefinitionFileName_input:
   """ Required : 
   reportDefinitionId
   styleNum
   printProgramOptions
   """  
   def __init__(self, obj):
      self.reportDefinitionId:str = obj["reportDefinitionId"]
      """  Report Definition Id  """  
      self.styleNum:int = obj["styleNum"]
      """  Style number  """  
      self.printProgramOptions:str = obj["printProgramOptions"]
      """  Print program options  """  
      pass

class GetDefaultEDIDefinitionFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Generated file name  """  
      pass

class GetDefaultOutputEDI_input:
   """ Required : 
   rptTypeID
   """  
   def __init__(self, obj):
      self.rptTypeID:str = obj["rptTypeID"]
      """  Report Type ID  """  
      pass

class GetDefaultOutputEDI_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Default value for OutputEDI  """  
      pass

class GetDisplayPathWithUpdatedFolderName_input:
   """ Required : 
   originalPath
   folderName
   """  
   def __init__(self, obj):
      self.originalPath:str = obj["originalPath"]
      self.folderName:str = obj["folderName"]
      pass

class GetDisplayPathWithUpdatedFolderName_output:
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
      self.returnObj:list[Ice_Tablesets_ReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewReportStyleImage_input:
   """ Required : 
   ds
   reportID
   styleNum
   reportStyleImageName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.styleNum:int = obj["styleNum"]
      self.reportStyleImageName:str = obj["reportStyleImageName"]
      pass

class GetNewReportStyleImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReportStyleRule_input:
   """ Required : 
   ds
   reportID
   styleNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.styleNum:int = obj["styleNum"]
      pass

class GetNewReportStyleRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReportStyle_input:
   """ Required : 
   ds
   reportID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      pass

class GetNewReportStyle_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

class GetNewReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptStylePrinters_input:
   """ Required : 
   ds
   company
   reportID
   styleNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.reportID:str = obj["reportID"]
      self.styleNum:int = obj["styleNum"]
      pass

class GetNewRptStylePrinters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrinterPageInformation_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_Report_PrinterPageInfo] = obj["returnObj"]
      pass

class GetReportStyleHealthCheckStatus_input:
   """ Required : 
   reportId
   styleNum
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      self.styleNum:int = obj["styleNum"]
      pass

class GetReportStyleHealthCheckStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.status:int = obj["parameters"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetReportStyleRules_input:
   """ Required : 
   reportid
   """  
   def __init__(self, obj):
      self.reportid:str = obj["reportid"]
      """  Report ID  """  
      pass

class GetReportStyleRules_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  String array of styles with routing rules  """  
      pass

class GetReportStylesBySysRowIds_input:
   """ Required : 
   sysRowIDs
   """  
   def __init__(self, obj):
      self.sysRowIDs:str = obj["sysRowIDs"]
      """  The report style SysRowIDs.  """  
      pass

class GetReportStylesBySysRowIds_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

class GetReportTypeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetReportsThatDefaultToEmfRenderFormat_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The reports that default to EMF render format.  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseReport
   whereClauseReportStyle
   whereClauseRptStylePrinters
   whereClauseReportStyleImage
   whereClauseReportStyleRule
   whereClauseReportComp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseReport:str = obj["whereClauseReport"]
      self.whereClauseReportStyle:str = obj["whereClauseReportStyle"]
      self.whereClauseRptStylePrinters:str = obj["whereClauseRptStylePrinters"]
      self.whereClauseReportStyleImage:str = obj["whereClauseReportStyleImage"]
      self.whereClauseReportStyleRule:str = obj["whereClauseReportStyleRule"]
      self.whereClauseReportComp:str = obj["whereClauseReportComp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSsrsReportPageSettings_input:
   """ Required : 
   reportLocation
   """  
   def __init__(self, obj):
      self.reportLocation:str = obj["reportLocation"]
      """  The report location. This comes from the ReportStyle.PrintProgram column value.  """  
      pass

class GetSsrsReportPageSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.height:int = obj["parameters"]
      self.width:int = obj["parameters"]
      self.top:int = obj["parameters"]
      self.bottom:int = obj["parameters"]
      self.left:int = obj["parameters"]
      self.right:int = obj["parameters"]
      pass

      """  output parameters  """  

class HasMarkupInDirectoryName_input:
   """ Required : 
   outputLocation
   """  
   def __init__(self, obj):
      self.outputLocation:str = obj["outputLocation"]
      """  Output location.  """  
      pass

class HasMarkupInDirectoryName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `True` if mark up was found within any directory name.  """  
      pass

class HasReportStyleImages_input:
   """ Required : 
   reportID
   styleNumber
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report identifier.  """  
      self.styleNumber:int = obj["styleNumber"]
      """  Style number.  """  
      pass

class HasReportStyleImages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Ice_BO_Report_ErpPaperSourceKind:
   def __init__(self, obj):
      self.SourceName:str = obj["SourceName"]
      self.RawKind:int = obj["RawKind"]
      pass

class Ice_BO_Report_PrinterPageInfo:
   def __init__(self, obj):
      self.PaperSizes:str = obj["PaperSizes"]
      self.PaperSources:list[Ice_BO_Report_ErpPaperSourceKind] = obj["PaperSources"]
      self.DuplexSetting:str = obj["DuplexSetting"]
      pass

class Ice_BO_Report_ReportHealthCheckMissingCatalogItems:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ReportStyleNum:int = obj["ReportStyleNum"]
      self.CatalogItems:str = obj["CatalogItems"]
      pass

class Ice_BO_Report_SsrsReportImportInfo:
   def __init__(self, obj):
      self.ReportFullName:str = obj["ReportFullName"]
      self.Error:str = obj["Error"]
      self.Warnings:str = obj["Warnings"]
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

class Ice_Tablesets_CopiedReportFoldersRow:
   def __init__(self, obj):
      self.Folder:str = obj["Folder"]
      """  Report folder name  """  
      self.CopiedPaths:str = obj["CopiedPaths"]
      """  Paths of the copied reports  """  
      self.OriginalPaths:str = obj["OriginalPaths"]
      """  Paths of the original reports  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CopiedReportFoldersTableset:
   def __init__(self, obj):
      self.CopiedReportFolders:list[Ice_Tablesets_CopiedReportFoldersRow] = obj["CopiedReportFolders"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ReportCompRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      self.StyleNum:int = obj["StyleNum"]
      self.Company:str = obj["Company"]
      self.ValidStyle:bool = obj["ValidStyle"]
      self.IsDefault:bool = obj["IsDefault"]
      self.CompanyName:str = obj["CompanyName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportListRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanAutoPrint:bool = obj["CanAutoPrint"]
      """  Indicates if the current report can be auto-printed  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportListTableset:
   def __init__(self, obj):
      self.ReportList:list[Ice_Tablesets_ReportListRow] = obj["ReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ReportRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.AutoProgram:str = obj["AutoProgram"]
      """  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.CanAutoPrint:bool = obj["CanAutoPrint"]
      """  Indicates if the current report can be auto-printed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleImageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.ReportStyleImageName:str = obj["ReportStyleImageName"]
      """  ReportStyleImageName  """  
      self.ImageCompany:str = obj["ImageCompany"]
      """  ImageCompany  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ImageContent:str = obj["ImageContent"]
      self.ImageType:str = obj["ImageType"]
      self.CategoryID:str = obj["CategoryID"]
      self.SubcategoryID:str = obj["SubcategoryID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Report Style Description  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Foreign Key to RptDef table.  """  
      self.CompanyList:str = obj["CompanyList"]
      """   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  """  
      self.ServerNum:int = obj["ServerNum"]
      """  This is a Crystal Server Num that is defined in CrystalServer table.  """  
      self.OutputLocation:str = obj["OutputLocation"]
      """   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.StructuredOutputEnabled:bool = obj["StructuredOutputEnabled"]
      """  StructuredOutputEnabled  """  
      self.RequireSubmissionID:bool = obj["RequireSubmissionID"]
      """  RequireSubmissionID  """  
      self.AllowResetAfterSubmit:bool = obj["AllowResetAfterSubmit"]
      """  AllowResetAfterSubmit  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language  """  
      self.FormatCulture:str = obj["FormatCulture"]
      """  Culture Format  """  
      self.StructuredOutputCertificateID:str = obj["StructuredOutputCertificateID"]
      """  StructuredOutputCertificateID  """  
      self.StructuredOutputAlgorithm:str = obj["StructuredOutputAlgorithm"]
      """  StructuredOutputAlgorithm  """  
      self.HasBAQOrEI:bool = obj["HasBAQOrEI"]
      """  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  """  
      self.RoutingRuleEnabled:bool = obj["RoutingRuleEnabled"]
      """  Flag to indicate if this report style record has an enabled routing rule.  """  
      self.CertificateIsAllComp:bool = obj["CertificateIsAllComp"]
      """  Digital cert for signing is an All Company cert.  """  
      self.CertificateIsSystem:bool = obj["CertificateIsSystem"]
      """  Indicates the certificate is a system cert.  """  
      self.CertExpiration:str = obj["CertExpiration"]
      """  Certificate expiration date.  """  
      self.Status:int = obj["Status"]
      """  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  """  
      self.StatusMessage:str = obj["StatusMessage"]
      """  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  """  
      self.RptDefSystemFlag:bool = obj["RptDefSystemFlag"]
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.IsBAQReport:bool = obj["IsBAQReport"]
      self.StructuredOutputCertificateIsAllComp:bool = obj["StructuredOutputCertificateIsAllComp"]
      self.StructuredOutputCertificateIsSystem:bool = obj["StructuredOutputCertificateIsSystem"]
      self.StructuredOutputCertificateExpirationDate:str = obj["StructuredOutputCertificateExpirationDate"]
      self.AllowGenerateEDI:bool = obj["AllowGenerateEDI"]
      self.BitFlag:int = obj["BitFlag"]
      self.ReportRptDescription:str = obj["ReportRptDescription"]
      self.RptDefRptDescription:str = obj["RptDefRptDescription"]
      self.RptTypeRptTypeDescription:str = obj["RptTypeRptTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  ZDataTableID  """  
      self.RuleBody:str = obj["RuleBody"]
      """  RuleBody  """  
      self.Thumbnail:str = obj["Thumbnail"]
      """  Thumbnail  """  
      self.IsEnabled:bool = obj["IsEnabled"]
      """  IsEnabled  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ReportDataDefinitionRptDescription:str = obj["ReportDataDefinitionRptDescription"]
      self.ReportStyleStyleDescription:str = obj["ReportStyleStyleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportTableset:
   def __init__(self, obj):
      self.Report:list[Ice_Tablesets_ReportRow] = obj["Report"]
      self.ReportStyle:list[Ice_Tablesets_ReportStyleRow] = obj["ReportStyle"]
      self.RptStylePrinters:list[Ice_Tablesets_RptStylePrintersRow] = obj["RptStylePrinters"]
      self.ReportStyleImage:list[Ice_Tablesets_ReportStyleImageRow] = obj["ReportStyleImage"]
      self.ReportStyleRule:list[Ice_Tablesets_ReportStyleRuleRow] = obj["ReportStyleRule"]
      self.ReportComp:list[Ice_Tablesets_ReportCompRow] = obj["ReportComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptStylePrintersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report  ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.PrinterID:str = obj["PrinterID"]
      """  Printer Identifier. (PK)  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtReportTableset:
   def __init__(self, obj):
      self.Report:list[Ice_Tablesets_ReportRow] = obj["Report"]
      self.ReportStyle:list[Ice_Tablesets_ReportStyleRow] = obj["ReportStyle"]
      self.RptStylePrinters:list[Ice_Tablesets_RptStylePrintersRow] = obj["RptStylePrinters"]
      self.ReportStyleImage:list[Ice_Tablesets_ReportStyleImageRow] = obj["ReportStyleImage"]
      self.ReportStyleRule:list[Ice_Tablesets_ReportStyleRuleRow] = obj["ReportStyleRule"]
      self.ReportComp:list[Ice_Tablesets_ReportCompRow] = obj["ReportComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportReportStyleImages_input:
   """ Required : 
   exportDataSet
   """  
   def __init__(self, obj):
      self.exportDataSet      #schema had no properties on an object.
      """  The previously exported data set.  """  
      pass

class ImportReportStyleImages_output:
   def __init__(self, obj):
      pass

class ImportReportStyle_input:
   """ Required : 
   ds
   allCompanies
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      self.allCompanies:bool = obj["allCompanies"]
      """  If true then import the report style to all companies. Otherwise import the report style only for the current company.  """  
      pass

class ImportReportStyle_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportSsrsRdl_input:
   """ Required : 
   reportPath
   rdlBytes
   """  
   def __init__(self, obj):
      self.reportPath:str = obj["reportPath"]
      """  The report path.  """  
      self.rdlBytes:str = obj["rdlBytes"]
      """  The RDL bytes.  """  
      pass

class ImportSsrsRdl_output:
   def __init__(self, obj):
      pass

class ImportSsrsReports_input:
   """ Required : 
   reports
   """  
   def __init__(self, obj):
      self.reports      #schema had no properties on an object.
      """  The report paths and contents.  """  
      pass

class ImportSsrsReports_output:
   def __init__(self, obj):
      pass

class ImportZippedReports_input:
   """ Required : 
   reportsZip
   previousImportInfos
   """  
   def __init__(self, obj):
      self.reportsZip:str = obj["reportsZip"]
      """  The zipped reports.  """  
      self.previousImportInfos:list[Ice_BO_Report_SsrsReportImportInfo] = obj["previousImportInfos"]
      """  The import information from the previous run. `null` or empty otherwise.  """  
      pass

class ImportZippedReports_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_Report_SsrsReportImportInfo] = obj["returnObj"]
      """  The success and failure information for each of the reports imported.  """  
      pass

class LoadSsrsRdl_input:
   """ Required : 
   fullReportPath
   """  
   def __init__(self, obj):
      self.fullReportPath:str = obj["fullReportPath"]
      """  The full path to the report (not the Display path).  """  
      pass

class LoadSsrsRdl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The SSRS RDL bytes.  """  
      pass

class OnChangeOutputEDI_input:
   """ Required : 
   newRptTypeID
   ds
   """  
   def __init__(self, obj):
      self.newRptTypeID:str = obj["newRptTypeID"]
      """  New Report Type.  """  
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

class OnChangeOutputEDI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrepareZipWithSsrsReports_input:
   """ Required : 
   locations
   """  
   def __init__(self, obj):
      self.locations:str = obj["locations"]
      """  The report locations  """  
      pass

class PrepareZipWithSsrsReports_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Server path to zip file  """  
      pass

class RetrieveReportStyleImages_input:
   """ Required : 
   reportId
   styleNumber
   """  
   def __init__(self, obj):
      self.reportId:str = obj["reportId"]
      """  The report identifier.  """  
      self.styleNumber:int = obj["styleNumber"]
      """  The style number.  """  
      pass

class RetrieveReportStyleImages_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportTableset] = obj["returnObj"]
      pass

class SynchronizeDataset_input:
   """ Required : 
   company
   reportid
   stylenum
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company code  """  
      self.reportid:str = obj["reportid"]
      """  Report ID  """  
      self.stylenum:int = obj["stylenum"]
      """  Style Number  """  
      pass

class SynchronizeDataset_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  synchronization results, i.e. RptTables status.  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFolderName_input:
   """ Required : 
   customReportFolder
   """  
   def __init__(self, obj):
      self.customReportFolder:str = obj["customReportFolder"]
      """  Folder name entered by the user  """  
      pass

class ValidateFolderName_output:
   def __init__(self, obj):
      pass

class VerifyCertCanBeUsedForReportSigning_input:
   """ Required : 
   certificateID
   """  
   def __init__(self, obj):
      self.certificateID:str = obj["certificateID"]
      """  The certificate ID.  """  
      pass

class VerifyCertCanBeUsedForReportSigning_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if the certificate is OK to use, otherwise false.  """  
      pass

class VerifyReportStyleRdls_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_Report_ReportHealthCheckMissingCatalogItems] = obj["returnObj"]
      pass

class VerifyRptDataDefHasBQAOrEI_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  Report Data Definition Id  """  
      pass

class VerifyRptDataDefHasBQAOrEI_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True when report data definition has a data source with BAQ or EI. Otherwise false.  """  
      pass

