import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartAdvisorSvc
# Description: Part Advisor DataSet
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartAdvisors(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAdvisors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAdvisors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors",headers=creds) as resp:
           return await resp.json()

async def get_PartAdvisors_Company_PartNum(Company, PartNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAdvisor item
   Description: Calls GetByID to retrieve the PartAdvisor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAdvisor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartAdvisors_Company_PartNum_PartAttches(Company, PartNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")/PartAttches",headers=creds) as resp:
           return await resp.json()

async def get_PartAdvisors_Company_PartNum_PartAttches_Company_PartNum_DrawingSeq(Company, PartNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAttch item
   Description: Calls GetByID to retrieve the PartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAdvisors(" + Company + "," + PartNum + ")/PartAttches(" + Company + "," + PartNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAttches",headers=creds) as resp:
           return await resp.json()

async def get_PartAttches_Company_PartNum_DrawingSeq(Company, PartNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAttch item
   Description: Calls GetByID to retrieve the PartAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartAttches(" + Company + "," + PartNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcDtlPAs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcDtlPAs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/InvcDtlPAs",headers=creds) as resp:
           return await resp.json()

async def get_InvcDtlPAs_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcDtlPA item
   Description: Calls GetByID to retrieve the InvcDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcDtlPA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/InvcDtlPAs(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_JobHeadPAs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JobHeadPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobHeadPAs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/JobHeadPAs",headers=creds) as resp:
           return await resp.json()

async def get_JobHeadPAs_Company_JobNum(Company, JobNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JobHeadPA item
   Description: Calls GetByID to retrieve the JobHeadPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobHeadPA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JobHeadPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/JobHeadPAs(" + Company + "," + JobNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_OrderDtlPAs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OrderDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OrderDtlPAs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/OrderDtlPAs",headers=creds) as resp:
           return await resp.json()

async def get_OrderDtlPAs_Company_OrderNum_OrderLine(Company, OrderNum, OrderLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OrderDtlPA item
   Description: Calls GetByID to retrieve the OrderDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OrderDtlPA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OrderDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/OrderDtlPAs(" + Company + "," + OrderNum + "," + OrderLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartBins(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartBins
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartBins",headers=creds) as resp:
           return await resp.json()

async def get_PartBins_Company_PartNum_WarehouseCode_BinNum_DimCode_LotNum_PCID_AttributeSetID(Company, PartNum, WarehouseCode, BinNum, DimCode, LotNum, PCID, AttributeSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartBin item
   Description: Calls GetByID to retrieve the PartBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/PartBins(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + DimCode + "," + LotNum + "," + PCID + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlPAs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlPAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlPAs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/QuoteDtlPAs",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlPAs_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlPA item
   Description: Calls GetByID to retrieve the QuoteDtlPA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlPA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlPARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/QuoteDtlPAs(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method returns a list of Parts
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: This method returns a dataset for Part Advisor
   OperationID: GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns a list of Part, including those with blank Company ID
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AfterGetRows(epicorHeaders = None):
   """  
   Summary: Invoke method AfterGetRows
   OperationID: AfterGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AfterGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AllowProfitability(epicorHeaders = None):
   """  
   Summary: Invoke method AllowProfitability
   Description: Allows profitability
   OperationID: AllowProfitability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowProfitability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByIDWithCounters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDWithCounters
   Description: This method returns a dataset for Part Advisor with counters
   OperationID: GetByIDWithCounters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDWithCounters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDWithCounters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcDtlPARows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcDtlPARows
   Description: Searches and fills the InvcDtlPA table with the InvcDtl records that match the given part and the InvoiceType = SHP
   OperationID: GetInvcDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcDtlPAList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcDtlPAList
   Description: Searches and fills the InvcDtlPA table with the InvcDtl records that match the given part and the InvoiceType = SHP
   OperationID: GetInvcDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobHeadPARows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobHeadPARows
   Description: Searches and fills the JobHeadPA table with the JobHead records that match the given part
   OperationID: GetJobHeadPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobHeadPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobHeadPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobHeadPAList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobHeadPAList
   Description: Searches and fills the JobHeadPA table with the JobHead records that match the given part
   OperationID: GetJobHeadPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobHeadPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobHeadPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderDtlPARows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderDtlPARows
   Description: Searches and fills the OrderDtlPA table with the OrderDtl records that match the given part
   OperationID: GetOrderDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrderDtlPAList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrderDtlPAList
   Description: Searches and fills the OrderDtlPA table with the OrderDtl records that match the given part
   OperationID: GetOrderDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrderDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartBinRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartBinRows
   Description: Searches and fills the PartBin table with the PartBin records that match the given part
   OperationID: GetPartBinRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartBinList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartBinList
   Description: Searches and fills the PartBin table with the PartBin records that match the given part
   OperationID: GetPartBinList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartBinList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartBinList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartDetails
   Description: This method returns a list of Parts, including those with blank Company ID
   OperationID: GetPartDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteDtlPARows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteDtlPARows
   Description: Searches and fills the QuoteDtlPA table with the QuoteDtl records that match the given part
   OperationID: GetQuoteDtlPARows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlPARows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlPARows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteDtlPAList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteDtlPAList
   Description: Searches and fills the QuoteDtlPA table with the QuoteDtl records that match the given part
   OperationID: GetQuoteDtlPAList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteDtlPAList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteDtlPAList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: This method finds the actual part number for the entered part and indicates if multiple actual parts match the entered part
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAdvisorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlPARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlPARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadPARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JobHeadPARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderDtlPARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OrderDtlPARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartBinRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartBinRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlPARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlPARow] = obj["value"]
      pass

class Erp_Tablesets_InvcDtlPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RepRate:int = obj["RepRate"]
      """  Sales representative commission rate.  """  
      self.RepSplit:int = obj["RepSplit"]
      self.InvcHeadInvoiceDate:str = obj["InvcHeadInvoiceDate"]
      self.InvcHeadCurrencyCode:str = obj["InvcHeadCurrencyCode"]
      self.InvcHeadCustID:str = obj["InvcHeadCustID"]
      self.InvcHeadCustName:str = obj["InvcHeadCustName"]
      self.TotalCost:int = obj["TotalCost"]
      self.ProfitLoss:int = obj["ProfitLoss"]
      self.ProfitLossPct:int = obj["ProfitLossPct"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.APSUpdatedDate:str = obj["APSUpdatedDate"]
      """  The date that APS updated this record.  If this field is set then APS has scheduled the Job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.APSUpdatedTime:int = obj["APSUpdatedTime"]
      """  The time, in decimal hours, that APS updated the dates and times for this job.  This field is only valid if the APSUpdateDate field is set.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EstTotalCost:int = obj["EstTotalCost"]
      self.ActualTotalCost:int = obj["ActualTotalCost"]
      self.TotalVariance:int = obj["TotalVariance"]
      self.EstLabor:int = obj["EstLabor"]
      self.EstBurden:int = obj["EstBurden"]
      self.EstMaterial:int = obj["EstMaterial"]
      self.EstMtlBurden:int = obj["EstMtlBurden"]
      self.EstSubcontract:int = obj["EstSubcontract"]
      self.ActLabor:int = obj["ActLabor"]
      self.ActBurden:int = obj["ActBurden"]
      self.ActMaterial:int = obj["ActMaterial"]
      self.ActMtlBurden:int = obj["ActMtlBurden"]
      self.ActSubcontract:int = obj["ActSubcontract"]
      self.VarLabor:int = obj["VarLabor"]
      self.VarBurden:int = obj["VarBurden"]
      self.VarMaterial:int = obj["VarMaterial"]
      self.VarMtlBurden:int = obj["VarMtlBurden"]
      self.VarSubcontract:int = obj["VarSubcontract"]
      self.EstSetupHrs:int = obj["EstSetupHrs"]
      self.ActSetupHrs:int = obj["ActSetupHrs"]
      self.EstProdHrs:int = obj["EstProdHrs"]
      self.ActProdHrs:int = obj["ActProdHrs"]
      self.EstTotalHrs:int = obj["EstTotalHrs"]
      self.ActTotalHrs:int = obj["ActTotalHrs"]
      self.VarTotalHrs:int = obj["VarTotalHrs"]
      self.JobAsmblAssemblySeq:int = obj["JobAsmblAssemblySeq"]
      self.JobAsmblEstUnitCost:int = obj["JobAsmblEstUnitCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderDtlPARow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderHedOrderDate:str = obj["OrderHedOrderDate"]
      self.OrderHedPONum:str = obj["OrderHedPONum"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerCustName:str = obj["CustomerCustName"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Phase_c:str = obj["Phase_c"]
      self.ItemID_c:str = obj["ItemID_c"]
      self.TypeCode_c:str = obj["TypeCode_c"]
      self.OrigTypeCode_c:str = obj["OrigTypeCode_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.IndustryShipDate_c:str = obj["IndustryShipDate_c"]
      self.CreateDate_c:str = obj["CreateDate_c"]
      self.PriceUpdateDate_c:str = obj["PriceUpdateDate_c"]
      self.CreatedBy_c:str = obj["CreatedBy_c"]
      self.UpdatedBy_c:str = obj["UpdatedBy_c"]
      pass

class Erp_Tablesets_PartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part Number. It must be valid in the Part table.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """   Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.
Note: With 9.0 the OnHandQty value is in terms of unit of measure (PartBin.DimCode) and does not require any conversion displaying in that uom.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock and of the open job material requirements that are to be issued from stock (JobMtl.Buyit = No) for this Part within a specific bin within the warehouse.  NOTE: This value is the TOTAL of job allocation PartAlloc.  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled by stock in this bin in this warehouse and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of mfg demands on firm jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobHead.Released = No.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Bin in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.ShippingQty:int = obj["ShippingQty"]
      """  Holds the Quantity in the Shipping process in the warehouse from this specific bin location.  """  
      self.PackedQty:int = obj["PackedQty"]
      """  Amount in Bin that is in a Packaging Unit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the PartBin has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.QtyPerPiece:int = obj["QtyPerPiece"]
      """  When tracking inventory attributes this is the quantity per piece in the inventory UOM used to calculate Nbr. Of Pieces.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.HasMRPPlanningAttribute:bool = obj["HasMRPPlanningAttribute"]
      """  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.


Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """   Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.UserChar1:str = obj["UserChar1"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar1Label
is non blank.  """  
      self.UserChar2:str = obj["UserChar2"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar2Label
is non blank.  """  
      self.UserChar3:str = obj["UserChar3"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar3Label
is non blank.  """  
      self.UserChar4:str = obj["UserChar4"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar4Label
is non blank.  """  
      self.UserDate1:str = obj["UserDate1"]
      """   User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate1Label
is non blank.  """  
      self.UserDate2:str = obj["UserDate2"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate2Label is non blank.  """  
      self.UserDate3:str = obj["UserDate3"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate3 Label is non blank.  """  
      self.UserDate4:str = obj["UserDate4"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate4 Label is non blank.  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """   User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec1Label
is non blank.  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec2Label is non blank.  """  
      self.UserDecimal3:int = obj["UserDecimal3"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec3Label is non blank.  """  
      self.UserDecimal4:int = obj["UserDecimal4"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec4Label is non blank.  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt1Label is non blank.  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt2Label is non blank.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """  if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """  The Reason.Code associate with the reason why the part has been placed on hold. Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Default analysis code to be used when this part appears as an assembly  on a quote or a job.  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Current setting for the prefix that will be attached to all new Serial Numbers as they are generated.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """  Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer  """  
      self.Constrained:bool = obj["Constrained"]
      """  Used by the scheduling process when a part is stocked.  When TRUE,  the availability of this Part must be calculated via the TimePhase process prior to scheduling a Job.  """  
      self.UPCCode1:str = obj["UPCCode1"]
      """  UPS / UCC Code required by some industries.  """  
      self.UPCCode2:str = obj["UPCCode2"]
      """  UPS / UCC Code required by some industries.  """  
      self.UPCCode3:str = obj["UPCCode3"]
      """  UPS / UCC Code required by some industries.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.WebInStock:bool = obj["WebInStock"]
      """  For Customer Connect Only.  This field is used in Store Front to indicate if the part is available in stock.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Should this Part be included in Consolidated Purchasing?  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RecDocReq:bool = obj["RecDocReq"]
      """   Receiving Documents Required.
Indicates receiving documents are required when receiving this part.  This pertains only to lot tracked parts that are received to inventory. If checked, then at the time of receiving the system will require that one or more attachments with a reference to a DocType having Receipt = yes be entered.Requires DocManagement license.  """  
      self.MDPV:int = obj["MDPV"]
      """  Maximum daily production value.  Used in demand shipping schedule.  """  
      self.ShipDocReq:bool = obj["ShipDocReq"]
      """   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part. Pertains to Inventory shipments of lot tracked parts or shipments directly from the job only. If checked, then at the time of shipping the system will require that the PartLot.Ship DocsAvail, or JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  """  
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      """  The returnable container for this part when the part needs to be returned.  The value is provided by the trading partner.  """  
      self.NetVolume:int = obj["NetVolume"]
      """  The Part's Net Volume.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  """  
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      """  This field contains the Country of Origin Code from the Country table.  For International shipping.  """  
      self.NAFTAProd:str = obj["NAFTAProd"]
      """  NAFTA Producer Code - For international shipping  """  
      self.NAFTAPref:str = obj["NAFTAPref"]
      """  NAFTA Preference Code  """  
      self.ExpLicType:str = obj["ExpLicType"]
      """  Export License Type  """  
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      """  Export License Number  """  
      self.ECCNNumber:str = obj["ECCNNumber"]
      """  ECCN Number  """  
      self.AESExp:str = obj["AESExp"]
      """  AES Export code  """  
      self.HTS:str = obj["HTS"]
      """  Harmonized Tariff Schedule Code  """  
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      """  Use HTS description flag - for shippers shippers export declaration  """  
      self.SchedBcode:str = obj["SchedBcode"]
      """  Schedule B Code  """  
      self.HazItem:bool = obj["HazItem"]
      """  Hazardous Item  """  
      self.HazTechName:str = obj["HazTechName"]
      """  Hazardous Technical Name  """  
      self.HazClass:str = obj["HazClass"]
      """  Hazardous Class Number  """  
      self.HazSub:str = obj["HazSub"]
      """  Hazardous Subrisk Class  """  
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      """  Hazardous Government Assigned ID  """  
      self.HazPackInstr:str = obj["HazPackInstr"]
      """  Hazardous Packing instructions  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this Part.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the invoice line for this Part.  """  
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      """  Reverse Charge Under Threshold value. If the absolute value of an invoice line is less than the under threshold then the reverse charge tax code will be applied.  """  
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      """  Reverse Charge Over Threshold value. If the absolute value of an invoice line is more than the over threshold then the reverse charge tax code will be applied.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Part. The UOM Class establishes the list of unit of measures that can be used in reference to this part.
Must be valid in the UOMClass table.  """  
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It will be used when defaulting the SNLastUsedSeq field for new PartSite records.  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  """  
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      """   Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotPrefix:str = obj["LotPrefix"]
      """  Defines a prefix to be used when a lot number is generated for the specific part.  """  
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      """  When generating the numeric portion of a lot number it can be either based on a next available number for the part (see Part.LotNextNum) or next available number from a Global Sequence (see LotSeq table and Part.LotSeqID)  """  
      self.LotSeqID:str = obj["LotSeqID"]
      """  The LotSeqID of the LotSeq record to use to retreive next available number when the part is using a Global Sequence  (Part.LotUseGlobalSeq = True). Must be valid in the LotSeq table if Part.LotUseGlobalSeq = True)  """  
      self.LotNxtNum:int = obj["LotNxtNum"]
      """  The next available number to use to generate new lot numbers a part when the  is configured to use "Part Specific" number sequence. (Part.LotUseGlobalSeq = false).  """  
      self.LotDigits:int = obj["LotDigits"]
      """  Number of digits of the Next Avail Lot Number controls that will be used by system Generate lot number logic.  """  
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      """  If leading zeros should be included in the numeric portion of the system generated lot number.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      """   Option to append a trailing date string to the system generated lot number. The Date is the current system date.
Valid options are: None (Default), DD, MM, YYYY, MMYYYY, MM_YYYY, DDMMYYY, DD-MM-YYY, MMDDYYYY, MM-DD-YYYY,  YYYYMMDD, YYYY-MM-DD  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.IsConfigured:bool = obj["IsConfigured"]
      """  Configured Part  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.RefCategory:str = obj["RefCategory"]
      """  The reference category that this Part belongs to.  """  
      self.CSFCJ5:bool = obj["CSFCJ5"]
      """   Malaysia Localization
The flag to indicate that the part is under CJ5 jurisdiction  """  
      self.CSFLMW:bool = obj["CSFLMW"]
      """   Malaysa Localization
The flag to indicate that the part is under LMW jurisdiction  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  The Part's Unit Gross Weight.  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  when creating new part records.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number this part number was generated from.  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      """  Field Service Sales Unit Price  """  
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      """  Indicates the field service sales pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. The initial default is "E".  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required upon receipt.  Inspection will also be enforced if the related Part Class, Vendor, PO Detail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.EstimateID:str = obj["EstimateID"]
      """  EstimateID  """  
      self.EstimateOrPlan:str = obj["EstimateOrPlan"]
      """  EstimateOrPlan  """  
      self.DiffPrc2PrchUOM:bool = obj["DiffPrc2PrchUOM"]
      """  DiffPrc2PrchUOM  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.PricingFactor:int = obj["PricingFactor"]
      """  PricingFactor  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.MobilePart:bool = obj["MobilePart"]
      """  MobilePart  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGUseGoodMark:bool = obj["AGUseGoodMark"]
      """  AGUseGoodMark  """  
      self.AGProductMark:bool = obj["AGProductMark"]
      """  AGProductMark  """  
      self.ISRegion:str = obj["ISRegion"]
      """  ISRegion  """  
      self.INChapterID:str = obj["INChapterID"]
      """  INChapterID  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  CSF Peru -  SUNAT Type  """  
      self.PESUNATUOM:str = obj["PESUNATUOM"]
      """  PESUNATUOM  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.PartLengthWidthHeightUM:str = obj["PartLengthWidthHeightUM"]
      """  PartLengthWidthHeightUM  """  
      self.DiameterUM:str = obj["DiameterUM"]
      """  DiameterUM  """  
      self.DiameterInside:int = obj["DiameterInside"]
      """  DiameterInside  """  
      self.DiameterOutside:int = obj["DiameterOutside"]
      """  DiameterOutside  """  
      self.ThicknessUM:str = obj["ThicknessUM"]
      """  ThicknessUM  """  
      self.Thickness:int = obj["Thickness"]
      """  Thickness  """  
      self.ThicknessMax:int = obj["ThicknessMax"]
      """  ThicknessMax  """  
      self.Durometer:str = obj["Durometer"]
      """  Durometer  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.EngineeringAlert:str = obj["EngineeringAlert"]
      """  EngineeringAlert  """  
      self.Condition:str = obj["Condition"]
      """  Condition  """  
      self.IsCompliant:bool = obj["IsCompliant"]
      """  IsCompliant  """  
      self.IsRestricted:bool = obj["IsRestricted"]
      """  IsRestricted  """  
      self.IsSafetyItem:bool = obj["IsSafetyItem"]
      """  IsSafetyItem  """  
      self.CommercialBrand:str = obj["CommercialBrand"]
      """  CommercialBrand  """  
      self.CommercialSubBrand:str = obj["CommercialSubBrand"]
      """  CommercialSubBrand  """  
      self.CommercialCategory:str = obj["CommercialCategory"]
      """  CommercialCategory  """  
      self.CommercialSubCategory:str = obj["CommercialSubCategory"]
      """  CommercialSubCategory  """  
      self.CommercialStyle:str = obj["CommercialStyle"]
      """  CommercialStyle  """  
      self.CommercialSize1:str = obj["CommercialSize1"]
      """  CommercialSize1  """  
      self.CommercialSize2:str = obj["CommercialSize2"]
      """  CommercialSize2  """  
      self.CommercialColor:str = obj["CommercialColor"]
      """  CommercialColor  """  
      self.IsGiftCard:bool = obj["IsGiftCard"]
      """  IsGiftCard  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  PhotoFile  """  
      self.PartPhotoExists:bool = obj["PartPhotoExists"]
      """  PartPhotoExists  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.PartSpecificPackingUOM:bool = obj["PartSpecificPackingUOM"]
      """  Indicates if the packaging information is part specific or specified at the UOM class level.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  Specification Code for China GTI purposes  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the part  is synchronized to an External CRM.  """  
      self.ExternalCRMPartID:str = obj["ExternalCRMPartID"]
      """  This field holds the id of this part in the External CRM  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the  part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the part needs to be synchronized to the External CRM. If there are changes in the part master file , Epicor ERP automatically turns on this field.  """  
      self.PESUNATTypeCode:str = obj["PESUNATTypeCode"]
      """  PESUNATTypeCode  """  
      self.PESUNATUOMCode:str = obj["PESUNATUOMCode"]
      """  PESUNATUOMCode  """  
      self.CNCodeVersion:str = obj["CNCodeVersion"]
      """  Code Version for China GTI purposes  """  
      self.CNTaxCategoryCode:str = obj["CNTaxCategoryCode"]
      """  Tax Category Code for China GTI purposes  """  
      self.CNHasPreferentialTreatment:bool = obj["CNHasPreferentialTreatment"]
      """  Has Preferential Treatment value for China GTI purposes  """  
      self.CNPreferentialTreatmentContent:str = obj["CNPreferentialTreatmentContent"]
      """  Preferential Treatment Content for China GTI purposes  """  
      self.CNZeroTaxRateMark:str = obj["CNZeroTaxRateMark"]
      """  Zero Tax Rate Mark for China GTI purposes  """  
      self.SubLevelCode:int = obj["SubLevelCode"]
      """  SubLevelCode  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Date the Part was created  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  User the Part was created by  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date/Time when the Part record was updated  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Part has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.FSAItem:bool = obj["FSAItem"]
      """  When the part is marked as Item, it will create an Item Resource in Epicor FSA.  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the part is marked as Equipment, it will create an Equipment Resource Template in Epicor FSA.  """  
      self.BOLClass:str = obj["BOLClass"]
      """  Bill of Lading Class. Additional data for the part required for LTL and International shipments.  """  
      self.FairMarketValue:int = obj["FairMarketValue"]
      """  Fair Market Value. Additional data for the part required for LTL and International shipments.  """  
      self.SAFTProdCategory:str = obj["SAFTProdCategory"]
      """  SAFTProdCategory  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.LocationIDNumReq:bool = obj["LocationIDNumReq"]
      """  Indicates if this part requires Identification Numbers shipment time.  This is disable if Track Location inventory is false.  """  
      self.LocationTrackInv:bool = obj["LocationTrackInv"]
      """  Indicates if this part tracks Location Inventory.  """  
      self.LocationMtlView:bool = obj["LocationMtlView"]
      """  Set the default value of Location View for materials added in Engineering Workbench.  """  
      self.LCNRVReporting:bool = obj["LCNRVReporting"]
      """  LCNRVReporting  """  
      self.LCNRVEstimatedUnitPrice:int = obj["LCNRVEstimatedUnitPrice"]
      """  LCNRVEstimatedUnitPrice  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.LocationFormatID:str = obj["LocationFormatID"]
      """  Default format ID used when assigning ID Numbers.  """  
      self.IsServices:bool = obj["IsServices"]
      """  IsServices  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PEDetrGoodServiceCode  """  
      self.PEProductServiceCode:str = obj["PEProductServiceCode"]
      """  PEProductServiceCode  """  
      self.DualUOMClassID:str = obj["DualUOMClassID"]
      """  Dual UOM Class ID  """  
      self.CNProductName:str = obj["CNProductName"]
      """  Product Name  """  
      self.CNWeight:int = obj["CNWeight"]
      """  Weight  """  
      self.CNWeightUOM:str = obj["CNWeightUOM"]
      """  Unit of Weight  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ISO / IEC 6523  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Part ID  """  
      self.CommoditySchemeID:str = obj["CommoditySchemeID"]
      """  UNTDID 7143  """  
      self.CommoditySchemeVersion:str = obj["CommoditySchemeVersion"]
      """  Part Commodity Scheme Version  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.PlanningByRevision:bool = obj["PlanningByRevision"]
      """  Indicates if this part performs MRP by Revision.  Requires Planning by Revision license.  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMPartType:int = obj["FSMPartType"]
      """  FSMPartType  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.EnableExpressCheckOut:bool = obj["EnableExpressCheckOut"]
      """  Should the Express Part Check Out option be enabled?  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.EnableGlobalPart:bool = obj["EnableGlobalPart"]
      self.EnableInActive:bool = obj["EnableInActive"]
      """  Indicates if the InActive flag should be available for input,  """  
      self.EnableIUM:bool = obj["EnableIUM"]
      """  Flag to tell UI whether the Part.IUM field should be enabled or not.  """  
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Indicates if the Serial Number button should be enabled.  """  
      self.EnableTrackSerialNum:bool = obj["EnableTrackSerialNum"]
      """  This field is used only as a flag to determine in UI, if the Part.TrackSerialNum can be change.  """  
      self.EnableUOMClass:bool = obj["EnableUOMClass"]
      """  Flag to tell UI whether the UOMClassID field should be enabled or not.  """  
      self.ExtCoExist:bool = obj["ExtCoExist"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      """  Default installation price of an equipment that requires installation in Epicor FSA.  """  
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstTypeDesc:str = obj["FSAInstTypeDesc"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Part is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPartNum that is linking to this part  """  
      self.GlbTableAllowUpdTrackDim:bool = obj["GlbTableAllowUpdTrackDim"]
      """  check if TrackDimension is in GlbTable and should be disabled in Part Entry  """  
      self.GlbTableAllowUpdTrackLots:bool = obj["GlbTableAllowUpdTrackLots"]
      """  check if TrackLots is in GlbTable and should be disabled in Part Entry  """  
      self.GlbTableAllowUpdTrackSerial:bool = obj["GlbTableAllowUpdTrackSerial"]
      """  check if TrackSerialNum is in GlbTable and should be disabled in Part Entry  """  
      self.HasOnHandQty:bool = obj["HasOnHandQty"]
      """  Indicates if there is any quantity on hand for this part  """  
      self.IsComponent:bool = obj["IsComponent"]
      """  Indicates if part is a component (has a where used list available)  """  
      self.IsCoPart:bool = obj["IsCoPart"]
      """   This field indicates if the part is being used as a co-part anywhere.  This field will be used to prevent a Part from being marked as serial tracked or configured after being added as a co-part.

CoParts Project.  """  
      self.ISOrigCountryNum:int = obj["ISOrigCountryNum"]
      """  This is the numeric value of ISOrigCountry.  """  
      self.NextGeneratedLotNum:str = obj["NextGeneratedLotNum"]
      """  Shows what the next generated lot number for this part would look like  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      self.PEProductServiceCodeDesc:str = obj["PEProductServiceCodeDesc"]
      self.PLM:bool = obj["PLM"]
      self.PLMEnabled:bool = obj["PLMEnabled"]
      """  Indicates if the PLM toggle box is enabled.  """  
      self.Revision:bool = obj["Revision"]
      """  Revision  """  
      self.SalesUMDisp:str = obj["SalesUMDisp"]
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      self.SNMaskPrefixLength:int = obj["SNMaskPrefixLength"]
      self.SNMaskSuffixLength:int = obj["SNMaskSuffixLength"]
      self.SNNumODigits:int = obj["SNNumODigits"]
      self.UpdatePartPlant:bool = obj["UpdatePartPlant"]
      """  Yes means to copy the NonStock and CostMethod from Part to all the PartPlant records.  """  
      self.UpdateSNPartPlant:bool = obj["UpdateSNPartPlant"]
      """  Indicates whether to update the Part serial number format changes to part plant  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.HasMRPPlanningAttribute:bool = obj["HasMRPPlanningAttribute"]
      """  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  """  
      self.UpdatePartPlantOverride:bool = obj["UpdatePartPlantOverride"]
      self.DEPayStatCodeDescr:str = obj["DEPayStatCodeDescr"]
      """  DEPayStatCode Description  """  
      self.DEDenominationDescr:str = obj["DEDenominationDescr"]
      """  DEDenomination Description  """  
      self.DefaultBuyerName:str = obj["DefaultBuyerName"]
      self.DefaultPlannerName:str = obj["DefaultPlannerName"]
      self.EnableTrackByRevision:bool = obj["EnableTrackByRevision"]
      """  This field is used only as a flag to determine in UI, if the Part.TrackInventoryByRevision can be changed.  """  
      self.LinkedToGlbPart:bool = obj["LinkedToGlbPart"]
      """  indicated if this part has been linked to a global part  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeSuppUnitsUOM:str = obj["CommodityCodeSuppUnitsUOM"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.DualUOMClassIDDescription:str = obj["DualUOMClassIDDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.FSAssetClassCodeFSAssetClassDesc:str = obj["FSAssetClassCodeFSAssetClassDesc"]
      self.Mtl_AnalysisCdDescription:str = obj["Mtl_AnalysisCdDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OnHoldReasonCodeDescription:str = obj["OnHoldReasonCodeDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RefCategoryDescription:str = obj["RefCategoryDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.CustomBuyout_c:bool = obj["CustomBuyout_c"]
      self.NonSellable_c:bool = obj["NonSellable_c"]
      self.WebSearchable_c:bool = obj["WebSearchable_c"]
      pass

class Erp_Tablesets_QuoteDtlPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuoteHedDateQuoted:str = obj["QuoteHedDateQuoted"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustIDBTName:str = obj["CustNumCustIDBTName"]
      self.CustNumCustIDName:str = obj["CustNumCustIDName"]
      self.CustNumCustIDCustID:str = obj["CustNumCustIDCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AfterGetRows_output:
   def __init__(self, obj):
      pass

class AllowProfitability_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_InvcDtlPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RepRate:int = obj["RepRate"]
      """  Sales representative commission rate.  """  
      self.RepSplit:int = obj["RepSplit"]
      self.InvcHeadInvoiceDate:str = obj["InvcHeadInvoiceDate"]
      self.InvcHeadCurrencyCode:str = obj["InvcHeadCurrencyCode"]
      self.InvcHeadCustID:str = obj["InvcHeadCustID"]
      self.InvcHeadCustName:str = obj["InvcHeadCustName"]
      self.TotalCost:int = obj["TotalCost"]
      self.ProfitLoss:int = obj["ProfitLoss"]
      self.ProfitLossPct:int = obj["ProfitLossPct"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobHeadPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.APSUpdatedDate:str = obj["APSUpdatedDate"]
      """  The date that APS updated this record.  If this field is set then APS has scheduled the Job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.APSUpdatedTime:int = obj["APSUpdatedTime"]
      """  The time, in decimal hours, that APS updated the dates and times for this job.  This field is only valid if the APSUpdateDate field is set.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EstTotalCost:int = obj["EstTotalCost"]
      self.ActualTotalCost:int = obj["ActualTotalCost"]
      self.TotalVariance:int = obj["TotalVariance"]
      self.EstLabor:int = obj["EstLabor"]
      self.EstBurden:int = obj["EstBurden"]
      self.EstMaterial:int = obj["EstMaterial"]
      self.EstMtlBurden:int = obj["EstMtlBurden"]
      self.EstSubcontract:int = obj["EstSubcontract"]
      self.ActLabor:int = obj["ActLabor"]
      self.ActBurden:int = obj["ActBurden"]
      self.ActMaterial:int = obj["ActMaterial"]
      self.ActMtlBurden:int = obj["ActMtlBurden"]
      self.ActSubcontract:int = obj["ActSubcontract"]
      self.VarLabor:int = obj["VarLabor"]
      self.VarBurden:int = obj["VarBurden"]
      self.VarMaterial:int = obj["VarMaterial"]
      self.VarMtlBurden:int = obj["VarMtlBurden"]
      self.VarSubcontract:int = obj["VarSubcontract"]
      self.EstSetupHrs:int = obj["EstSetupHrs"]
      self.ActSetupHrs:int = obj["ActSetupHrs"]
      self.EstProdHrs:int = obj["EstProdHrs"]
      self.ActProdHrs:int = obj["ActProdHrs"]
      self.EstTotalHrs:int = obj["EstTotalHrs"]
      self.ActTotalHrs:int = obj["ActTotalHrs"]
      self.VarTotalHrs:int = obj["VarTotalHrs"]
      self.JobAsmblAssemblySeq:int = obj["JobAsmblAssemblySeq"]
      self.JobAsmblEstUnitCost:int = obj["JobAsmblEstUnitCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderDtlPARow:
   def __init__(self, obj):
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RequestDate:str = obj["RequestDate"]
      """   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  """  
      self.AdvanceBillBal:int = obj["AdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  """  
      self.DocAdvanceBillBal:int = obj["DocAdvanceBillBal"]
      """  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  """  
      self.TMBilling:bool = obj["TMBilling"]
      """  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  """  
      self.OrigWhyNoTax:str = obj["OrigWhyNoTax"]
      """  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  """  
      self.Rework:bool = obj["Rework"]
      """   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  """  
      self.RMANum:int = obj["RMANum"]
      """   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  The line item of the RMA detail that this order line item is fulfilling.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this OrderDtl record. Can be blank.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days"," Months", "Years".  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.SellingQuantity:int = obj["SellingQuantity"]
      """  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.ShipLineComplete:bool = obj["ShipLineComplete"]
      """  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order line is linked to an inter-company PO line.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the order line can be changed.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderHedOrderDate:str = obj["OrderHedOrderDate"]
      self.OrderHedPONum:str = obj["OrderHedPONum"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerCustName:str = obj["CustomerCustName"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Phase_c:str = obj["Phase_c"]
      self.ItemID_c:str = obj["ItemID_c"]
      self.TypeCode_c:str = obj["TypeCode_c"]
      self.OrigTypeCode_c:str = obj["OrigTypeCode_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.IndustryShipDate_c:str = obj["IndustryShipDate_c"]
      self.CreateDate_c:str = obj["CreateDate_c"]
      self.PriceUpdateDate_c:str = obj["PriceUpdateDate_c"]
      self.CreatedBy_c:str = obj["CreatedBy_c"]
      self.UpdatedBy_c:str = obj["UpdatedBy_c"]
      pass

class Erp_Tablesets_PartAdvisorListTableset:
   def __init__(self, obj):
      self.PartList:list[Erp_Tablesets_PartListRow] = obj["PartList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAdvisorTableset:
   def __init__(self, obj):
      self.Part:list[Erp_Tablesets_PartRow] = obj["Part"]
      self.PartAttch:list[Erp_Tablesets_PartAttchRow] = obj["PartAttch"]
      self.InvcDtlPA:list[Erp_Tablesets_InvcDtlPARow] = obj["InvcDtlPA"]
      self.JobHeadPA:list[Erp_Tablesets_JobHeadPARow] = obj["JobHeadPA"]
      self.OrderDtlPA:list[Erp_Tablesets_OrderDtlPARow] = obj["OrderDtlPA"]
      self.PartBin:list[Erp_Tablesets_PartBinRow] = obj["PartBin"]
      self.QuoteDtlPA:list[Erp_Tablesets_QuoteDtlPARow] = obj["QuoteDtlPA"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the Part Number. It must be valid in the Part table.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.OnhandQty:int = obj["OnhandQty"]
      """   Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.
Note: With 9.0 the OnHandQty value is in terms of unit of measure (PartBin.DimCode) and does not require any conversion displaying in that uom.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.DimCode:str = obj["DimCode"]
      """  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  A summary of the outstanding quantities for order open sales releases that are being filled from stock and of the open job material requirements that are to be issued from stock (JobMtl.Buyit = No) for this Part within a specific bin within the warehouse.  NOTE: This value is the TOTAL of job allocation PartAlloc.  """  
      self.SalesAllocatedQty:int = obj["SalesAllocatedQty"]
      """  New in 9.00.  A summary of outstanding quantities for order open sales releases that are being filled by stock in this bin in this warehouse and have not been reserved, selected for picking or picked. Calculated as OurStockQty - ReservedQty + PickingQty + PickedQty).  Note: ReservedQty, PickingQty, PickedQty are summaries of PartAlloc records with a blank job,  related to an OrderRel.  The system tracks allocation summaries in the following sequence; AllocQty--> ReservedQty--> PickingQty--> PickedQty.  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobAllocatedQty:int = obj["JobAllocatedQty"]
      """  New in 9.00.  Summary of mfg demands on firm jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobHead.Released = No.  """  
      self.JobPickingQty:int = obj["JobPickingQty"]
      """  Quantity that is in the picking process for jobs. A summary of PartAlloc.PickingQty where PartAlloc.JobNum <> ''.  """  
      self.JobPickedQty:int = obj["JobPickedQty"]
      """  Stock Quantity picked for jobs.  """  
      self.TFOrdAllocatedQty:int = obj["TFOrdAllocatedQty"]
      """  Summary of Transfer Order Allocated Qty for this Part in this Bin in this Warehouse.  """  
      self.TFOrdPickingQty:int = obj["TFOrdPickingQty"]
      """  Quantity that is in the picking process for transfer orders.  A summary of PartAlloc.PickingQty where PartAlloc.TFOrdNum > 0.  """  
      self.TFOrdPickedQty:int = obj["TFOrdPickedQty"]
      """  Stock Quantity picked for transfer orders.  """  
      self.ShippingQty:int = obj["ShippingQty"]
      """  Holds the Quantity in the Shipping process in the warehouse from this specific bin location.  """  
      self.PackedQty:int = obj["PackedQty"]
      """  Amount in Bin that is in a Packaging Unit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the PartBin has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.QtyPerPiece:int = obj["QtyPerPiece"]
      """  When tracking inventory attributes this is the quantity per piece in the inventory UOM used to calculate Nbr. Of Pieces.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.HasMRPPlanningAttribute:bool = obj["HasMRPPlanningAttribute"]
      """  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file. In Part maintenance the Search Word is to only be updated upon initial creation of the Part with the first 8 bytes of the Part.Description.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.ClassID:str = obj["ClassID"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  During Part Maintenance the XaSyst.UM is used as a default for this field. This is used in Purchase Order entry as the default on line item details.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.B = Planning BOM.
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item. This can be used so that "custom" built items which only exist per the customers order can be established as a valid part in order to provide default descriptions etc.... This can also be used for parts that are only purchased for direct use on jobs, but would normally never exist in inventory. This value will be used in report selection criteria.  It also controls the default setting of the "Make" flag in order entry line items  and the "Purchase" flag in Job material records. If a NoStock part is referenced in order entry then it defaults as "Make".  If it is referenced on a job material requirement it will default as "Purchase"  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory. Example is purchased in pounds, stocked in sheets.


Formula: Issue Qty * Conversion Factor = Purchased Qty.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Base Unit Selling Price for the Item. Maintainable only via Part Master Maintenance program. It is used as a default unit price on Sales Order line detail and on Invoice line details that are not referencing a sales order line.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.InternalUnitPrice:int = obj["InternalUnitPrice"]
      """  Base Internal Unit Selling Price for the Item.  Maintainable only via Part Master Maintenance program.  If zero, then the external unit price (Part.UnitPrice) is used.  """  
      self.InternalPricePerCode:str = obj["InternalPricePerCode"]
      """  Indicates the internal pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Maintainable only via Part Maintenance.  The initial default is "E".  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection. Also as a default in order entry, invoice entry and job entry.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job. These are copied to JobHead.Comment, JobAsmbl.Comment,JobMtl.MfgComment depending on the point of reference. Commens are printed on the routing report.  """  
      self.PurComment:str = obj["PurComment"]
      """   Part Comments that will be used as a default for purchasing. These will be copied into the JobMtl.PurComment which then will be used to pass along to the PO when that JobMtl is referenced. It will also be copied into the PODetail.Comment field when the PO is buying the part for stock and not referencing a Job. View as an EDITOR widget.
To be view-as EDITOR widget.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method to be associated with this Part. Use the XaSyst.CostMethod as a default.  When a unit cost is retrieved from the Part file the programs will use this field to determine which one of the Four sets of cost fields should be used.  A = Use Average L= Use Last S = Use Standard T = Use Avg by lot(not found in XaSyst).  """  
      self.UserChar1:str = obj["UserChar1"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar1Label
is non blank.  """  
      self.UserChar2:str = obj["UserChar2"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar2Label
is non blank.  """  
      self.UserChar3:str = obj["UserChar3"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar3Label
is non blank.  """  
      self.UserChar4:str = obj["UserChar4"]
      """   User Defined character field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserChar4Label
is non blank.  """  
      self.UserDate1:str = obj["UserDate1"]
      """   User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate1Label
is non blank.  """  
      self.UserDate2:str = obj["UserDate2"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate2Label is non blank.  """  
      self.UserDate3:str = obj["UserDate3"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate3 Label is non blank.  """  
      self.UserDate4:str = obj["UserDate4"]
      """  User Defined Date field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDate4 Label is non blank.  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """   User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec1Label
is non blank.  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec2Label is non blank.  """  
      self.UserDecimal3:int = obj["UserDecimal3"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec3Label is non blank.  """  
      self.UserDecimal4:int = obj["UserDecimal4"]
      """  User Defined Decimal field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserDec4Label is non blank.  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt1Label is non blank.  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  User Defined Integer field. Actual label used is defined in the XaSyst record. This Field is only accessible if XaSyst.PartUserInt2Label is non blank.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Part. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part Master is considered as "Inactive".
This flag will be used to exclude parts from certain searches and reports.  """  
      self.LowLevelCode:int = obj["LowLevelCode"]
      """  Internally assigned integer which indicates the deepest level of assembly indention that this part is used at.  This is used by the Cost Rollup routines to control the order in which parts get costed. Part at the bottom (highest levelcode) Product structure are calculated first and continues up the chain, with the final assembly parts being processed last.  This insures that when retrieving the cost of an assemblies components the components will already have had their cost rolled up.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.TrackLots:bool = obj["TrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms.
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.DefaultDim:str = obj["DefaultDim"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN). The Commodity Code field can be blank to indicate the value from the part class or must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty for this part  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SalesUM:str = obj["SalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.NetWeight:int = obj["NetWeight"]
      """  The Part's Unit Net Weight.  """  
      self.UsePartRev:bool = obj["UsePartRev"]
      """  if Yes then the part effective revision is used. If No then the revision of the demand source is used (OrderDtl, JobMtl...)  """  
      self.PartsPerContainer:int = obj["PartsPerContainer"]
      """  Default for label printing.  Zero indicates that only one label should be produced for the entire quantity.  """  
      self.PartLength:int = obj["PartLength"]
      """  Part's length.  """  
      self.PartWidth:int = obj["PartWidth"]
      """  Part's width.  """  
      self.PartHeight:int = obj["PartHeight"]
      """  Part's Height.  """  
      self.LotShelfLife:int = obj["LotShelfLife"]
      """  Shelf life of a lot in days.  Zero indicates unlimited shelf life.  """  
      self.WebPart:bool = obj["WebPart"]
      """  This is a Web saleable part  """  
      self.RunOut:bool = obj["RunOut"]
      """  Indicates that the onhand quantity is to be consumed and no further replenishments should be made.  Similar to Obsolete, however only warning messages will be issued to the user if they attempt new references.  """  
      self.SubPart:str = obj["SubPart"]
      """  Indicates the default Substitute part number.  This is optional. Must be one of the related PartSub records.  This field is set indirectly when the user checks the default toggle box in Part Substitution dialog.  """  
      self.Diameter:int = obj["Diameter"]
      """  Part's diameter.  """  
      self.Gravity:int = obj["Gravity"]
      """  Part's gravity.  """  
      self.OnHold:bool = obj["OnHold"]
      """  Indicates that the part is on hold.  This feature can be used to indicate that a new part is not yet approved, that it is being phased out, has a quality issue, etc.  Further demands/supplies of this part should not be made. Similar to an "Inactive" part. However at the moment it still may have an onhand balance, supply and demands and will be reflected in stock status reporting.  """  
      self.OnHoldDate:str = obj["OnHoldDate"]
      """  Date that part becomes obsolete.  This can be set to a future date when the part should become obsolete.  """  
      self.OnHoldReasonCode:str = obj["OnHoldReasonCode"]
      """  The Reason.Code associate with the reason why the part has been placed on hold. Valid only when Part.OnHold = Yes.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Default analysis code to be used when this part appears as an assembly  on a quote or a job.  """  
      self.GlobalPart:bool = obj["GlobalPart"]
      """  Marks the Part as a global Part, available to be sent out to other companies  """  
      self.MtlAnalysisCode:str = obj["MtlAnalysisCode"]
      """  MtlAnalysisCode  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.ISSuppUnitsFactor:int = obj["ISSuppUnitsFactor"]
      """  This value is used to calculate the Supplementary Units for the Intrastat.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path & filename (relative to images/prod_img directory on Web Server) of .jpg product image file.  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Current setting for the prefix that will be attached to all new Serial Numbers as they are generated.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """  Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer  """  
      self.Constrained:bool = obj["Constrained"]
      """  Used by the scheduling process when a part is stocked.  When TRUE,  the availability of this Part must be calculated via the TimePhase process prior to scheduling a Job.  """  
      self.UPCCode1:str = obj["UPCCode1"]
      """  UPS / UCC Code required by some industries.  """  
      self.UPCCode2:str = obj["UPCCode2"]
      """  UPS / UCC Code required by some industries.  """  
      self.UPCCode3:str = obj["UPCCode3"]
      """  UPS / UCC Code required by some industries.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.WebInStock:bool = obj["WebInStock"]
      """  For Customer Connect Only.  This field is used in Store Front to indicate if the part is available in stock.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Should this Part be included in Consolidated Purchasing?  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Purchasing Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Selling Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RecDocReq:bool = obj["RecDocReq"]
      """   Receiving Documents Required.
Indicates receiving documents are required when receiving this part.  This pertains only to lot tracked parts that are received to inventory. If checked, then at the time of receiving the system will require that one or more attachments with a reference to a DocType having Receipt = yes be entered.Requires DocManagement license.  """  
      self.MDPV:int = obj["MDPV"]
      """  Maximum daily production value.  Used in demand shipping schedule.  """  
      self.ShipDocReq:bool = obj["ShipDocReq"]
      """   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part. Pertains to Inventory shipments of lot tracked parts or shipments directly from the job only. If checked, then at the time of shipping the system will require that the PartLot.Ship DocsAvail, or JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  """  
      self.ReturnableContainer:str = obj["ReturnableContainer"]
      """  The returnable container for this part when the part needs to be returned.  The value is provided by the trading partner.  """  
      self.NetVolume:int = obj["NetVolume"]
      """  The Part's Net Volume.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part. Works in conjunction with the Non-Stock field to enable the part master parts to be setup for expense items.  Quantity Bearing will be set to Yes by default and only enable to be set to No if the Non-Stock flag is Yes.  """  
      self.NAFTAOrigCountry:str = obj["NAFTAOrigCountry"]
      """  This field contains the Country of Origin Code from the Country table.  For International shipping.  """  
      self.NAFTAProd:str = obj["NAFTAProd"]
      """  NAFTA Producer Code - For international shipping  """  
      self.NAFTAPref:str = obj["NAFTAPref"]
      """  NAFTA Preference Code  """  
      self.ExpLicType:str = obj["ExpLicType"]
      """  Export License Type  """  
      self.ExpLicNumber:str = obj["ExpLicNumber"]
      """  Export License Number  """  
      self.ECCNNumber:str = obj["ECCNNumber"]
      """  ECCN Number  """  
      self.AESExp:str = obj["AESExp"]
      """  AES Export code  """  
      self.HTS:str = obj["HTS"]
      """  Harmonized Tariff Schedule Code  """  
      self.UseHTSDesc:bool = obj["UseHTSDesc"]
      """  Use HTS description flag - for shippers shippers export declaration  """  
      self.SchedBcode:str = obj["SchedBcode"]
      """  Schedule B Code  """  
      self.HazItem:bool = obj["HazItem"]
      """  Hazardous Item  """  
      self.HazTechName:str = obj["HazTechName"]
      """  Hazardous Technical Name  """  
      self.HazClass:str = obj["HazClass"]
      """  Hazardous Class Number  """  
      self.HazSub:str = obj["HazSub"]
      """  Hazardous Subrisk Class  """  
      self.HazGvrnmtID:str = obj["HazGvrnmtID"]
      """  Hazardous Government Assigned ID  """  
      self.HazPackInstr:str = obj["HazPackInstr"]
      """  Hazardous Packing instructions  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this Part.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the invoice line for this Part.  """  
      self.RCUnderThreshold:int = obj["RCUnderThreshold"]
      """  Reverse Charge Under Threshold value. If the absolute value of an invoice line is less than the under threshold then the reverse charge tax code will be applied.  """  
      self.RCOverThreshold:int = obj["RCOverThreshold"]
      """  Reverse Charge Over Threshold value. If the absolute value of an invoice line is more than the over threshold then the reverse charge tax code will be applied.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Part. The UOM Class establishes the list of unit of measures that can be used in reference to this part.
Must be valid in the UOMClass table.  """  
      self.SNMask:str = obj["SNMask"]
      """  This is the ID by which the user will reference a particular serial number format mask.  """  
      self.SNMaskExample:str = obj["SNMaskExample"]
      """  BL-generated example of the serial number mask if SNBaseDataType = Mask.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers currently used only by SNBaseStructure Mask types.  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types.  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It will be used when defaulting the SNLastUsedSeq field for new PartSite records.  """  
      self.UseMaskSeq:bool = obj["UseMaskSeq"]
      """  Indicates to use the value in SerialMask.SNLastUsedSeq when generating the next serial number for a Generate Mask type.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  """  
      self.NetVolumeUOM:str = obj["NetVolumeUOM"]
      """   Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts.  """  
      self.LotPrefix:str = obj["LotPrefix"]
      """  Defines a prefix to be used when a lot number is generated for the specific part.  """  
      self.LotUseGlobalSeq:bool = obj["LotUseGlobalSeq"]
      """  When generating the numeric portion of a lot number it can be either based on a next available number for the part (see Part.LotNextNum) or next available number from a Global Sequence (see LotSeq table and Part.LotSeqID)  """  
      self.LotSeqID:str = obj["LotSeqID"]
      """  The LotSeqID of the LotSeq record to use to retreive next available number when the part is using a Global Sequence  (Part.LotUseGlobalSeq = True). Must be valid in the LotSeq table if Part.LotUseGlobalSeq = True)  """  
      self.LotNxtNum:int = obj["LotNxtNum"]
      """  The next available number to use to generate new lot numbers a part when the  is configured to use "Part Specific" number sequence. (Part.LotUseGlobalSeq = false).  """  
      self.LotDigits:int = obj["LotDigits"]
      """  Number of digits of the Next Avail Lot Number controls that will be used by system Generate lot number logic.  """  
      self.LotLeadingZeros:bool = obj["LotLeadingZeros"]
      """  If leading zeros should be included in the numeric portion of the system generated lot number.  """  
      self.LotAppendDate:str = obj["LotAppendDate"]
      """   Option to append a trailing date string to the system generated lot number. The Date is the current system date.
Valid options are: None (Default), DD, MM, YYYY, MMYYYY, MM_YYYY, DDMMYYY, DD-MM-YYY, MMDDYYYY, MM-DD-YYYY,  YYYYMMDD, YYYY-MM-DD  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This flag identifies those parts that will suggest a PO each time than a sales order is created. This flag will be used as a default in the sales order.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This flag identifies those parts that are commonly drop shipped. This flag will be used as a default in the sales order.  """  
      self.IsConfigured:bool = obj["IsConfigured"]
      """  Configured Part  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.RefCategory:str = obj["RefCategory"]
      """  The reference category that this Part belongs to.  """  
      self.CSFCJ5:bool = obj["CSFCJ5"]
      """   Malaysia Localization
The flag to indicate that the part is under CJ5 jurisdiction  """  
      self.CSFLMW:bool = obj["CSFLMW"]
      """   Malaysa Localization
The flag to indicate that the part is under LMW jurisdiction  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  The Part's Unit Gross Weight.  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  when creating new part records.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number this part number was generated from.  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  Class Code Entry Field  """  
      self.FSSalesUnitPrice:int = obj["FSSalesUnitPrice"]
      """  Field Service Sales Unit Price  """  
      self.FSPricePerCode:str = obj["FSPricePerCode"]
      """  Indicates the field service sales pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. The initial default is "E".  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required upon receipt.  Inspection will also be enforced if the related Part Class, Vendor, PO Detail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.EstimateID:str = obj["EstimateID"]
      """  EstimateID  """  
      self.EstimateOrPlan:str = obj["EstimateOrPlan"]
      """  EstimateOrPlan  """  
      self.DiffPrc2PrchUOM:bool = obj["DiffPrc2PrchUOM"]
      """  DiffPrc2PrchUOM  """  
      self.DupOnJobCrt:bool = obj["DupOnJobCrt"]
      """  DupOnJobCrt  """  
      self.PricingFactor:int = obj["PricingFactor"]
      """  PricingFactor  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.MobilePart:bool = obj["MobilePart"]
      """  MobilePart  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGUseGoodMark:bool = obj["AGUseGoodMark"]
      """  AGUseGoodMark  """  
      self.AGProductMark:bool = obj["AGProductMark"]
      """  AGProductMark  """  
      self.ISRegion:str = obj["ISRegion"]
      """  ISRegion  """  
      self.INChapterID:str = obj["INChapterID"]
      """  INChapterID  """  
      self.PESUNATType:str = obj["PESUNATType"]
      """  CSF Peru -  SUNAT Type  """  
      self.PESUNATUOM:str = obj["PESUNATUOM"]
      """  PESUNATUOM  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.PartLengthWidthHeightUM:str = obj["PartLengthWidthHeightUM"]
      """  PartLengthWidthHeightUM  """  
      self.DiameterUM:str = obj["DiameterUM"]
      """  DiameterUM  """  
      self.DiameterInside:int = obj["DiameterInside"]
      """  DiameterInside  """  
      self.DiameterOutside:int = obj["DiameterOutside"]
      """  DiameterOutside  """  
      self.ThicknessUM:str = obj["ThicknessUM"]
      """  ThicknessUM  """  
      self.Thickness:int = obj["Thickness"]
      """  Thickness  """  
      self.ThicknessMax:int = obj["ThicknessMax"]
      """  ThicknessMax  """  
      self.Durometer:str = obj["Durometer"]
      """  Durometer  """  
      self.Specification:str = obj["Specification"]
      """  Specification  """  
      self.EngineeringAlert:str = obj["EngineeringAlert"]
      """  EngineeringAlert  """  
      self.Condition:str = obj["Condition"]
      """  Condition  """  
      self.IsCompliant:bool = obj["IsCompliant"]
      """  IsCompliant  """  
      self.IsRestricted:bool = obj["IsRestricted"]
      """  IsRestricted  """  
      self.IsSafetyItem:bool = obj["IsSafetyItem"]
      """  IsSafetyItem  """  
      self.CommercialBrand:str = obj["CommercialBrand"]
      """  CommercialBrand  """  
      self.CommercialSubBrand:str = obj["CommercialSubBrand"]
      """  CommercialSubBrand  """  
      self.CommercialCategory:str = obj["CommercialCategory"]
      """  CommercialCategory  """  
      self.CommercialSubCategory:str = obj["CommercialSubCategory"]
      """  CommercialSubCategory  """  
      self.CommercialStyle:str = obj["CommercialStyle"]
      """  CommercialStyle  """  
      self.CommercialSize1:str = obj["CommercialSize1"]
      """  CommercialSize1  """  
      self.CommercialSize2:str = obj["CommercialSize2"]
      """  CommercialSize2  """  
      self.CommercialColor:str = obj["CommercialColor"]
      """  CommercialColor  """  
      self.IsGiftCard:bool = obj["IsGiftCard"]
      """  IsGiftCard  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  PhotoFile  """  
      self.PartPhotoExists:bool = obj["PartPhotoExists"]
      """  PartPhotoExists  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.PartSpecificPackingUOM:bool = obj["PartSpecificPackingUOM"]
      """  Indicates if the packaging information is part specific or specified at the UOM class level.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  Specification Code for China GTI purposes  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the part  is synchronized to an External CRM.  """  
      self.ExternalCRMPartID:str = obj["ExternalCRMPartID"]
      """  This field holds the id of this part in the External CRM  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the  part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the part needs to be synchronized to the External CRM. If there are changes in the part master file , Epicor ERP automatically turns on this field.  """  
      self.PESUNATTypeCode:str = obj["PESUNATTypeCode"]
      """  PESUNATTypeCode  """  
      self.PESUNATUOMCode:str = obj["PESUNATUOMCode"]
      """  PESUNATUOMCode  """  
      self.CNCodeVersion:str = obj["CNCodeVersion"]
      """  Code Version for China GTI purposes  """  
      self.CNTaxCategoryCode:str = obj["CNTaxCategoryCode"]
      """  Tax Category Code for China GTI purposes  """  
      self.CNHasPreferentialTreatment:bool = obj["CNHasPreferentialTreatment"]
      """  Has Preferential Treatment value for China GTI purposes  """  
      self.CNPreferentialTreatmentContent:str = obj["CNPreferentialTreatmentContent"]
      """  Preferential Treatment Content for China GTI purposes  """  
      self.CNZeroTaxRateMark:str = obj["CNZeroTaxRateMark"]
      """  Zero Tax Rate Mark for China GTI purposes  """  
      self.SubLevelCode:int = obj["SubLevelCode"]
      """  SubLevelCode  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Date the Part was created  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  User the Part was created by  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Date/Time when the Part record was updated  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Part has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.FSAItem:bool = obj["FSAItem"]
      """  When the part is marked as Item, it will create an Item Resource in Epicor FSA.  """  
      self.FSAEquipment:bool = obj["FSAEquipment"]
      """  When the part is marked as Equipment, it will create an Equipment Resource Template in Epicor FSA.  """  
      self.BOLClass:str = obj["BOLClass"]
      """  Bill of Lading Class. Additional data for the part required for LTL and International shipments.  """  
      self.FairMarketValue:int = obj["FairMarketValue"]
      """  Fair Market Value. Additional data for the part required for LTL and International shipments.  """  
      self.SAFTProdCategory:str = obj["SAFTProdCategory"]
      """  SAFTProdCategory  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.LocationIDNumReq:bool = obj["LocationIDNumReq"]
      """  Indicates if this part requires Identification Numbers shipment time.  This is disable if Track Location inventory is false.  """  
      self.LocationTrackInv:bool = obj["LocationTrackInv"]
      """  Indicates if this part tracks Location Inventory.  """  
      self.LocationMtlView:bool = obj["LocationMtlView"]
      """  Set the default value of Location View for materials added in Engineering Workbench.  """  
      self.LCNRVReporting:bool = obj["LCNRVReporting"]
      """  LCNRVReporting  """  
      self.LCNRVEstimatedUnitPrice:int = obj["LCNRVEstimatedUnitPrice"]
      """  LCNRVEstimatedUnitPrice  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.LocationFormatID:str = obj["LocationFormatID"]
      """  Default format ID used when assigning ID Numbers.  """  
      self.IsServices:bool = obj["IsServices"]
      """  IsServices  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PEDetrGoodServiceCode  """  
      self.PEProductServiceCode:str = obj["PEProductServiceCode"]
      """  PEProductServiceCode  """  
      self.DualUOMClassID:str = obj["DualUOMClassID"]
      """  Dual UOM Class ID  """  
      self.CNProductName:str = obj["CNProductName"]
      """  Product Name  """  
      self.CNWeight:int = obj["CNWeight"]
      """  Weight  """  
      self.CNWeightUOM:str = obj["CNWeightUOM"]
      """  Unit of Weight  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.DefaultAttributeSetID:int = obj["DefaultAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ISO / IEC 6523  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Part ID  """  
      self.CommoditySchemeID:str = obj["CommoditySchemeID"]
      """  UNTDID 7143  """  
      self.CommoditySchemeVersion:str = obj["CommoditySchemeVersion"]
      """  Part Commodity Scheme Version  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.PlanningByRevision:bool = obj["PlanningByRevision"]
      """  Indicates if this part performs MRP by Revision.  Requires Planning by Revision license.  """  
      self.RcvInspectionReqPart:str = obj["RcvInspectionReqPart"]
      """  RcvInspectionReqPart  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMPartType:int = obj["FSMPartType"]
      """  FSMPartType  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.EnableExpressCheckOut:bool = obj["EnableExpressCheckOut"]
      """  Should the Express Part Check Out option be enabled?  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.EnableGlobalPart:bool = obj["EnableGlobalPart"]
      self.EnableInActive:bool = obj["EnableInActive"]
      """  Indicates if the InActive flag should be available for input,  """  
      self.EnableIUM:bool = obj["EnableIUM"]
      """  Flag to tell UI whether the Part.IUM field should be enabled or not.  """  
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Override Reverse Charge check box should be enabled.  """  
      self.EnableSerialNum:bool = obj["EnableSerialNum"]
      """  Indicates if the Serial Number button should be enabled.  """  
      self.EnableTrackSerialNum:bool = obj["EnableTrackSerialNum"]
      """  This field is used only as a flag to determine in UI, if the Part.TrackSerialNum can be change.  """  
      self.EnableUOMClass:bool = obj["EnableUOMClass"]
      """  Flag to tell UI whether the UOMClassID field should be enabled or not.  """  
      self.ExtCoExist:bool = obj["ExtCoExist"]
      self.FSAInstallationCost:int = obj["FSAInstallationCost"]
      """  Default installation price of an equipment that requires installation in Epicor FSA.  """  
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstTypeDesc:str = obj["FSAInstTypeDesc"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Part is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPartNum that is linking to this part  """  
      self.GlbTableAllowUpdTrackDim:bool = obj["GlbTableAllowUpdTrackDim"]
      """  check if TrackDimension is in GlbTable and should be disabled in Part Entry  """  
      self.GlbTableAllowUpdTrackLots:bool = obj["GlbTableAllowUpdTrackLots"]
      """  check if TrackLots is in GlbTable and should be disabled in Part Entry  """  
      self.GlbTableAllowUpdTrackSerial:bool = obj["GlbTableAllowUpdTrackSerial"]
      """  check if TrackSerialNum is in GlbTable and should be disabled in Part Entry  """  
      self.HasOnHandQty:bool = obj["HasOnHandQty"]
      """  Indicates if there is any quantity on hand for this part  """  
      self.IsComponent:bool = obj["IsComponent"]
      """  Indicates if part is a component (has a where used list available)  """  
      self.IsCoPart:bool = obj["IsCoPart"]
      """   This field indicates if the part is being used as a co-part anywhere.  This field will be used to prevent a Part from being marked as serial tracked or configured after being added as a co-part.

CoParts Project.  """  
      self.ISOrigCountryNum:int = obj["ISOrigCountryNum"]
      """  This is the numeric value of ISOrigCountry.  """  
      self.NextGeneratedLotNum:str = obj["NextGeneratedLotNum"]
      """  Shows what the next generated lot number for this part would look like  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      self.PEProductServiceCodeDesc:str = obj["PEProductServiceCodeDesc"]
      self.PLM:bool = obj["PLM"]
      self.PLMEnabled:bool = obj["PLMEnabled"]
      """  Indicates if the PLM toggle box is enabled.  """  
      self.Revision:bool = obj["Revision"]
      """  Revision  """  
      self.SalesUMDisp:str = obj["SalesUMDisp"]
      self.SNLeadingZeros:bool = obj["SNLeadingZeros"]
      self.SNMaskPrefixLength:int = obj["SNMaskPrefixLength"]
      self.SNMaskSuffixLength:int = obj["SNMaskSuffixLength"]
      self.SNNumODigits:int = obj["SNNumODigits"]
      self.UpdatePartPlant:bool = obj["UpdatePartPlant"]
      """  Yes means to copy the NonStock and CostMethod from Part to all the PartPlant records.  """  
      self.UpdateSNPartPlant:bool = obj["UpdateSNPartPlant"]
      """  Indicates whether to update the Part serial number format changes to part plant  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.HasMRPPlanningAttribute:bool = obj["HasMRPPlanningAttribute"]
      """  If this Part is TrackInventoryAttributes = true, and the AttrClassID it is associated to has one or more attributes whose DynAttrClassDtl.UsedInPlanning= true.  """  
      self.UpdatePartPlantOverride:bool = obj["UpdatePartPlantOverride"]
      self.DEPayStatCodeDescr:str = obj["DEPayStatCodeDescr"]
      """  DEPayStatCode Description  """  
      self.DEDenominationDescr:str = obj["DEDenominationDescr"]
      """  DEDenomination Description  """  
      self.DefaultBuyerName:str = obj["DefaultBuyerName"]
      self.DefaultPlannerName:str = obj["DefaultPlannerName"]
      self.EnableTrackByRevision:bool = obj["EnableTrackByRevision"]
      """  This field is used only as a flag to determine in UI, if the Part.TrackInventoryByRevision can be changed.  """  
      self.LinkedToGlbPart:bool = obj["LinkedToGlbPart"]
      """  indicated if this part has been linked to a global part  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeSuppUnitsUOM:str = obj["CommodityCodeSuppUnitsUOM"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.DualUOMClassIDDescription:str = obj["DualUOMClassIDDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.FSAssetClassCodeFSAssetClassDesc:str = obj["FSAssetClassCodeFSAssetClassDesc"]
      self.Mtl_AnalysisCdDescription:str = obj["Mtl_AnalysisCdDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OnHoldReasonCodeDescription:str = obj["OnHoldReasonCodeDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RefCategoryDescription:str = obj["RefCategoryDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.XbSystELIEinvoice:bool = obj["XbSystELIEinvoice"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.SalesCatID_c:str = obj["SalesCatID_c"]
      self.CustomBuyout_c:bool = obj["CustomBuyout_c"]
      self.NonSellable_c:bool = obj["NonSellable_c"]
      self.WebSearchable_c:bool = obj["WebSearchable_c"]
      pass

class Erp_Tablesets_QuoteDtlPARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QuoteHedDateQuoted:str = obj["QuoteHedDateQuoted"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustIDBTName:str = obj["CustNumCustIDBTName"]
      self.CustNumCustIDName:str = obj["CustNumCustIDName"]
      self.CustNumCustIDCustID:str = obj["CustNumCustIDCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Entered PartNum  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByIDWithCounters_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      pass

class GetByIDWithCounters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.profitableCounter:int = obj["parameters"]
      self.producedCounter:int = obj["parameters"]
      self.soldCounter:int = obj["parameters"]
      self.quotedCounter:int = obj["parameters"]
      self.onHandExists:bool = obj["onHandExists"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetInvcDtlPAList_input:
   """ Required : 
   whereClauseInvcDtlPA
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcDtlPA:str = obj["whereClauseInvcDtlPA"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetInvcDtlPAList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetInvcDtlPARows_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetInvcDtlPARows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetJobHeadPAList_input:
   """ Required : 
   whereClauseJobHeadPA
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHeadPA:str = obj["whereClauseJobHeadPA"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetJobHeadPAList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetJobHeadPARows_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetJobHeadPARows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetOrderDtlPAList_input:
   """ Required : 
   whereClauseOrderDtlPA
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOrderDtlPA:str = obj["whereClauseOrderDtlPA"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetOrderDtlPAList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetOrderDtlPARows_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetOrderDtlPARows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetPartBinList_input:
   """ Required : 
   whereClausePartBin
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartBin:str = obj["whereClausePartBin"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetPartBinList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPartBinRows_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetPartBinRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetPartDetails_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetPartDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetQuoteDtlPAList_input:
   """ Required : 
   whereClauseQuoteDtlPA
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteDtlPA:str = obj["whereClauseQuoteDtlPA"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetQuoteDtlPAList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetQuoteDtlPARows_input:
   """ Required : 
   iPartNum
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number for which you want details  """  
      pass

class GetQuoteDtlPARows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePart
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePart:str = obj["whereClausePart"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAdvisorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

