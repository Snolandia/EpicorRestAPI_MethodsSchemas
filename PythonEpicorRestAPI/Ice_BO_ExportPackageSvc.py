import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ExportPackageSvc
# Description: This object is used to create and export an export package.
An export package contains a list of records that need to be exported and then
loaded to a customer's database. Examples of such records include BAQ, zDataset, etc.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID(PackageID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExportPackage item
   Description: Calls GetByID to retrieve the ExportPackage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExportPackage
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ExportPackageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPBAQReports_PackageID_BAQRptID(PackageID, BAQRptID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPBAQReport item
   Description: Calls GetByID to retrieve the EPBAQReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBAQReport1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBAQReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPBAQReports(" + PackageID + "," + BAQRptID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPBpDirectiveGroups_PackageID_DirectiveGroup(PackageID, DirectiveGroup, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPBpDirectiveGroup item
   Description: Calls GetByID to retrieve the EPBpDirectiveGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBpDirectiveGroup1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param DirectiveGroup: Desc: DirectiveGroup   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBpDirectiveGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPBpDirectiveGroups(" + PackageID + "," + DirectiveGroup + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPChgLogGAs_PackageID_Company_AlertNum(PackageID, Company, AlertNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPChgLogGA item
   Description: Calls GetByID to retrieve the EPChgLogGA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPChgLogGA1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AlertNum: Desc: AlertNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPChgLogGARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPChgLogGAs(" + PackageID + "," + Company + "," + AlertNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPDashBdDefs_PackageID_Company_ProductID_DefinitionID(PackageID, Company, ProductID, DefinitionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPDashBdDef item
   Description: Calls GetByID to retrieve the EPDashBdDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPDashBdDef1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPDashBdDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPDashBdDefs(" + PackageID + "," + Company + "," + ProductID + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPEfxLibraries_PackageID_LibraryID(PackageID, LibraryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPEfxLibrary item
   Description: Calls GetByID to retrieve the EPEfxLibrary item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPEfxLibrary1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param LibraryID: Desc: LibraryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPEfxLibraryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPEfxLibraries(" + PackageID + "," + LibraryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPExports_PackageID_Company_Approved_UserID_ExportID(PackageID, Company, Approved, UserID, ExportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPExport item
   Description: Calls GetByID to retrieve the EPExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExport1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Approved: Desc: Approved   Required: True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param ExportID: Desc: ExportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExportsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPExports(" + PackageID + "," + Company + "," + Approved + "," + UserID + "," + ExportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPFileContents_PackageID_SourcePath(PackageID, SourcePath, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPFileContent item
   Description: Calls GetByID to retrieve the EPFileContent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPFileContent1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param SourcePath: Desc: SourcePath   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPFileContentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPFileContents(" + PackageID + "," + SourcePath + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPHistories_PackageID_ActionNum_ActionDate(PackageID, ActionNum, ActionDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPHistory item
   Description: Calls GetByID to retrieve the EPHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPHistory1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ActionNum: Desc: ActionNum   Required: True
      :param ActionDate: Desc: ActionDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPHistories(" + PackageID + "," + ActionNum + "," + ActionDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPMenus_PackageID_MenuID(PackageID, MenuID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPMenu item
   Description: Calls GetByID to retrieve the EPMenu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPMenu1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param MenuID: Desc: MenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPMenus(" + PackageID + "," + MenuID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPQuickSearches_PackageID_Company_GlbCompany_QuickSearchID(PackageID, Company, GlbCompany, QuickSearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPQuickSearch item
   Description: Calls GetByID to retrieve the EPQuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPQuickSearch1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPQuickSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPQuickSearches(" + PackageID + "," + Company + "," + GlbCompany + "," + QuickSearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPReports_PackageID_ReportID(PackageID, ReportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPReport item
   Description: Calls GetByID to retrieve the EPReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReport1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPReports(" + PackageID + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPReportStyles_PackageID_ReportID_StyleNum(PackageID, ReportID, StyleNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPReportStyle item
   Description: Calls GetByID to retrieve the EPReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReportStyle1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPReportStyles(" + PackageID + "," + ReportID + "," + StyleNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPRptDataDefs_PackageID_RptDefID(PackageID, RptDefID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPRptDataDef item
   Description: Calls GetByID to retrieve the EPRptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPRptDataDef1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPRptDataDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPRptDataDefs(" + PackageID + "," + RptDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPSecurities_PackageID_Company_SecCode(PackageID, Company, SecCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSecurity item
   Description: Calls GetByID to retrieve the EPSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSecurity1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSecurityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPSecurities(" + PackageID + "," + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPUDCodeTypes_PackageID_Company_CodeTypeID(PackageID, Company, CodeTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPUDCodeType item
   Description: Calls GetByID to retrieve the EPUDCodeType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUDCodeType1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CodeTypeID: Desc: CodeTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUDCodeTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPUDCodeTypes(" + PackageID + "," + Company + "," + CodeTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPUserDefinedTables_PackageID_TableName(PackageID, TableName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPUserDefinedTable item
   Description: Calls GetByID to retrieve the EPUserDefinedTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUserDefinedTable1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUserDefinedTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPUserDefinedTables(" + PackageID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPXXXDefs_PackageID_Company_ProductID_TypeCode_Key1_Key2_Key3(PackageID, Company, ProductID, TypeCode, Key1, Key2, Key3, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPXXXDef item
   Description: Calls GetByID to retrieve the EPXXXDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPXXXDef1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPXXXDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPXXXDefs(" + PackageID + "," + Company + "," + ProductID + "," + TypeCode + "," + Key1 + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPzBODefs_PackageID_ClassName_ObjectNS(PackageID, ClassName, ObjectNS, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPzBODef item
   Description: Calls GetByID to retrieve the EPzBODef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzBODef1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param ObjectNS: Desc: ObjectNS   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzBODefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPzBODefs(" + PackageID + "," + ClassName + "," + ObjectNS + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExportPackages_PackageID_EPzDatas_PackageID_DataTableID(PackageID, DataTableID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPzData item
   Description: Calls GetByID to retrieve the EPzData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzData1
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/ExportPackages(" + PackageID + ")/EPzDatas(" + PackageID + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPBAQReports_PackageID_BAQRptID(PackageID, BAQRptID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPBAQReport item
   Description: Calls GetByID to retrieve the EPBAQReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBAQReport
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param BAQRptID: Desc: BAQRptID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBAQReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPBAQReports(" + PackageID + "," + BAQRptID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPBpDirectiveGroups_PackageID_DirectiveGroup(PackageID, DirectiveGroup, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPBpDirectiveGroup item
   Description: Calls GetByID to retrieve the EPBpDirectiveGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPBpDirectiveGroup
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param DirectiveGroup: Desc: DirectiveGroup   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPBpDirectiveGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPBpDirectiveGroups(" + PackageID + "," + DirectiveGroup + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPChgLogGAs_PackageID_Company_AlertNum(PackageID, Company, AlertNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPChgLogGA item
   Description: Calls GetByID to retrieve the EPChgLogGA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPChgLogGA
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AlertNum: Desc: AlertNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPChgLogGARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPChgLogGAs(" + PackageID + "," + Company + "," + AlertNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPDashBdDefs_PackageID_Company_ProductID_DefinitionID(PackageID, Company, ProductID, DefinitionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPDashBdDef item
   Description: Calls GetByID to retrieve the EPDashBdDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPDashBdDef
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPDashBdDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPDashBdDefs(" + PackageID + "," + Company + "," + ProductID + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPEfxLibraries_PackageID_LibraryID(PackageID, LibraryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPEfxLibrary item
   Description: Calls GetByID to retrieve the EPEfxLibrary item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPEfxLibrary
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param LibraryID: Desc: LibraryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPEfxLibraryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPEfxLibraries(" + PackageID + "," + LibraryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPExports_PackageID_Company_Approved_UserID_ExportID(PackageID, Company, Approved, UserID, ExportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPExport item
   Description: Calls GetByID to retrieve the EPExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExport
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Approved: Desc: Approved   Required: True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param ExportID: Desc: ExportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExportsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPExports(" + PackageID + "," + Company + "," + Approved + "," + UserID + "," + ExportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPFileContents_PackageID_SourcePath(PackageID, SourcePath, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPFileContent item
   Description: Calls GetByID to retrieve the EPFileContent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPFileContent
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param SourcePath: Desc: SourcePath   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPFileContentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPFileContents(" + PackageID + "," + SourcePath + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPHistories_PackageID_ActionNum_ActionDate(PackageID, ActionNum, ActionDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPHistory item
   Description: Calls GetByID to retrieve the EPHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPHistory
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ActionNum: Desc: ActionNum   Required: True
      :param ActionDate: Desc: ActionDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPHistories(" + PackageID + "," + ActionNum + "," + ActionDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPMenus_PackageID_MenuID(PackageID, MenuID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPMenu item
   Description: Calls GetByID to retrieve the EPMenu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPMenu
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param MenuID: Desc: MenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPMenus(" + PackageID + "," + MenuID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPQuickSearches_PackageID_Company_GlbCompany_QuickSearchID(PackageID, Company, GlbCompany, QuickSearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPQuickSearch item
   Description: Calls GetByID to retrieve the EPQuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPQuickSearch
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPQuickSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPQuickSearches(" + PackageID + "," + Company + "," + GlbCompany + "," + QuickSearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPReports_PackageID_ReportID(PackageID, ReportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPReport item
   Description: Calls GetByID to retrieve the EPReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReport
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPReports(" + PackageID + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPReportStyles_PackageID_ReportID_StyleNum(PackageID, ReportID, StyleNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPReportStyle item
   Description: Calls GetByID to retrieve the EPReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPReportStyle
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param StyleNum: Desc: StyleNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPReportStyleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPReportStyles(" + PackageID + "," + ReportID + "," + StyleNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPRptDataDefs_PackageID_RptDefID(PackageID, RptDefID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPRptDataDef item
   Description: Calls GetByID to retrieve the EPRptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPRptDataDef
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPRptDataDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPRptDataDefs(" + PackageID + "," + RptDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSecurities_PackageID_Company_SecCode(PackageID, Company, SecCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSecurity item
   Description: Calls GetByID to retrieve the EPSecurity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSecurity
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SecCode: Desc: SecCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSecurityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSecurities(" + PackageID + "," + Company + "," + SecCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPUDCodeTypes_PackageID_Company_CodeTypeID(PackageID, Company, CodeTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPUDCodeType item
   Description: Calls GetByID to retrieve the EPUDCodeType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUDCodeType
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CodeTypeID: Desc: CodeTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUDCodeTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPUDCodeTypes(" + PackageID + "," + Company + "," + CodeTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPUserDefinedTables_PackageID_TableName(PackageID, TableName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPUserDefinedTable item
   Description: Calls GetByID to retrieve the EPUserDefinedTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPUserDefinedTable
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPUserDefinedTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPUserDefinedTables(" + PackageID + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPXXXDefs_PackageID_Company_ProductID_TypeCode_Key1_Key2_Key3(PackageID, Company, ProductID, TypeCode, Key1, Key2, Key3, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPXXXDef item
   Description: Calls GetByID to retrieve the EPXXXDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPXXXDef
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProductID: Desc: ProductID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPXXXDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPXXXDefs(" + PackageID + "," + Company + "," + ProductID + "," + TypeCode + "," + Key1 + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPzBODefs_PackageID_ClassName_ObjectNS(PackageID, ClassName, ObjectNS, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPzBODef item
   Description: Calls GetByID to retrieve the EPzBODef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzBODef
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param ObjectNS: Desc: ObjectNS   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzBODefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPzBODefs(" + PackageID + "," + ClassName + "," + ObjectNS + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPzDatas_PackageID_DataTableID(PackageID, DataTableID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPzData item
   Description: Calls GetByID to retrieve the EPzData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPzData
      :param PackageID: Desc: PackageID   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPzDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPzDatas(" + PackageID + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPExtensionSets_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPExtensionSet item
   Description: Calls GetByID to retrieve the EPExtensionSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPExtensionSet
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPExtensionSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPExtensionSets(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionDetails_SolutionID_ForeignSysRowID(SolutionID, ForeignSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionDetail item
   Description: Calls GetByID to retrieve the EPSolutionDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionDetail
      :param SolutionID: Desc: SolutionID   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionDetails(" + SolutionID + "," + ForeignSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionDetailDisplays_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionDetailDisplay item
   Description: Calls GetByID to retrieve the EPSolutionDetailDisplay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionDetailDisplay
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionDetailDisplayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionDetailDisplays(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionHeaders_SolutionID(SolutionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionHeader item
   Description: Calls GetByID to retrieve the EPSolutionHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionHeader
      :param SolutionID: Desc: SolutionID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionHeaders(" + SolutionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionPackages_SolutionID_ForeignSysRowID(SolutionID, ForeignSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionPackage item
   Description: Calls GetByID to retrieve the EPSolutionPackage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionPackage
      :param SolutionID: Desc: SolutionID   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionPackageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionPackages(" + SolutionID + "," + ForeignSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionTrackers_SolutionID_TableName_LastUpdated_ForeignSysRowID(SolutionID, TableName, LastUpdated, ForeignSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionTracker item
   Description: Calls GetByID to retrieve the EPSolutionTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionTracker
      :param SolutionID: Desc: SolutionID   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param LastUpdated: Desc: LastUpdated   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTrackerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTrackers(" + SolutionID + "," + TableName + "," + LastUpdated + "," + ForeignSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionTrackerDetails_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionTrackerDetail item
   Description: Calls GetByID to retrieve the EPSolutionTrackerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionTrackerDetail
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTrackerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTrackerDetails(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPSolutionTypes_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPSolutionType item
   Description: Calls GetByID to retrieve the EPSolutionType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPSolutionType
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPSolutionTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPSolutionTypes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EPStructuredReports_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EPStructuredReport item
   Description: Calls GetByID to retrieve the EPStructuredReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EPStructuredReport
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.EPStructuredReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/EPStructuredReports(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ExportPackageListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: This method returns a dataset representing an ExportPackage
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This method returns a list of solutions
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasUnsupportedContentTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasUnsupportedContentTypes
   Description: Has solution files invalid/unsupported content types.
   OperationID: HasUnsupportedContentTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasUnsupportedContentTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasUnsupportedContentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEPFileContents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEPFileContents
   Description: This method creates a EPFileContents row
   OperationID: GetNewEPFileContents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEPFileContents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEPFileContents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEPHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEPHistory
   Description: This method creates a EPHistory row
   OperationID: GetNewEPHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEPHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEPHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExportPackage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExportPackage
   Description: This method creates a new Export package
   OperationID: GetNewExportPackage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExportPackage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExportPackage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Update
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveWorkbenchPromoteDetailRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveWorkbenchPromoteDetailRows
   Description: Removes deleted rows from the SolutionDetail table
   OperationID: RemoveWorkbenchPromoteDetailRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveWorkbenchPromoteDetailRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveWorkbenchPromoteDetailRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveWorkbenchTrackerDetailRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveWorkbenchTrackerDetailRows
   Description: Selects or Removes the row in the SoltutionTracker table
   OperationID: RemoveWorkbenchTrackerDetailRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveWorkbenchTrackerDetailRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveWorkbenchTrackerDetailRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PopulateWorkbenchTrackerDetailPanel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PopulateWorkbenchTrackerDetailPanel
   Description: Populates the detail view in the WorkbenchTrackerDetailPanel
   OperationID: PopulateWorkbenchTrackerDetailPanel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateWorkbenchTrackerDetailPanel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateWorkbenchTrackerDetailPanel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes the Solution
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PopulateWorkbenchPromoteDetailPanel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PopulateWorkbenchPromoteDetailPanel
   Description: Populates the detail view in the WorkbenchPromoteDetailPanel
   OperationID: PopulateWorkbenchPromoteDetailPanel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateWorkbenchPromoteDetailPanel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateWorkbenchPromoteDetailPanel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidBORecByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidBORecByID
   Description: validates the imported row
   OperationID: IsValidBORecByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidBORecByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidBORecByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBORecByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBORecByID
   Description: Gets the row to export
   OperationID: GetBORecByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBORecByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBORecByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMenuModuleType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMenuModuleType
   Description: update the Module for the Menu row
   OperationID: UpdateMenuModuleType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMenuModuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMenuModuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDBScript(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDBScript
   Description: updates the database script in the SolutionScriptStore
   OperationID: UpdateDBScript
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDBScript_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDBScript_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSolutionDBScripts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSolutionDBScripts
   Description: deletes the database script in the SolutionScriptStore for the solution and company
   OperationID: DeleteSolutionDBScripts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSolutionDBScripts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSolutionDBScripts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetElementBOName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetElementBOName
   Description: returns the BO associated with the Solution Element
   OperationID: GetElementBOName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetElementBOName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetElementBOName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExportRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExportRow
   Description: Gets the row to export
   OperationID: GetExportRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExportRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExportRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveTrackedRowsToSolution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveTrackedRowsToSolution
   Description: Move Tracked Selected rows to the Solution
   OperationID: MoveTrackedRowsToSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveTrackedRowsToSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveTrackedRowsToSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddItemToSolution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddItemToSolution
   Description: Add rows (non-tracked) to the Solution
   OperationID: AddItemToSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddItemToSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddItemToSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSolutionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSolutionType
   Description: Validates the Solution Type ID
   OperationID: ValidateSolutionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSolutionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSolutionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstalledSolution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInstalledSolution
   Description: Get the previous install of a solution.
   OperationID: GetInstalledSolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInstalledSolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstalledSolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSolutionInstall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSolutionInstall
   Description: Delete the last record of a solution installation.
   OperationID: DeleteSolutionInstall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSolutionInstall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSolutionInstall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecordSolutionInstall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecordSolutionInstall
   Description: Record the fact that we're installing a solution.
   OperationID: RecordSolutionInstall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecordSolutionInstall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecordSolutionInstall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstalledSolutions(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstalledSolutions
   Description: Get the list of installed solutions.
   OperationID: GetInstalledSolutions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstalledSolutions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSolutionHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSolutionHistory
   Description: Get the history of a solution.
   OperationID: GetSolutionHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSolutionHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSolutionHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Build(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Build
   Description: Build solution package.
   OperationID: Build
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Build_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Build_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBuildSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBuildSettings
   Description: Gets build settings.
   OperationID: GetBuildSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBuildSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBuildSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBuildSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBuildSettings
   Description: Validate build settings.
   OperationID: ValidateBuildSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBuildSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBuildSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstallSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInstallSettings
   Description: Get install settings.
   OperationID: GetInstallSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInstallSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInstallSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInstallSettings
   Description: Validate install settings.
   OperationID: ValidateInstallSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInstallSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInstallSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Install(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Install
   Description: Install solution.
   OperationID: Install
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Install_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Install_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Delete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Delete
   Description: Delete solution.
   OperationID: Delete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Delete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Delete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ExportPackageSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ExportPackageListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ExportPackageListRow] = obj["value"]
      pass

class Ice_Tablesets_EPBAQReportRow:
   def __init__(self, obj):
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Selected:bool = obj["Selected"]
      """  Indicating if this record is selected in the export package  """  
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPBpDirectiveGroupRow:
   def __init__(self, obj):
      self.DirectiveGroup:str = obj["DirectiveGroup"]
      self.DirectiveCount:int = obj["DirectiveCount"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPChgLogGARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AlertNum:int = obj["AlertNum"]
      """  The unique Alert Num of the record.  The AlertNum should be greater than or equal to 2000 to avoid conflicts with standard global alerts.  """  
      self.Selected:bool = obj["Selected"]
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  The description of the alert/change log  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPDashBdDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPEfxLibraryRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.LibraryID:str = obj["LibraryID"]
      """  ID of Epicor Functions Library  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPExportsRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPExtensionSetRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPFileContentsRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  Export Package ID  """  
      self.SourcePath:str = obj["SourcePath"]
      """  Source Path  """  
      self.FileContentType:int = obj["FileContentType"]
      """  File Content Type  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.CabFolder:str = obj["CabFolder"]
      self.Selected:bool = obj["Selected"]
      self.SourceFilename:str = obj["SourceFilename"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPHistoryRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  Export Package ID  """  
      self.ActionNum:int = obj["ActionNum"]
      """  Action Number  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Action Date  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPMenuRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPQuickSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.Selected:bool = obj["Selected"]
      """  Indicating if this record is selected in the export package  """  
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPReportRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.ReportID:str = obj["ReportID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPReportStyleRow:
   def __init__(self, obj):
      self.CGCCode:str = obj["CGCCode"]
      self.Description:str = obj["Description"]
      self.PackageID:str = obj["PackageID"]
      self.ReportID:str = obj["ReportID"]
      self.Selected:bool = obj["Selected"]
      self.StyleNum:int = obj["StyleNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPRptDataDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.RptDefID:str = obj["RptDefID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSecurityRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionDetailDisplayRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionDetailRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Elements:str = obj["Elements"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:int = obj["Selected"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.InstallationOrder:str = obj["InstallationOrder"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionHeaderRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AppVersion:str = obj["AppVersion"]
      """  AppVersion  """  
      self.InternalNotes:str = obj["InternalNotes"]
      """  InternalNotes  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.LastExported:str = obj["LastExported"]
      """  LastExported  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      """  SolutionTypeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BuildIteration:int = obj["BuildIteration"]
      """  BuildIteration  """  
      self.SolutionReference:str = obj["SolutionReference"]
      """  SolutionReference  """  
      self.MinAppVersion:int = obj["MinAppVersion"]
      """  MinAppVersion  """  
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      """  ImportSameRelease  """  
      self.PackageID:str = obj["PackageID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionPackageRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTrackerDetailRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTrackerRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  IsSelected  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Available:int = obj["Available"]
      self.Elements:str = obj["Elements"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:int = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTypeRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      self.Company:str = obj["Company"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.ElementHeaderID:str = obj["ElementHeaderID"]
      self.ParentTableName:str = obj["ParentTableName"]
      self.BusinessObject:str = obj["BusinessObject"]
      self.BOMethod:str = obj["BOMethod"]
      self.ChildTableName:str = obj["ChildTableName"]
      self.ElementDisplayColumnID:int = obj["ElementDisplayColumnID"]
      self.ParentColumnName:str = obj["ParentColumnName"]
      self.DataType:str = obj["DataType"]
      self.ParameterName:str = obj["ParameterName"]
      self.ParameterOrder:int = obj["ParameterOrder"]
      self.ParameterDataType:str = obj["ParameterDataType"]
      self.PackageID:str = obj["PackageID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPStructuredReportRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPUDCodeTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CodeTypeID:str = obj["CodeTypeID"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPUserDefinedTableRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  EP Package ID  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Selected:bool = obj["Selected"]
      """  Selection flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPXXXDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.  
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPzBODefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.ClassName:str = obj["ClassName"]
      self.ObjectNS:str = obj["ObjectNS"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPzDataRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.DataTableID:str = obj["DataTableID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExportPackageListRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      self.AppVersion:str = obj["AppVersion"]
      self.CreateDate:str = obj["CreateDate"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.LastExported:str = obj["LastExported"]
      self.Notes:str = obj["Notes"]
      self.InternalNotes:str = obj["InternalNotes"]
      self.Type:str = obj["Type"]
      """  Solution Type  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.Company:str = obj["Company"]
      self.SolutionID:str = obj["SolutionID"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.SolutionVersion:str = obj["SolutionVersion"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      self.MinAppVersion:int = obj["MinAppVersion"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExportPackageRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      self.AppVersion:str = obj["AppVersion"]
      self.CreateDate:str = obj["CreateDate"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.LastExported:str = obj["LastExported"]
      self.Notes:str = obj["Notes"]
      self.InternalNotes:str = obj["InternalNotes"]
      self.Type:str = obj["Type"]
      """  Solution Type  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.Company:str = obj["Company"]
      self.SolutionID:str = obj["SolutionID"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      self.MinAppVersion:int = obj["MinAppVersion"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddItemToSolution_input:
   """ Required : 
   solutionID
   ds
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      self.ds      #schema had no properties on an object.
      pass

class AddItemToSolution_output:
   def __init__(self, obj):
      pass

class Build_input:
   """ Required : 
   settings
   """  
   def __init__(self, obj):
      self.settings:list[Ice_Tablesets_SolutionBuildSettingsTableset] = obj["settings"]
      pass

class Build_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ExportPackage_SolutionBuildResult] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  the SolutionID  """  
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteSolutionDBScripts_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  the SolutionID of the import  """  
      pass

class DeleteSolutionDBScripts_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  success or failure of the update  """  
      pass

class DeleteSolutionInstall_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  Solution ID.  """  
      pass

class DeleteSolutionInstall_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Whether a row was found to delete.  """  
      pass

   def parameters(self, obj):
      self.content:str = obj["parameters"]
      pass

      """  output parameters  """  

class Delete_input:
   """ Required : 
   solutionID
   allCompanies
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  The solution identifier.  """  
      self.allCompanies:bool = obj["allCompanies"]
      """  if set to `true` [all companies].  """  
      pass

class Delete_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ExportPackage_SolutionResult] = obj["returnObj"]
      pass

class GetBORecByID_input:
   """ Required : 
   xml
   """  
   def __init__(self, obj):
      self.xml:str = obj["xml"]
      pass

class GetBORecByID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetBuildSettings_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  Solution identifier.  """  
      pass

class GetBuildSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SolutionBuildSettingsTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   packageID
   """  
   def __init__(self, obj):
      self.packageID:str = obj["packageID"]
      """  The package ID code  """  
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExportPackageTableset] = obj["returnObj"]
      pass

class GetElementBOName_input:
   """ Required : 
   tableName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      pass

class GetElementBOName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetExportRow_input:
   """ Required : 
   tableName
   foreignSysRowId
   ns
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.foreignSysRowId:str = obj["foreignSysRowId"]
      self.ns:str = obj["ns"]
      pass

class GetExportRow_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetInstallSettings_input:
   """ Required : 
   cabData
   solutionFile
   """  
   def __init__(self, obj):
      self.cabData:str = obj["cabData"]
      """  The CAB data.  """  
      self.solutionFile:str = obj["solutionFile"]
      """  Solution file name.  """  
      pass

class GetInstallSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SolutionInstallSettingsTableset] = obj["returnObj"]
      pass

class GetInstalledSolution_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      pass

class GetInstalledSolution_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.content:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInstalledSolutions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ExportPackage_InstalledSolution] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The whereClause filter  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ExportPackageListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEPFileContents_input:
   """ Required : 
   ds
   packageID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      self.packageID:str = obj["packageID"]
      """  The package ID  """  
      pass

class GetNewEPFileContents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEPHistory_input:
   """ Required : 
   ds
   packageID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      self.packageID:str = obj["packageID"]
      """  The package ID  """  
      pass

class GetNewEPHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExportPackage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

class GetNewExportPackage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSolutionHistory_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      pass

class GetSolutionHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ExportPackage_SolutionEvent] = obj["returnObj"]
      pass

class HasUnsupportedContentTypes_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      pass

class HasUnsupportedContentTypes_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Ice_BO_ExportPackage_InstalledSolution:
   def __init__(self, obj):
      self.CompanyID:str = obj["CompanyID"]
      self.SolutionID:str = obj["SolutionID"]
      self.Description:str = obj["Description"]
      self.FileName:str = obj["FileName"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangedOn:str = obj["ChangedOn"]
      pass

class Ice_BO_ExportPackage_LogRecord:
   def __init__(self, obj):
      self.UtcDate:str = obj["UtcDate"]
      self.Type:int = obj["Type"]
      self.Message:str = obj["Message"]
      pass

class Ice_BO_ExportPackage_SolutionBuildResult:
   def __init__(self, obj):
      self.Content:str = obj["Content"]
      self.HashContent:str = obj["HashContent"]
      self.LogRecords:list[Ice_BO_ExportPackage_LogRecord] = obj["LogRecords"]
      self.HasErrors:bool = obj["HasErrors"]
      pass

class Ice_BO_ExportPackage_SolutionEvent:
   def __init__(self, obj):
      self.CompanyID:str = obj["CompanyID"]
      self.SolutionID:str = obj["SolutionID"]
      self.Sequence:int = obj["Sequence"]
      self.Event:str = obj["Event"]
      self.Description:str = obj["Description"]
      self.FileName:str = obj["FileName"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.CreatedOn:str = obj["CreatedOn"]
      pass

class Ice_BO_ExportPackage_SolutionResult:
   def __init__(self, obj):
      self.LogRecords:list[Ice_BO_ExportPackage_LogRecord] = obj["LogRecords"]
      self.HasErrors:bool = obj["HasErrors"]
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

class Ice_Tablesets_BAQBuildSettingsRow:
   def __init__(self, obj):
      self.QueryDescription:str = obj["QueryDescription"]
      self.QueryID:str = obj["QueryID"]
      self.SCPassword:str = obj["SCPassword"]
      self.SCServer:str = obj["SCServer"]
      self.SCServerUrl:str = obj["SCServerUrl"]
      self.SCUser:str = obj["SCUser"]
      self.SCCredentialsAreValid:bool = obj["SCCredentialsAreValid"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BAQInstallSettingsRow:
   def __init__(self, obj):
      self.ExtDataSourceName:str = obj["ExtDataSourceName"]
      self.OverwriteExistingSCWorkflow:bool = obj["OverwriteExistingSCWorkflow"]
      self.QueryDescription:str = obj["QueryDescription"]
      self.QueryID:str = obj["QueryID"]
      self.QueryType:int = obj["QueryType"]
      self.SCExecPassword:str = obj["SCExecPassword"]
      self.SCExecUser:str = obj["SCExecUser"]
      self.SCPassword:str = obj["SCPassword"]
      self.SCServer:str = obj["SCServer"]
      self.SCServerUrl:str = obj["SCServerUrl"]
      self.SCUser:str = obj["SCUser"]
      self.SCWorkflowPackage:str = obj["SCWorkflowPackage"]
      self.UseCompanyDefaultSCSettings:bool = obj["UseCompanyDefaultSCSettings"]
      self.SCCredentialsAreValid:bool = obj["SCCredentialsAreValid"]
      self.CanImportSCWorkflow:bool = obj["CanImportSCWorkflow"]
      self.SCExecutionCredentialsAreValid:bool = obj["SCExecutionCredentialsAreValid"]
      self.SCExecServer:str = obj["SCExecServer"]
      self.SCWorkflowName:str = obj["SCWorkflowName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPBAQReportRow:
   def __init__(self, obj):
      self.BAQRptID:str = obj["BAQRptID"]
      """  BAQ Report ID, the unique identifier for this report within the company  """  
      self.Selected:bool = obj["Selected"]
      """  Indicating if this record is selected in the export package  """  
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPBpDirectiveGroupRow:
   def __init__(self, obj):
      self.DirectiveGroup:str = obj["DirectiveGroup"]
      self.DirectiveCount:int = obj["DirectiveCount"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPChgLogGARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AlertNum:int = obj["AlertNum"]
      """  The unique Alert Num of the record.  The AlertNum should be greater than or equal to 2000 to avoid conflicts with standard global alerts.  """  
      self.Selected:bool = obj["Selected"]
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  The description of the alert/change log  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPDashBdDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.DefinitionID:str = obj["DefinitionID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPEfxLibraryRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.LibraryID:str = obj["LibraryID"]
      """  ID of Epicor Functions Library  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPExportsRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Approved:bool = obj["Approved"]
      """   no = this exports is a work-in-process one
Since 9.0 there should be only approved BAQs.  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPExtensionSetRow:
   def __init__(self, obj):
      self.ExtensionSetID:str = obj["ExtensionSetID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPFileContentsRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  Export Package ID  """  
      self.SourcePath:str = obj["SourcePath"]
      """  Source Path  """  
      self.FileContentType:int = obj["FileContentType"]
      """  File Content Type  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.CabFolder:str = obj["CabFolder"]
      self.Selected:bool = obj["Selected"]
      self.SourceFilename:str = obj["SourceFilename"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPHistoryRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  Export Package ID  """  
      self.ActionNum:int = obj["ActionNum"]
      """  Action Number  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Action Date  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPMenuRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.MenuID:str = obj["MenuID"]
      """  MM=module, XX=MN,UP,LS,PC, and ZZZZ = number.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPQuickSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.Selected:bool = obj["Selected"]
      """  Indicating if this record is selected in the export package  """  
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPReportRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.ReportID:str = obj["ReportID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPReportStyleRow:
   def __init__(self, obj):
      self.CGCCode:str = obj["CGCCode"]
      self.Description:str = obj["Description"]
      self.PackageID:str = obj["PackageID"]
      self.ReportID:str = obj["ReportID"]
      self.Selected:bool = obj["Selected"]
      self.StyleNum:int = obj["StyleNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPRptDataDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.RptDefID:str = obj["RptDefID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSecurityRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SecCode:str = obj["SecCode"]
      """  Security ID for the Program/SubMenu.  Format is either "XXX999-888" or "XXX999-888", where XXX is either SEC or UD (User Defined), 999 is a number to make the code unique, and -888 is a number used to make a subcomponent unique.  Subcomponents are used to allow more restricted access to a piece of a menu item(program).  For example: Costing information in Job Tracker.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionDetailDisplayRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionDetailRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Elements:str = obj["Elements"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:int = obj["Selected"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.InstallationOrder:str = obj["InstallationOrder"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionHeaderRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AppVersion:str = obj["AppVersion"]
      """  AppVersion  """  
      self.InternalNotes:str = obj["InternalNotes"]
      """  InternalNotes  """  
      self.Notes:str = obj["Notes"]
      """  Notes  """  
      self.LastExported:str = obj["LastExported"]
      """  LastExported  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      """  SolutionTypeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BuildIteration:int = obj["BuildIteration"]
      """  BuildIteration  """  
      self.SolutionReference:str = obj["SolutionReference"]
      """  SolutionReference  """  
      self.MinAppVersion:int = obj["MinAppVersion"]
      """  MinAppVersion  """  
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      """  ImportSameRelease  """  
      self.PackageID:str = obj["PackageID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionPackageRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTrackerDetailRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTrackerRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  SolutionID  """  
      self.TableName:str = obj["TableName"]
      """  TableName  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  IsSelected  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Available:int = obj["Available"]
      self.Elements:str = obj["Elements"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:int = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPSolutionTypeRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      self.Company:str = obj["Company"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.ElementHeaderID:str = obj["ElementHeaderID"]
      self.ParentTableName:str = obj["ParentTableName"]
      self.BusinessObject:str = obj["BusinessObject"]
      self.BOMethod:str = obj["BOMethod"]
      self.ChildTableName:str = obj["ChildTableName"]
      self.ElementDisplayColumnID:int = obj["ElementDisplayColumnID"]
      self.ParentColumnName:str = obj["ParentColumnName"]
      self.DataType:str = obj["DataType"]
      self.ParameterName:str = obj["ParameterName"]
      self.ParameterOrder:int = obj["ParameterOrder"]
      self.ParameterDataType:str = obj["ParameterDataType"]
      self.PackageID:str = obj["PackageID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPStructuredReportRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPUDCodeTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CodeTypeID:str = obj["CodeTypeID"]
      self.PackageID:str = obj["PackageID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPUserDefinedTableRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      """  EP Package ID  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Selected:bool = obj["Selected"]
      """  Selection flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPXXXDefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProductID:str = obj["ProductID"]
      """  VN - Vantage, VS - Vista  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Key1:str = obj["Key1"]
      """   Generic key component field.
Ex: Customization Name if TypeCode =  "Customization" 
FormName if TypeCode = "Personalization"  """  
      self.Key2:str = obj["Key2"]
      """   Generic key component field.
Ex: FormName Name if TypeCode =  "Customization" 
UserID if TypeCode = "Personalization"  """  
      self.Key3:str = obj["Key3"]
      """   Generic key component field.  
Ex: if TypeCode =  "Customization"  this may contain "WIP" or blanks.  """  
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPzBODefRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.ClassName:str = obj["ClassName"]
      self.ObjectNS:str = obj["ObjectNS"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_EPzDataRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.DataTableID:str = obj["DataTableID"]
      self.Selected:bool = obj["Selected"]
      self.Description:str = obj["Description"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExportPackageListRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      self.AppVersion:str = obj["AppVersion"]
      self.CreateDate:str = obj["CreateDate"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.LastExported:str = obj["LastExported"]
      self.Notes:str = obj["Notes"]
      self.InternalNotes:str = obj["InternalNotes"]
      self.Type:str = obj["Type"]
      """  Solution Type  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.Company:str = obj["Company"]
      self.SolutionID:str = obj["SolutionID"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.SolutionVersion:str = obj["SolutionVersion"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      self.MinAppVersion:int = obj["MinAppVersion"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExportPackageListTableset:
   def __init__(self, obj):
      self.ExportPackageList:list[Ice_Tablesets_ExportPackageListRow] = obj["ExportPackageList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ExportPackageRow:
   def __init__(self, obj):
      self.PackageID:str = obj["PackageID"]
      self.Description:str = obj["Description"]
      self.AppVersion:str = obj["AppVersion"]
      self.CreateDate:str = obj["CreateDate"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.LastExported:str = obj["LastExported"]
      self.Notes:str = obj["Notes"]
      self.InternalNotes:str = obj["InternalNotes"]
      self.Type:str = obj["Type"]
      """  Solution Type  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group / Country Code for CSF  """  
      self.Company:str = obj["Company"]
      self.SolutionID:str = obj["SolutionID"]
      self.SolutionTypeID:str = obj["SolutionTypeID"]
      self.BuildIteration:int = obj["BuildIteration"]
      self.SolutionReference:str = obj["SolutionReference"]
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      self.MinAppVersion:int = obj["MinAppVersion"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ExportPackageTableset:
   def __init__(self, obj):
      self.ExportPackage:list[Ice_Tablesets_ExportPackageRow] = obj["ExportPackage"]
      self.EPBAQReport:list[Ice_Tablesets_EPBAQReportRow] = obj["EPBAQReport"]
      self.EPBpDirectiveGroup:list[Ice_Tablesets_EPBpDirectiveGroupRow] = obj["EPBpDirectiveGroup"]
      self.EPChgLogGA:list[Ice_Tablesets_EPChgLogGARow] = obj["EPChgLogGA"]
      self.EPDashBdDef:list[Ice_Tablesets_EPDashBdDefRow] = obj["EPDashBdDef"]
      self.EPEfxLibrary:list[Ice_Tablesets_EPEfxLibraryRow] = obj["EPEfxLibrary"]
      self.EPExports:list[Ice_Tablesets_EPExportsRow] = obj["EPExports"]
      self.EPFileContents:list[Ice_Tablesets_EPFileContentsRow] = obj["EPFileContents"]
      self.EPHistory:list[Ice_Tablesets_EPHistoryRow] = obj["EPHistory"]
      self.EPMenu:list[Ice_Tablesets_EPMenuRow] = obj["EPMenu"]
      self.EPQuickSearch:list[Ice_Tablesets_EPQuickSearchRow] = obj["EPQuickSearch"]
      self.EPReport:list[Ice_Tablesets_EPReportRow] = obj["EPReport"]
      self.EPReportStyle:list[Ice_Tablesets_EPReportStyleRow] = obj["EPReportStyle"]
      self.EPRptDataDef:list[Ice_Tablesets_EPRptDataDefRow] = obj["EPRptDataDef"]
      self.EPSecurity:list[Ice_Tablesets_EPSecurityRow] = obj["EPSecurity"]
      self.EPUDCodeType:list[Ice_Tablesets_EPUDCodeTypeRow] = obj["EPUDCodeType"]
      self.EPUserDefinedTable:list[Ice_Tablesets_EPUserDefinedTableRow] = obj["EPUserDefinedTable"]
      self.EPXXXDef:list[Ice_Tablesets_EPXXXDefRow] = obj["EPXXXDef"]
      self.EPzBODef:list[Ice_Tablesets_EPzBODefRow] = obj["EPzBODef"]
      self.EPzData:list[Ice_Tablesets_EPzDataRow] = obj["EPzData"]
      self.EPExtensionSet:list[Ice_Tablesets_EPExtensionSetRow] = obj["EPExtensionSet"]
      self.EPSolutionDetail:list[Ice_Tablesets_EPSolutionDetailRow] = obj["EPSolutionDetail"]
      self.EPSolutionDetailDisplay:list[Ice_Tablesets_EPSolutionDetailDisplayRow] = obj["EPSolutionDetailDisplay"]
      self.EPSolutionHeader:list[Ice_Tablesets_EPSolutionHeaderRow] = obj["EPSolutionHeader"]
      self.EPSolutionPackage:list[Ice_Tablesets_EPSolutionPackageRow] = obj["EPSolutionPackage"]
      self.EPSolutionTracker:list[Ice_Tablesets_EPSolutionTrackerRow] = obj["EPSolutionTracker"]
      self.EPSolutionTrackerDetail:list[Ice_Tablesets_EPSolutionTrackerDetailRow] = obj["EPSolutionTrackerDetail"]
      self.EPSolutionType:list[Ice_Tablesets_EPSolutionTypeRow] = obj["EPSolutionType"]
      self.EPStructuredReport:list[Ice_Tablesets_EPStructuredReportRow] = obj["EPStructuredReport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_MainBuildSettingsRow:
   def __init__(self, obj):
      self.LibraryType:int = obj["LibraryType"]
      """  Library type.  """  
      self.SolutionID:str = obj["SolutionID"]
      """  Solution identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.Output:str = obj["Output"]
      self.PromptForCABName:bool = obj["PromptForCABName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MainInstallSettingsRow:
   def __init__(self, obj):
      self.SolutionID:str = obj["SolutionID"]
      """  Solution identifier.  """  
      self.Description:str = obj["Description"]
      """  Solution description.  """  
      self.SourceVersion:str = obj["SourceVersion"]
      """  Source version.  """  
      self.DestinationVersion:str = obj["DestinationVersion"]
      """  Destination version.  """  
      self.SolutionFile:str = obj["SolutionFile"]
      """  Solution file.  """  
      self.InstallNotes:str = obj["InstallNotes"]
      """  Installation notes.  """  
      self.BuildIteration:int = obj["BuildIteration"]
      """  Build iteration.  """  
      self.SolutionReference:str = obj["SolutionReference"]
      """  Solution reference.  """  
      self.MinAppVersion:int = obj["MinAppVersion"]
      """  Minimum application version.  """  
      self.ImportSameRelease:bool = obj["ImportSameRelease"]
      """  Import the same release.  """  
      self.LibraryType:int = obj["LibraryType"]
      """  Library type.  """  
      self.SourceCabSchema:str = obj["SourceCabSchema"]
      """  Source CAB schema.  """  
      self.SourceCompany:str = obj["SourceCompany"]
      """  Source company.  """  
      self.IncludesFilesForDeployment:bool = obj["IncludesFilesForDeployment"]
      """  Includes files for deployment.  """  
      self.ValidationHash:str = obj["ValidationHash"]
      """  Validation hash.  """  
      self.AutoOverwriteDuplicateFile:bool = obj["AutoOverwriteDuplicateFile"]
      """  Auto overwrite duplicate file.  """  
      self.AutoOverwriteDuplicateData:bool = obj["AutoOverwriteDuplicateData"]
      """  Auto overwrite duplicate data.  """  
      self.DeletePreviousInstall:bool = obj["DeletePreviousInstall"]
      """  Delete previous install.  """  
      self.OverrideDirectives:bool = obj["OverrideDirectives"]
      """  Override directives.  """  
      self.OnlyTargetCurrentCompany:bool = obj["OnlyTargetCurrentCompany"]
      """  Only target current company.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.Output:str = obj["Output"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_PromptInstallSettingsRow:
   def __init__(self, obj):
      self.TargetBasePath:int = obj["TargetBasePath"]
      """  Predefined server paths.  """  
      self.RelativePath:str = obj["RelativePath"]
      """  Relative path for selected Target Base Path.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.SolutionItem:str = obj["SolutionItem"]
      """  File name with extension or a folder name.  """  
      self.ItemType:int = obj["ItemType"]
      """  Source item type (file or directory).  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleBuildSettingsRow:
   def __init__(self, obj):
      self.ExportImage:bool = obj["ExportImage"]
      """  Export image option.  """  
      self.ExportRDL:bool = obj["ExportRDL"]
      """  Export RDL file option.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report identifier.  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Style description.  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Style identifier.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.ExportCertificate:bool = obj["ExportCertificate"]
      """  Export certificate option.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportStyleInstallSettingsRow:
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Report Style Description  """  
      self.CertificateID:str = obj["CertificateID"]
      """  Certificate ID  """  
      self.OverwriteCertificate:bool = obj["OverwriteCertificate"]
      """  Overwrite Certificate  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SolutionBuildSettingsTableset:
   def __init__(self, obj):
      self.BAQBuildSettings:list[Ice_Tablesets_BAQBuildSettingsRow] = obj["BAQBuildSettings"]
      self.MainBuildSettings:list[Ice_Tablesets_MainBuildSettingsRow] = obj["MainBuildSettings"]
      self.ReportStyleBuildSettings:list[Ice_Tablesets_ReportStyleBuildSettingsRow] = obj["ReportStyleBuildSettings"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SolutionInstallSettingsTableset:
   def __init__(self, obj):
      self.BAQInstallSettings:list[Ice_Tablesets_BAQInstallSettingsRow] = obj["BAQInstallSettings"]
      self.MainInstallSettings:list[Ice_Tablesets_MainInstallSettingsRow] = obj["MainInstallSettings"]
      self.PromptInstallSettings:list[Ice_Tablesets_PromptInstallSettingsRow] = obj["PromptInstallSettings"]
      self.ReportStyleInstallSettings:list[Ice_Tablesets_ReportStyleInstallSettingsRow] = obj["ReportStyleInstallSettings"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Install_input:
   """ Required : 
   cabData
   settings
   """  
   def __init__(self, obj):
      self.cabData:str = obj["cabData"]
      """  The CAB data.  """  
      self.settings:list[Ice_Tablesets_SolutionInstallSettingsTableset] = obj["settings"]
      pass

class Install_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ExportPackage_SolutionResult] = obj["returnObj"]
      pass

class IsValidBORecByID_input:
   """ Required : 
   xml
   """  
   def __init__(self, obj):
      self.xml:str = obj["xml"]
      pass

class IsValidBORecByID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class MoveTrackedRowsToSolution_input:
   """ Required : 
   solutionID
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      pass

class MoveTrackedRowsToSolution_output:
   def __init__(self, obj):
      pass

class PopulateWorkbenchPromoteDetailPanel_input:
   """ Required : 
   elementType
   solutionID
   """  
   def __init__(self, obj):
      self.elementType:str = obj["elementType"]
      self.solutionID:str = obj["solutionID"]
      pass

class PopulateWorkbenchPromoteDetailPanel_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class PopulateWorkbenchTrackerDetailPanel_input:
   """ Required : 
   elementType
   solutionID
   """  
   def __init__(self, obj):
      self.elementType:str = obj["elementType"]
      self.solutionID:str = obj["solutionID"]
      pass

class PopulateWorkbenchTrackerDetailPanel_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class RecordSolutionInstall_input:
   """ Required : 
   solutionID
   description
   fileName
   content
   buildIteration
   solutionReference
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      self.description:str = obj["description"]
      self.fileName:str = obj["fileName"]
      self.content:str = obj["content"]
      self.buildIteration:int = obj["buildIteration"]
      self.solutionReference:str = obj["solutionReference"]
      pass

class RecordSolutionInstall_output:
   def __init__(self, obj):
      pass

class RemoveWorkbenchPromoteDetailRows_input:
   """ Required : 
   foreignSysRowIDs
   solutionID
   """  
   def __init__(self, obj):
      self.foreignSysRowIDs:str = obj["foreignSysRowIDs"]
      """  the foreignsysrowid(s) of the row to delete  """  
      self.solutionID:str = obj["solutionID"]
      """  the users solutionID  """  
      pass

class RemoveWorkbenchPromoteDetailRows_output:
   def __init__(self, obj):
      pass

class RemoveWorkbenchTrackerDetailRows_input:
   """ Required : 
   foreignSysRowIDs
   solutionID
   delete
   IsSelected
   """  
   def __init__(self, obj):
      self.foreignSysRowIDs:str = obj["foreignSysRowIDs"]
      self.solutionID:str = obj["solutionID"]
      self.delete:bool = obj["delete"]
      self.IsSelected:bool = obj["IsSelected"]
      pass

class RemoveWorkbenchTrackerDetailRows_output:
   def __init__(self, obj):
      pass

class UpdateDBScript_input:
   """ Required : 
   solutionID
   scriptName
   scriptContent
   runSequence
   notes
   """  
   def __init__(self, obj):
      self.solutionID:str = obj["solutionID"]
      """  the SolutionID of the import  """  
      self.scriptName:str = obj["scriptName"]
      """  the file name of the script being imported  """  
      self.scriptContent:str = obj["scriptContent"]
      """  the script content  """  
      self.runSequence:int = obj["runSequence"]
      """  the sequence to run the script in the DatabaseScriptRunner  """  
      self.notes:str = obj["notes"]
      """  the user notes for this script  """  
      pass

class UpdateDBScript_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  success or failure of the update  """  
      pass

class UpdateMenuModuleType_input:
   """ Required : 
   importID
   importModuleType
   """  
   def __init__(self, obj):
      self.importID:str = obj["importID"]
      """  the MenuID  """  
      self.importModuleType:str = obj["importModuleType"]
      """  the Menu Module  """  
      pass

class UpdateMenuModuleType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  success  """  
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ExportPackageTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBuildSettings_input:
   """ Required : 
   settings
   """  
   def __init__(self, obj):
      self.settings:list[Ice_Tablesets_SolutionBuildSettingsTableset] = obj["settings"]
      pass

class ValidateBuildSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SolutionBuildSettingsTableset] = obj["returnObj"]
      pass

class ValidateInstallSettings_input:
   """ Required : 
   settings
   """  
   def __init__(self, obj):
      self.settings:list[Ice_Tablesets_SolutionInstallSettingsTableset] = obj["settings"]
      pass

class ValidateInstallSettings_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SolutionInstallSettingsTableset] = obj["returnObj"]
      pass

class ValidateSolutionType_input:
   """ Required : 
   solutionTypeID
   """  
   def __init__(self, obj):
      self.solutionTypeID:str = obj["solutionTypeID"]
      """  The Solution Type ID  """  
      pass

class ValidateSolutionType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  false if the Solution Type ID is not valid in the database  """  
      pass

